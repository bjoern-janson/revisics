# STRUCTURE-001 Reference Implementation Plan V3

> **Execution mode:** inline TDD. Follow tasks in order. Stop on any failed control rather than changing scientific semantics.

**Goal:** Build the cheapest transparent Python **3.13.5** reference implementation that mechanically realizes `SYSTEM_CONSTRUCTION_MANIFEST_V1.md @ f5874063b06997f49f3ee80d291de879c8d27a7f`, then demonstrate I0-I4 with exactly two complete quarantined control traversals. Do not generate the primary frozen universe.

**Scientific authority:** `f5874063b06997f49f3ee80d291de879c8d27a7f`  
**Base implementation design:** `535013cf4ce97234c1777a3ae1d7884c0578b455`  
**Implementation-design amendment:** `docs/superpowers/specs/2026-09-09-structure-001-reference-implementation-amendment-v1.md`  
**Scientific changes:** NONE

## Cost constitution

The machine remains the boring executor of the stones, but we do not pay for redundant work.

```text
local TDD / symbolic controls
        ↓
complete CONTROL_RUN A   ← first full V1 traversal
        ↓
complete CONTROL_RUN B   ← second full V1 traversal
        ↓
record-level + integrity comparison
        ↓
STOP FOR IMPLEMENTATION-LOCK REVIEW
```

There is no third full-domain preflight run. Exact observed counts are checked inside A and B. Runtime dependencies are standard library only; pytest is test-only. No package installation is required.

## Global hard rules

- Exact runtime: `sys.version_info[:3] == (3, 13, 5)`.
- Candidate IDs, outcomes, applicability, scores, or implementations never enter construction code.
- No randomness, model calls, network access, wall-clock semantics, filesystem-order semantics, locale dependence, process-scheduling semantics, or Python-hash semantics.
- Every scientific/control record is immutable and canonically encoded.
- `CONTROL_FAILURE -> STOP`; no repair mode, sampling fallback, or silent reinterpretation.
- `PRIMARY_UNIVERSE_RUN` stays blocked until separately reviewed and authorized `IMPLEMENTATION_LOCK` exists.

## Files

```text
pyproject.toml
scripts/structure001
experiments/STRUCTURE-001/implementation-controls/
    PRE_IMPLEMENTATION_CUSTODY_V1.txt
src/revisics_structure001/
    __init__.py
    __main__.py
    constants.py
    model.py
    encoding.py
    identity.py
    generation.py
    canonical.py
    validation.py
    provenance.py
    audit.py
    replay.py
    families/{__init__,f1,f2,f3,f4,f5}.py
tests/structure001/
    test_custody.py
    test_encoding.py
    test_f1.py
    test_f2.py
    test_f3.py
    test_f4.py
    test_f5.py
    test_canonical.py
    test_validation.py
    test_provenance.py
    test_audit.py
    test_replay.py
    test_count_contract.py
```

---

# Task 1 — I0 custody and exact runtime before implementation source

**Create:** `pyproject.toml`, custody record, `tests/structure001/test_custody.py`. Do not create `src/` yet.

Custody record exact fields:

```text
record_type=PreImplementationCustodyRecord
record_version=structure001-custody-v1
manifest_sha=f5874063b06997f49f3ee80d291de879c8d27a7f
parent_scientific_contract_sha=9711a6dd1b14ade10fd43a03c424ddc840cc565e
parent_candidate_ontology_sha=7d1e3cf3bd61b212d6131a7e1d98c10f401aa95d
implementation_branch_base_sha=f5874063b06997f49f3ee80d291de879c8d27a7f
raw_constructions_generated=0
canonical_worlds_generated=0
f5_recoding_cases_generated=0
candidate_case_outcomes_observed=0
```

`pyproject.toml`:

```toml
[project]
name = "revisics-structure001"
version = "0.0.0"
requires-python = "==3.13.5"
dependencies = []

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

Tests:

1. exact `sys.version_info[:3] == (3,13,5)`;
2. Git blob SHA of the three scientific artifacts remains exactly:
   - preregistration `1200d1388082441ef0bfc68e52c8a14c94027458`
   - candidate manifest `5ee1d18642ab8f7025d2db157207c8069303a050`
   - system manifest `502d37b98c16086fe013bdca4c166122ed1e637e`
3. all four zero-state custody assertions are present.

Run:

```bash
python -m pytest tests/structure001/test_custody.py -v
```

Expected PASS. Commit:

```bash
git add pyproject.toml experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt tests/structure001/test_custody.py
git commit -m "control: record STRUCTURE-001 preimplementation custody"
```

---

# Task 2 — Immutable kernel, explicit failures, canonical encoding, identities

**TDD RED first.** Create tests before source.

Required `ControlFailure` constructor:

```python
class ControlFailure(RuntimeError):
    def __init__(
        self,
        control_id: str,
        family: str | None = None,
        record_id: str | None = None,
        expected: str = "",
        observed: str = "",
    ) -> None:
        self.control_id = control_id
        self.family = family
        self.record_id = record_id
        self.expected = expected
        self.observed = observed
        super().__init__(
            f"{control_id}: family={family!r} record_id={record_id!r} "
            f"expected={expected!r} observed={observed!r}"
        )
```

Frozen slotted dataclasses:

```text
PreImplementationCustodyRecord
TransportWitness(phi_x, phi_a)
F1Object(n,m,targets)
F2Object(n,m,targets,partition)
F3Object(n,m,targets,costs,updates,regimes)
ExtensionKey(history,action,target)
HistoryDecision(key,allowed)
F4Object(n,m,targets,horizon,decisions)
F5BaseObject(n,m,targets,costs,horizon)
CanonicalizedObject
ValidityRecord
RawConstructionRecord
CanonicalWorldRecord
ProvenanceEdge
F5RecodingRecord
TypedCountRecord
AuditManifest
ControlRunResult
```

Canonical encoder supports only `None`, bool, int, str, bytes, tuple, frozenset, and frozen dataclasses; every type and field is framed; frozensets sort encoded elements; unsupported values raise `ENCODING_UNSUPPORTED`; no `repr`, pickle, marshal, or JSON object-order dependence.

Use encoding version `structure001-canonical-v1`. SHA-256 is the only content identity.

RED tests must prove:
- dataclass immutability;
- `ControlFailure(control_id="X", expected="a", observed="b")` works and retains fields;
- frozenset order independence;
- transport image sequences encode deterministically;
- unsupported object fails rather than falling back.

Run RED, implement minimum, run GREEN, commit:

```bash
git commit -m "feat: add STRUCTURE-001 typed encoding kernel"
```

---

# Task 3 — F1 and F2 generation

Interfaces:

```python
iter_f1(n,m)
iter_partitions(n)
normalize_partition(labels)
iter_f2(n,m)
```

F1 uses `(None, *range(n))` in every `(a,x)` cell, cell index `a*n+x`. F2 partitions are generated directly as normalized restricted-growth strings.

Cheap tests:
- F1 `(n=2,m=1)` has `9` tables;
- Bell counts for `n=1,2,3` are `1,2,5`;
- no duplicate F2 partitions for a small carrier;
- symbolic frozen raw totals evaluate to `267137` and `1333172` from the exact grammar formulas.

Do **not** perform the complete F1/F2 universe traversal merely to re-count here. The actual iterators are exhaustively counted in each complete control run.

RED -> GREEN -> commit:

```bash
git commit -m "feat: enumerate STRUCTURE-001 F1 and F2"
```

---

# Task 4 — F3 exact resource/regime grammar

Edge order is ascending transition-table cell index. For `k` executable edges:

```text
costs:   product((0,1), repeat=k)
updates: product((None,0,1), repeat=2*k)
regimes: ((0,1),(0,2),(1,1),(1,2))
```

Update index is `resource*k + edge_index`. Resource carrier labels are fixed and never relabeled.

RED tests:
- one executable edge produces exactly `18` decorations;
- explicit `0 -> 1 -> bot` update permits one traversal and rejects the second;
- symbolic grammar sum equals exactly `2,049,144`;
- no monotonicity filter exists.

Do not iterate all 2,049,144 cases in unit tests. Full emitted count is checked in both control runs.

RED -> GREEN -> commit:

```bash
git commit -m "feat: enumerate STRUCTURE-001 F3"
```

---

# Task 5 — F4 normalized history extension

Interfaces:

```python
iter_f4(n,m,horizon)
admissible_histories(obj,t)
has_current_state_collision(obj)
executable_extension_keys(...)
```

Only currently admissible histories create next-step alpha decisions. No inert descendant bit exists below a forbidden prefix.

Corrected RED controls:

```python
def test_forbidden_prefix_has_no_descendant_decision():
    blocked = next(
        w for w in iter_f4(1, 1, 2)
        if w.decisions and w.decisions[0].allowed is False
    )
    assert len(blocked.decisions) == 1
```

Negative collision control: `n=m=1` deterministic carrier cannot supply two distinct same-time histories ending at the same state.

Positive collision control: construct `n=2,m=1` raw core with both states transitioning to state `0`; allow both first-step extensions. At `t=1`, histories `(0,0,0)` and `(1,0,0)` are distinct and end at state `0`; `has_current_state_collision` must be true.

The complete F4 normalized space is only 13,056 and may be counted locally. Assert:

```text
normalized total = 13056
valid labeled (2,2,2) = 10886
```

RED -> GREEN -> commit:

```bash
git commit -m "feat: enumerate normalized STRUCTURE-001 F4"
```

---

# Task 6 — F5 labeled bases and recoding witnesses

Interfaces:

```python
iter_f5_labeled_bases(n,m)
iter_recoding_witnesses(n,m)
transport_f5(base,witness)
instance_id(base)
recoding_id(base_id,witness)
```

Witnesses are all state permutations crossed with all action permutations; identity included. `RecodingID = SHA256(CanonicalEncode(BaseID,phi_X,phi_A))`, never destination bytes.

RED tests:
- `(2,2)` has exactly four witnesses;
- every emitted witness is bijective;
- identity exists;
- a symmetric base may have equal destination bytes under distinct witnesses but must have distinct RecodingIDs;
- symbolic labeled-base grammar total equals `133899`.

Do not exhaustively expand all primary F5 recodings yet. Full emitted counts happen in A/B.

RED -> GREEN -> commit:

```bash
git commit -m "feat: enumerate STRUCTURE-001 F5 bases and recodings"
```

---

# Task 7 — Exhaustive canonicalization with unique transport witness

Each family implements exact transport under state/action bijections. F2 renormalizes transported observation blocks by first occurrence; F3 fixes resource labels; F4 transports every state/action occurrence in histories and decision keys; F5 canonicalizes bases only before recoding expansion.

Canonical selection:

```python
rows = []
for witness in all_witnesses(n,m):
    transported = family_transport(obj,witness)
    rows.append((canonical_encode(transported), canonical_encode(witness), transported, witness))
object_bytes, transport_bytes, payload, witness = min(rows, key=lambda r: (r[0],r[1]))
```

RED controls:
- relabeling invariance;
- idempotence;
- explicit automorphism tie chooses minimum transport bytes, not first enumerated witness;
- F3 resource labels never move;
- F5 post-expansion recodings are not canonical-deduplicated.

Full canonical totals are **not** recomputed in a separate preflight traversal. They are observed and checked inside both complete control runs:

```text
F1 8344
F2 40839
F3 500079
F4 2862
F4(2,2,2) 2784
F5 base 11718
```

RED -> GREEN -> commit:

```bash
git commit -m "feat: add exhaustive STRUCTURE-001 canonicalization"
```

---

# Task 8 — Rule-derived validators, including every actual F5 recoding

Interfaces:

```python
validate(obj) -> ValidityRecord
validate_f5_recoding(base,witness,destination) -> ValidityRecord
```

No validator repairs input.

Negative reason-code controls:

```text
F1_TARGET_OUT_OF_RANGE
F2_PARTITION_INVALID
F3_COST_OUT_OF_RANGE
F3_UPDATE_OUT_OF_CODOMAIN
F3_REGIME_BUNDLE_MISMATCH
F4_EXTENSION_KEY_INCONSISTENT
F4_NO_CURRENT_STATE_COLLISION
F5_EXEC_TRANSPORT_MISMATCH
F5_COST_TRANSPORT_MISMATCH
```

For every F5 recoding produced in a control run, the pipeline must:

```text
destination = transport_f5(base,witness)
validity = validate_f5_recoding(base,witness,destination)
write validity to L_V
if invalid: CONTROL_FAILURE -> STOP
only then emit F5RecodingRecord
```

RED test must inject a deterministic broken transport and prove it cannot pass merely because replay reproduces the same bug.

RED -> GREEN -> commit:

```bash
git commit -m "feat: validate STRUCTURE-001 family contracts"
```

---

# Task 9 — Canonical ledgers and provenance graph `L_P`

Canonical ledger framing:

```text
ASCII_decimal_length ':' payload
```

Sort full canonical record bytes before writing. Reader must reject malformed framing.

Every raw->canonical edge retains unique canonical transport witness. Every F5 recoding edge binds manifest SHA, implementation ID, BaseID, InstanceID, RecodingID, witness, and identity flag. Every provenance edge goes into `L_P`.

RED controls:
- write/read exact roundtrip;
- input order does not alter emitted ledger order;
- two raw sources for one canonical object remain two provenance edges;
- removing/changing a provenance edge is observable.

RED -> GREEN -> commit:

```bash
git commit -m "feat: add STRUCTURE-001 provenance ledger"
```

---

# Task 10 — Count-bound ledger commitments and AuditBundle

Ledger root algorithm:

1. sort canonical record bytes;
2. leaf:

```python
SHA256(b"structure001-leaf-v1\0" + tag + b"\0" + record)
```

3. internal node:

```python
SHA256(b"structure001-node-v1\0" + left + right)
```

4. odd level may duplicate final node;
5. final root **must bind exact record count**:

```python
SHA256(
    b"structure001-root-v2\0"
    + tag + b"\0"
    + str(record_count).encode("ascii") + b"\0"
    + tree_digest
).hexdigest()
```

The empty tree digest is separately domain-separated and then passed through the same count-bound final root.

Required RED regression:

```python
assert merkle_root([b"a",b"b",b"c"],"L_P") != merkle_root([b"a",b"b",b"c",b"c"],"L_P")
```

`AuditManifest` binds exact manifest SHA, implementation identity, `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, and `TypedCountRecord`. `AuditBundle = SHA256(CanonicalEncode(AuditManifest))`.

RED -> GREEN -> commit:

```bash
git commit -m "feat: bind STRUCTURE-001 audit bundle"
```

---

# Task 11 — Quarantined replay, F5 completeness, per-run integrity verification, CLI bootstrap

Required interface:

```python
run_control(
    output_dir: Path,
    implementation_id: str,
    *,
    test_mode: bool = False,
    test_limits: TestLimits | None = None,
) -> ControlRunResult

verify_run_integrity(run_dir: Path) -> VerifiedRun
compare_control_runs(left: Path,right: Path) -> None
```

If `test_limits` is provided without `test_mode=True`, raise `CONTROL_FAILURE`. Production CLI exposes no test-mode/bound override.

## F5 emitted-stream completeness

For each canonical F5 base:

```python
seen = set()
emitted = 0
identity_seen = False
for witness in iter_recoding_witnesses(n,m):
    assert sorted(witness.phi_x) == list(range(n))
    assert sorted(witness.phi_a) == list(range(m))
    key = (witness.phi_x,witness.phi_a)
    if key in seen: fail duplicate
    seen.add(key)
    identity_seen |= key == (tuple(range(n)),tuple(range(m)))

    destination = transport_f5(base,witness)
    vr = validate_f5_recoding(base,witness,destination)
    emit vr to L_V
    if not vr.valid: STOP
    emit recoding record to L_F5
    emitted += 1

assert identity_seen
assert emitted == len(seen) == factorial(n)*factorial(m)
```

The run-level `f5_recodings` count is incremented from actual emitted `L_F5` records only. It is never assigned from expected cardinality.

## Per-run integrity before comparison

`verify_run_integrity` independently:
- reads retained `L_R,L_C,L_V,L_P,L_F5`;
- recomputes each count-bound root;
- checks recomputed roots against stored metadata;
- reconstructs `AuditManifest` from validated roots + retained typed counts;
- recomputes the bundle digest;
- checks it equals stored `AuditBundle`;
- returns only if internally self-consistent.

`compare_control_runs` first calls `verify_run_integrity` on **both** runs, then byte-compares record streams, typed counts, roots, and bundles. Two identically stale/altered runs must therefore fail before cross-run equality can bless them.

## CLI with zero install cost

Create `scripts/structure001`:

```sh
#!/usr/bin/env sh
set -eu
ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
PYTHONPATH="$ROOT/src${PYTHONPATH:+:$PYTHONPATH}" exec python -m revisics_structure001 "$@"
```

The Python CLI itself verifies exact Python 3.13.5 before any semantic action. Mark script executable.

Mandatory smoke check outside pytest:

```bash
./scripts/structure001 --help
```

Expected exit 0.

RED controls also cover:
- missing/nonzero custody -> reject;
- nonempty output directory -> reject;
- production CLI has no bound override;
- `primary-universe-run` fails without authorized implementation-lock record;
- tiny test-mode replay passes;
- altered provenance ledger with stale stored root fails `verify_run_integrity`;
- identical altered run copies cannot pass comparison.

RED -> GREEN -> commit:

```bash
git commit -m "feat: add quarantined STRUCTURE-001 replay"
```

---

# Task 12 — Cheap preflight contract suite, no full universe traversal

Create `test_count_contract.py` to check the frozen acceptance table and symbolic raw formulas without pretending constants are observed counts.

Frozen expected observed values for the production control-run checker:

```text
F1 raw                    267137
F1 canonical                8344
F2 raw                   1333172
F2 canonical               40839
F3 raw                   2049144
F3 canonical              500079
F4 normalized              13056
F4 valid labeled (2,2,2)   10886
F4 canonical                2862
F4 canonical (2,2,2)        2784
F5 labeled bases          133899
F5 canonical bases         11718
F5 emitted recodings      139216
assay cases               691340
```

The production count checker receives **observed counters from traversal** and compares them to this table. It must not manufacture observed values from the table.

Run the complete local suite:

```bash
python -m pytest tests/structure001 -v
./scripts/structure001 --help
```

Expected PASS with no complete V1 traversal yet.

Commit:

```bash
git commit -m "test: freeze STRUCTURE-001 implementation controls"
```

---

# Task 13 — Exactly two complete control runs, I0-I4 evidence, then STOP

Before running, record exact implementation commit:

```bash
git rev-parse HEAD
```

Set this as `IMPLEMENTATION_ID`. Both runs must use identical code identity.

Keep full control outputs outside Git history under:

```text
.structure001-control/control-run-a/
.structure001-control/control-run-b/
```

Add `.structure001-control/` to local `.git/info/exclude`, not repository `.gitignore`.

## Run A — first complete traversal

```bash
./scripts/structure001 control-run \
  --output .structure001-control/control-run-a \
  --implementation-id "$IMPLEMENTATION_ID"
```

The run itself checks every observed raw/canonical/F5 count against the frozen table and stops on mismatch.

Then:

```bash
./scripts/structure001 verify-run .structure001-control/control-run-a
```

Must PASS internal root/bundle verification.

## Run B — second and final complete traversal before lock review

```bash
./scripts/structure001 control-run \
  --output .structure001-control/control-run-b \
  --implementation-id "$IMPLEMENTATION_ID"
./scripts/structure001 verify-run .structure001-control/control-run-b
```

Both must PASS.

## Cross-run I4

```bash
./scripts/structure001 compare-control-runs \
  .structure001-control/control-run-a \
  .structure001-control/control-run-b
```

Comparison performs internal verification again before equality comparison.

## Durable evidence

Create:

```text
experiments/STRUCTURE-001/implementation-controls/CONTROL_ARTIFACT_INDEX_V1.txt
experiments/STRUCTURE-001/implementation-controls/IMPLEMENTATION_ACCEPTANCE_V1.md
```

Index every retained file in A/B by path, byte size, SHA-256. If full control artifacts cannot be retained through independent review, record `CONTROL_ARTIFACT_RETENTION_FAILURE` and STOP.

Acceptance record contains observed evidence only:

```text
manifest_sha
implementation_sha
python_version=3.13.5
custody_record_sha256
artifact_index_sha256
I0 PASS/FAIL + evidence
I1 PASS/FAIL + observed raw counts
I2 PASS/FAIL + observed canonical counts + tie controls
I3 PASS/FAIL + F5 per-recoding validation + L_P evidence
I4 PASS/FAIL + both verified AuditBundles + record comparison
primary_universe_run=NOT_EXECUTED
candidate_evaluation=NOT_EXECUTED
claim_ceiling=implementation fidelity only; no scientific result
```

Do not write PASS before evidence exists.

Fresh final check:

```bash
python -m pytest tests/structure001 -v
./scripts/structure001 verify-run .structure001-control/control-run-a
./scripts/structure001 verify-run .structure001-control/control-run-b
./scripts/structure001 compare-control-runs \
  .structure001-control/control-run-a \
  .structure001-control/control-run-b
```

Commit only acceptance/index metadata, never the full ledgers by accident:

```bash
git add experiments/STRUCTURE-001/implementation-controls/IMPLEMENTATION_ACCEPTANCE_V1.md \
        experiments/STRUCTURE-001/implementation-controls/CONTROL_ARTIFACT_INDEX_V1.txt
git commit -m "control: record STRUCTURE-001 I0-I4 evidence index"
```

Then STOP.

```text
DO NOT create IMPLEMENTATION_LOCK
DO NOT run PRIMARY_UNIVERSE_RUN
DO NOT freeze a world universe
DO NOT implement/evaluate candidates
DO NOT make a scientific claim
```

---

# Acceptance mapping

```text
I0 custody
    exact scientific blobs + exact four-zero record + Python 3.13.5

I1 generation fidelity
    actual emitted raw/normalized counts in each complete control run

I2 canonicalization fidelity
    local invariance/idempotence/tie controls + actual canonical counts in A/B

I3 validation/provenance fidelity
    negative controls + every actual F5 recoding validated + complete L_P + content IDs

I4 deterministic replay
    each run internally reverified + record equality + count-bound roots + AuditBundle equality
```

Claim ceiling remains:

> Successful I0-I4 acceptance demonstrates only that the reference software faithfully realizes the frozen STRUCTURE-001 V1 construction contract. It is not a scientific result of STRUCTURE-001.
