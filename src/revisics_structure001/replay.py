from __future__ import annotations

import sys
from dataclasses import dataclass, fields
from itertools import islice, zip_longest
from math import factorial
from pathlib import Path
from typing import Iterable, Iterator

from .audit import audit_bundle_digest, build_audit_manifest, merkle_root_sorted
from .canonical import canonicalize
from .constants import *
from .encoding import canonical_encode
from .families.f1 import iter_f1
from .families.f2 import iter_f2
from .families.f3 import iter_f3
from .families.f4 import iter_f4
from .families.f5 import instance_id, iter_f5_labeled_bases, iter_recoding_witnesses, recoding_id, transport_f5
from .identity import content_id
from .model import CanonicalWorldRecord,ControlFailure,ControlRunResult,F5RecodingRecord,PreImplementationCustodyRecord,RawConstructionRecord,TypedCountRecord
from .provenance import ExternalLedgerWriter,canonical_to_assay_edge,f5_recoding_edge,iter_framed_records,raw_to_canonical_edge
from .validation import validate, validate_f5_recoding

REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CUSTODY_PATH = REPO_ROOT / "experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt"
FAMILY_ORDER=("F1","F2","F3","F4","F5")
LEDGER_TAGS=("L_R","L_C","L_V","L_P","L_F5")

@dataclass(frozen=True,slots=True)
class TestLimits:
    families:tuple[str,...]=("F1",)
    raw_limit_per_family:int=2
TestLimits.__test__=False

@dataclass(frozen=True,slots=True)
class VerifiedRun:
    run_dir:Path; manifest_sha:str; implementation_id:str; counts:TypedCountRecord; raw_root:str; canonical_root:str; validity_root:str; provenance_root:str; f5_root:str; audit_digest:str

def _require_runtime():
    if sys.version_info[:3]!=(3,13,5): raise ControlFailure(control_id="PYTHON_RUNTIME_MISMATCH",expected="3.13.5",observed=".".join(map(str,sys.version_info[:3])))
def _parse_kv(path):
    if not path.is_file(): raise ControlFailure(control_id="RUN_METADATA_MISSING",expected="retained metadata file",observed=str(path))
    result={}
    for line_number,line in enumerate(path.read_text(encoding="utf-8").splitlines(),1):
        if not line or "=" not in line: raise ControlFailure(control_id="RUN_METADATA_MALFORMED",expected="key=value",observed=f"{path}:{line_number}:{line!r}")
        key,value=line.split("=",1)
        if key in result: raise ControlFailure(control_id="RUN_METADATA_MALFORMED",expected="unique keys",observed=f"duplicate {key!r}")
        result[key]=value
    return result
def _write_kv(path,items): path.write_text("".join(f"{k}={v}\n" for k,v in items),encoding="utf-8")
def require_custody(path):
    if not path.is_file(): raise ControlFailure(control_id="I0_CUSTODY_MISSING",expected="retained PreImplementationCustodyRecord",observed=str(path))
    values=_parse_kv(path); required={"record_type","record_version","manifest_sha","parent_scientific_contract_sha","parent_candidate_ontology_sha","implementation_branch_base_sha","raw_constructions_generated","canonical_worlds_generated","f5_recoding_cases_generated","candidate_case_outcomes_observed"}
    if set(values)!=required: raise ControlFailure(control_id="I0_CUSTODY_SCHEMA",expected=str(sorted(required)),observed=str(sorted(values)))
    if values["record_type"]!="PreImplementationCustodyRecord" or values["record_version"]!="structure001-custody-v1": raise ControlFailure(control_id="I0_CUSTODY_SCHEMA",expected="PreImplementationCustodyRecord/structure001-custody-v1",observed=f"{values['record_type']}/{values['record_version']}")
    expected_ids={"manifest_sha":MANIFEST_COMMIT_SHA,"parent_scientific_contract_sha":PARENT_CONTRACT_SHA,"parent_candidate_ontology_sha":CANDIDATE_LOCK_SHA,"implementation_branch_base_sha":MANIFEST_COMMIT_SHA}
    for key,expected in expected_ids.items():
        if values[key]!=expected: raise ControlFailure(control_id="I0_CUSTODY_IDENTITY",expected=f"{key}={expected}",observed=f"{key}={values[key]}")
    zeros=("raw_constructions_generated","canonical_worlds_generated","f5_recoding_cases_generated","candidate_case_outcomes_observed"); parsed={}
    for key in zeros:
        try: parsed[key]=int(values[key])
        except ValueError as exc: raise ControlFailure(control_id="I0_CUSTODY_SCHEMA",expected=f"integer {key}",observed=values[key]) from exc
        if parsed[key]!=0: raise ControlFailure(control_id="I0_CUSTODY_NONZERO",expected=f"{key}=0",observed=f"{key}={parsed[key]}")
    return PreImplementationCustodyRecord(values["record_type"],values["record_version"],values["manifest_sha"],values["parent_scientific_contract_sha"],values["parent_candidate_ontology_sha"],values["implementation_branch_base_sha"],parsed[zeros[0]],parsed[zeros[1]],parsed[zeros[2]],parsed[zeros[3]])

def _all_family_objects(family):
    if family=="F1":
        for n in range(1,4):
            for m in range(1,4): yield from iter_f1(n,m)
    elif family=="F2":
        for n in range(1,4):
            for m in range(1,4): yield from iter_f2(n,m)
    elif family=="F3":
        for n in range(1,4):
            for m in range(1,4):
                if n*m<=4: yield from iter_f3(n,m)
    elif family=="F4":
        for n in (1,2):
            for m in (1,2):
                for horizon in (1,2): yield from iter_f4(n,m,horizon)
    elif family=="F5":
        for n in (2,3):
            for m in (2,3):
                if n*m<=6: yield from iter_f5_labeled_bases(n,m)
    else: raise ControlFailure(control_id="FAMILY_UNKNOWN",expected=str(FAMILY_ORDER),observed=family)
def _selected_families(test_mode,test_limits):
    if not test_mode or test_limits is None: return FAMILY_ORDER
    unknown=set(test_limits.families)-set(FAMILY_ORDER)
    if unknown or len(set(test_limits.families))!=len(test_limits.families): raise ControlFailure(control_id="TEST_LIMITS_INVALID",expected=f"unique subset of {FAMILY_ORDER}",observed=str(test_limits.families))
    if test_limits.raw_limit_per_family<1: raise ControlFailure(control_id="TEST_LIMITS_INVALID",expected="raw_limit_per_family >= 1",observed=str(test_limits.raw_limit_per_family))
    return tuple(f for f in FAMILY_ORDER if f in test_limits.families)
def _family_objects(family,test_mode,test_limits):
    stream=_all_family_objects(family)
    yield from islice(stream,test_limits.raw_limit_per_family) if test_mode and test_limits is not None else stream
def _append(writer,record): writer.append(canonical_encode(record))
def _check_canonical_collision(seen,canonical_id,canonical_bytes,family):
    existing=seen.get(canonical_id)
    if existing is None: seen[canonical_id]=canonical_bytes; return True
    if existing!=canonical_bytes: raise ControlFailure(control_id="CANONICAL_ID_COLLISION",family=family,record_id=canonical_id,expected="same content for repeated canonical ID",observed="different canonical bytes")
    return False
def _identity_witness(n,m): return tuple(range(n)),tuple(range(m))
def expected_counts_record():
    return TypedCountRecord(EXPECTED_F1_RAW,EXPECTED_F1_CANONICAL,EXPECTED_F2_RAW,EXPECTED_F2_CANONICAL,EXPECTED_F3_RAW,EXPECTED_F3_CANONICAL,EXPECTED_F4_NORMALIZED,EXPECTED_F4_222_VALID_LABELED,EXPECTED_F4_CANONICAL,EXPECTED_F4_222_CANONICAL,EXPECTED_F5_LABELED_BASES,EXPECTED_F5_CANONICAL_BASES,EXPECTED_F5_RECODINGS,EXPECTED_ASSAY_CASES)
def _check_production_counts(counts):
    expected=expected_counts_record()
    if counts!=expected: raise ControlFailure(control_id="FROZEN_COUNT_MISMATCH",expected=str(expected),observed=str(counts))
def _build_counts(counters): return TypedCountRecord(**{f.name:counters.get(f.name,0) for f in fields(TypedCountRecord)})

def run_control(output_dir,implementation_id,*,test_mode=False,test_limits=None):
    _require_runtime()
    if test_limits is not None and not test_mode: raise ControlFailure(control_id="TEST_LIMITS_FORBIDDEN",expected="test_limits only with test_mode=True",observed=str(test_limits))
    require_custody(Path(DEFAULT_CUSTODY_PATH)); output_dir=Path(output_dir)
    if output_dir.exists() and any(output_dir.iterdir()): raise ControlFailure(control_id="CONTROL_OUTPUT_NOT_EMPTY",expected="missing or empty output directory",observed=str(output_dir))
    output_dir.mkdir(parents=True,exist_ok=True); families=_selected_families(test_mode,test_limits); writers={tag:ExternalLedgerWriter(output_dir/f"{tag}.bin") for tag in LEDGER_TAGS}; counters={}; f5_canonical_bases={}
    for family in families:
        seen={}; f4_222_seen=set()
        for obj in _family_objects(family,test_mode,test_limits):
            raw_id=content_id(obj); raw_bytes=canonical_encode(obj); _append(writers["L_R"],RawConstructionRecord(family,raw_id,raw_bytes))
            counter_name={"F1":"f1_raw","F2":"f2_raw","F3":"f3_raw","F4":"f4_normalized","F5":"f5_labeled_bases"}[family]; counters[counter_name]=counters.get(counter_name,0)+1
            validity=validate(obj); _append(writers["L_V"],validity)
            if not validity.valid:
                if family=="F4" and validity.reason_code=="F4_NO_CURRENT_STATE_COLLISION": continue
                raise ControlFailure(control_id="GENERATED_INVALID_OBJECT",family=family,record_id=raw_id,expected="generator emits semantically valid object",observed=validity.reason_code)
            if family=="F4" and obj.n==2 and obj.m==2 and obj.horizon==2: counters["f4_valid_labeled_222"]=counters.get("f4_valid_labeled_222",0)+1
            canonical=canonicalize(obj); _append(writers["L_P"],raw_to_canonical_edge(MANIFEST_COMMIT_SHA,implementation_id,family,raw_id,canonical.canonical_id,canonical.witness))
            if not _check_canonical_collision(seen,canonical.canonical_id,canonical.canonical_bytes,family): continue
            _append(writers["L_C"],CanonicalWorldRecord(family,canonical.canonical_id,canonical.canonical_bytes))
            if family!="F5": _append(writers["L_P"],canonical_to_assay_edge(MANIFEST_COMMIT_SHA,implementation_id,family,canonical.canonical_id,canonical.canonical_id))
            else: f5_canonical_bases[canonical.canonical_id]=canonical.payload
            if family=="F4" and obj.n==2 and obj.m==2 and obj.horizon==2: f4_222_seen.add(canonical.canonical_id)
        if family=="F1": counters["f1_canonical"]=len(seen)
        elif family=="F2": counters["f2_canonical"]=len(seen)
        elif family=="F3": counters["f3_canonical"]=len(seen)
        elif family=="F4": counters["f4_canonical"]=len(seen); counters["f4_canonical_222"]=len(f4_222_seen)
        elif family=="F5": counters["f5_canonical_bases"]=len(seen)
    if "F5" in families:
        for base_id in sorted(f5_canonical_bases):
            base=f5_canonical_bases[base_id]; seen_witnesses=set(); emitted=0; identity_seen=False; expected_identity=_identity_witness(base.n,base.m)
            for witness in iter_recoding_witnesses(base.n,base.m):
                if tuple(sorted(witness.phi_x))!=tuple(range(base.n)) or tuple(sorted(witness.phi_a))!=tuple(range(base.m)): raise ControlFailure(control_id="F5_RECODING_COMPLETENESS",family="F5",record_id=base_id,expected="bijections",observed=str(witness))
                key=(witness.phi_x,witness.phi_a)
                if key in seen_witnesses: raise ControlFailure(control_id="F5_RECODING_COMPLETENESS",family="F5",record_id=base_id,expected="no duplicate witness",observed=str(key))
                seen_witnesses.add(key); identity_seen=identity_seen or key==expected_identity
                destination=transport_f5(base,witness); vr=validate_f5_recoding(base,witness,destination); _append(writers["L_V"],vr)
                if not vr.valid: raise ControlFailure(control_id="F5_RECODING_INVALID",family="F5",record_id=base_id,expected="exact execution/accounting transport",observed=vr.reason_code)
                instance=instance_id(destination); recoding=recoding_id(base_id,witness); identity_recoding=key==expected_identity
                _append(writers["L_F5"],F5RecodingRecord(base_id,instance,recoding,witness,canonical_encode(destination),identity_recoding)); _append(writers["L_P"],f5_recoding_edge(MANIFEST_COMMIT_SHA,implementation_id,base_id,instance,recoding,witness,identity_recoding)); emitted+=1; counters["f5_recodings"]=counters.get("f5_recodings",0)+1
            expected_emitted=factorial(base.n)*factorial(base.m)
            if not identity_seen or emitted!=len(seen_witnesses) or emitted!=expected_emitted: raise ControlFailure(control_id="F5_RECODING_COMPLETENESS",family="F5",record_id=base_id,expected=f"identity present; unique emitted={expected_emitted}",observed=f"identity={identity_seen}; emitted={emitted}; unique={len(seen_witnesses)}")
    counters["assay_cases"]=sum(counters.get(x,0) for x in ("f1_canonical","f2_canonical","f3_canonical","f4_canonical","f5_recodings")); counts=_build_counts(counters)
    if not test_mode: _check_production_counts(counts)
    for writer in writers.values(): writer.finalize()
    roots={tag:merkle_root_sorted(iter_framed_records(output_dir/f"{tag}.bin"),tag) for tag in LEDGER_TAGS}; manifest=build_audit_manifest(MANIFEST_COMMIT_SHA,implementation_id,roots["L_R"],roots["L_C"],roots["L_V"],roots["L_P"],roots["L_F5"],counts); audit_digest=audit_bundle_digest(manifest)
    _write_kv(output_dir/"run.txt",(("manifest_sha",MANIFEST_COMMIT_SHA),("implementation_id",implementation_id),("python_version","3.13.5"),("test_mode",int(test_mode))))
    _write_kv(output_dir/"counts.txt",((f.name,getattr(counts,f.name)) for f in fields(TypedCountRecord))); _write_kv(output_dir/"roots.txt",((tag,roots[tag]) for tag in LEDGER_TAGS)); _write_kv(output_dir/"audit.txt",(("AuditBundle",audit_digest),))
    return ControlRunResult(str(output_dir),implementation_id,counts,roots["L_R"],roots["L_C"],roots["L_V"],roots["L_P"],roots["L_F5"],audit_digest)

def _counts_from_file(path):
    values=_parse_kv(path); names=[f.name for f in fields(TypedCountRecord)]
    if set(values)!=set(names): raise ControlFailure(control_id="RUN_COUNTS_SCHEMA",expected=str(names),observed=str(sorted(values)))
    try: return TypedCountRecord(**{n:int(values[n]) for n in names})
    except ValueError as exc: raise ControlFailure(control_id="RUN_COUNTS_SCHEMA",expected="integer count values",observed=str(values)) from exc
def _sorted_records(path):
    previous=None
    for index,record in enumerate(iter_framed_records(path)):
        if previous is not None and record<previous: raise ControlFailure(control_id="RUN_LEDGER_NOT_SORTED",record_id=f"{path.name}:{index}",expected="nondecreasing canonical record bytes",observed="out-of-order record")
        previous=record; yield record
def verify_run_integrity(run_dir):
    _require_runtime(); run_dir=Path(run_dir); run_meta=_parse_kv(run_dir/"run.txt")
    if run_meta.get("manifest_sha")!=MANIFEST_COMMIT_SHA: raise ControlFailure(control_id="RUN_INTEGRITY_MANIFEST_MISMATCH",expected=MANIFEST_COMMIT_SHA,observed=run_meta.get("manifest_sha","<missing>"))
    if run_meta.get("python_version")!="3.13.5": raise ControlFailure(control_id="RUN_INTEGRITY_RUNTIME_MISMATCH",expected="3.13.5",observed=run_meta.get("python_version","<missing>"))
    implementation_id=run_meta.get("implementation_id")
    if not implementation_id: raise ControlFailure(control_id="RUN_INTEGRITY_IMPLEMENTATION_MISSING",expected="nonempty implementation_id",observed=str(implementation_id))
    counts=_counts_from_file(run_dir/"counts.txt"); stored_roots=_parse_kv(run_dir/"roots.txt")
    if set(stored_roots)!=set(LEDGER_TAGS): raise ControlFailure(control_id="RUN_ROOTS_SCHEMA",expected=str(LEDGER_TAGS),observed=str(sorted(stored_roots)))
    recomputed={}
    for tag in LEDGER_TAGS:
        ledger_path=run_dir/f"{tag}.bin"
        if not ledger_path.is_file(): raise ControlFailure(control_id="RUN_LEDGER_MISSING",expected=f"{tag}.bin",observed=str(ledger_path))
        recomputed[tag]=merkle_root_sorted(_sorted_records(ledger_path),tag)
        if recomputed[tag]!=stored_roots[tag]: raise ControlFailure(control_id="RUN_INTEGRITY_ROOT_MISMATCH",record_id=tag,expected=stored_roots[tag],observed=recomputed[tag])
    manifest=build_audit_manifest(MANIFEST_COMMIT_SHA,implementation_id,recomputed["L_R"],recomputed["L_C"],recomputed["L_V"],recomputed["L_P"],recomputed["L_F5"],counts); recomputed_audit=audit_bundle_digest(manifest); stored_audit=_parse_kv(run_dir/"audit.txt").get("AuditBundle")
    if recomputed_audit!=stored_audit: raise ControlFailure(control_id="RUN_INTEGRITY_AUDIT_MISMATCH",expected=str(stored_audit),observed=recomputed_audit)
    return VerifiedRun(run_dir,MANIFEST_COMMIT_SHA,implementation_id,counts,recomputed["L_R"],recomputed["L_C"],recomputed["L_V"],recomputed["L_P"],recomputed["L_F5"],recomputed_audit)
def _compare_record_streams(left,right,tag):
    sentinel=object()
    for index,(a,b) in enumerate(zip_longest(iter_framed_records(left/f"{tag}.bin"),iter_framed_records(right/f"{tag}.bin"),fillvalue=sentinel)):
        if a!=b: raise ControlFailure(control_id="I4_REPLAY_MISMATCH",record_id=f"{tag}:{index}",expected="record-level equality",observed="different record bytes or stream length")
def compare_control_runs(left,right):
    vl=verify_run_integrity(left); vr=verify_run_integrity(right)
    if vl.manifest_sha!=vr.manifest_sha or vl.implementation_id!=vr.implementation_id: raise ControlFailure(control_id="I4_REPLAY_MISMATCH",record_id="identity",expected=f"{vl.manifest_sha}/{vl.implementation_id}",observed=f"{vr.manifest_sha}/{vr.implementation_id}")
    for tag in LEDGER_TAGS: _compare_record_streams(Path(left),Path(right),tag)
    if vl.counts!=vr.counts: raise ControlFailure(control_id="I4_REPLAY_MISMATCH",record_id="counts",expected=str(vl.counts),observed=str(vr.counts))
    left_roots=(vl.raw_root,vl.canonical_root,vl.validity_root,vl.provenance_root,vl.f5_root); right_roots=(vr.raw_root,vr.canonical_root,vr.validity_root,vr.provenance_root,vr.f5_root)
    if left_roots!=right_roots or vl.audit_digest!=vr.audit_digest: raise ControlFailure(control_id="I4_REPLAY_MISMATCH",record_id="roots_or_bundle",expected=f"roots={left_roots},audit={vl.audit_digest}",observed=f"roots={right_roots},audit={vr.audit_digest}")
