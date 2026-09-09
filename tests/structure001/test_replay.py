from pathlib import Path
import shutil
import pytest
from revisics_structure001.model import ControlFailure,F5BaseObject,TransportWitness
from revisics_structure001.provenance import read_framed_records,write_canonical_ledger
from revisics_structure001.replay import TestLimits,compare_control_runs,require_custody,run_control,verify_run_integrity

def tiny_limits(*families,raw_limit=2): return TestLimits(families=tuple(families),raw_limit_per_family=raw_limit)
def test_require_custody_rejects_missing_file(tmp_path):
    with pytest.raises(ControlFailure) as exc: require_custody(tmp_path/"missing.txt")
    assert exc.value.control_id=="I0_CUSTODY_MISSING"
def test_run_control_rejects_limits_without_test_mode(tmp_path):
    with pytest.raises(ControlFailure) as exc: run_control(tmp_path/"run","impl-test",test_limits=tiny_limits("F1"))
    assert exc.value.control_id=="TEST_LIMITS_FORBIDDEN"
def test_run_control_rejects_nonempty_output_directory(tmp_path):
    output=tmp_path/"run"; output.mkdir(); (output/"junk").write_text("x")
    with pytest.raises(ControlFailure) as exc: run_control(output,"impl-test",test_mode=True,test_limits=tiny_limits("F1"))
    assert exc.value.control_id=="CONTROL_OUTPUT_NOT_EMPTY"
def test_nonzero_custody_is_rejected(tmp_path,monkeypatch):
    import revisics_structure001.replay as replay
    source=Path(replay.DEFAULT_CUSTODY_PATH); bad=tmp_path/"custody.txt"; bad.write_text(source.read_text().replace("raw_constructions_generated=0","raw_constructions_generated=1")); monkeypatch.setattr(replay,"DEFAULT_CUSTODY_PATH",bad)
    with pytest.raises(ControlFailure) as exc: replay.run_control(tmp_path/"run","impl-test",test_mode=True,test_limits=tiny_limits("F1"))
    assert exc.value.control_id=="I0_CUSTODY_NONZERO"
def test_tiny_replay_is_record_identical_and_integrity_verified(tmp_path):
    limits=tiny_limits("F1","F5",raw_limit=2); left=tmp_path/"a"; right=tmp_path/"b"; run_control(left,"impl-test",test_mode=True,test_limits=limits); run_control(right,"impl-test",test_mode=True,test_limits=limits); assert verify_run_integrity(left).audit_digest==verify_run_integrity(right).audit_digest; compare_control_runs(left,right)
def test_stale_provenance_root_is_detected_before_comparison(tmp_path):
    run=tmp_path/"run"; run_control(run,"impl-test",test_mode=True,test_limits=tiny_limits("F1",raw_limit=2)); p=run/"L_P.bin"; records=list(read_framed_records(p)); write_canonical_ledger(p,records+[records[-1]])
    with pytest.raises(ControlFailure) as exc: verify_run_integrity(run)
    assert exc.value.control_id=="RUN_INTEGRITY_ROOT_MISMATCH"
def test_identically_corrupted_copies_cannot_pass_compare(tmp_path):
    left=tmp_path/"a"; right=tmp_path/"b"; run_control(left,"impl-test",test_mode=True,test_limits=tiny_limits("F1",raw_limit=2)); shutil.copytree(left,right)
    for run in (left,right):
        p=run/"L_P.bin"; records=list(read_framed_records(p)); write_canonical_ledger(p,records+[records[-1]])
    with pytest.raises(ControlFailure) as exc: compare_control_runs(left,right)
    assert exc.value.control_id=="RUN_INTEGRITY_ROOT_MISMATCH"
def test_broken_f5_transport_cannot_replay_itself_into_acceptance(tmp_path,monkeypatch):
    import revisics_structure001.replay as replay
    correct=replay.transport_f5
    def broken(base,witness):
        destination=correct(base,witness)
        if any(target is not None for target in destination.targets):
            targets=list(destination.targets); index=next(i for i,target in enumerate(targets) if target is not None); targets[index]=None; costs=destination.costs[:-1]; return F5BaseObject(destination.n,destination.m,tuple(targets),costs,destination.horizon)
        return destination
    monkeypatch.setattr(replay,"transport_f5",broken)
    with pytest.raises(ControlFailure) as exc: replay.run_control(tmp_path/"run","impl-test",test_mode=True,test_limits=tiny_limits("F5",raw_limit=2))
    assert exc.value.control_id=="F5_RECODING_INVALID"
def test_f5_witness_omission_fails_per_base_completeness(tmp_path,monkeypatch):
    import revisics_structure001.replay as replay
    def only_identity(n,m): yield TransportWitness(tuple(range(n)),tuple(range(m)))
    monkeypatch.setattr(replay,"iter_recoding_witnesses",only_identity)
    with pytest.raises(ControlFailure) as exc: replay.run_control(tmp_path/"run","impl-test",test_mode=True,test_limits=tiny_limits("F5",raw_limit=1))
    assert exc.value.control_id=="F5_RECODING_COMPLETENESS"
def test_primary_universe_command_is_guarded_without_lock(tmp_path):
    from revisics_structure001.__main__ import main
    code=main(["primary-universe-run","--output",str(tmp_path/"primary"),"--implementation-lock",str(tmp_path/"missing-lock.txt")]); assert code!=0
def test_production_control_cli_has_no_test_limit_flags():
    from revisics_structure001.__main__ import build_parser
    parser=build_parser(); control=next(action for action in parser._subparsers._group_actions).choices["control-run"]; help_text=control.format_help(); assert "test-mode" not in help_text and "raw-limit" not in help_text and "bound" not in help_text
