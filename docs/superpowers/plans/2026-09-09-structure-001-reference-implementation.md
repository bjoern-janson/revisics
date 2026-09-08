# STRUCTURE-001 Reference Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the transparent Python 3.12 reference implementation that mechanically realizes `SYSTEM_CONSTRUCTION_MANIFEST_V1.md @ f5874063b06997f49f3ee80d291de879c8d27a7f`, then demonstrate I0-I4 with two quarantined complete control runs without generating the primary frozen universe.

**Architecture:** A standard-library-only `src/revisics_structure001/` package implements immutable typed family objects, one canonical encoder, SHA-256 identities, exhaustive F1-F5 generators, exhaustive relabeling canonicalization with deterministic transport tie-breaking, rule-derived validation, append-only provenance ledgers, deterministic audit roots, and quarantined replay. The manifest is the semantic authority; implementation disagreement is `CONTROL_FAILURE -> STOP`.

**Tech Stack:** Python 3.12, Python standard library, pytest as the only test dependency.

**Spec:** `docs/superpowers/specs/2026-09-08-structure-001-reference-implementation-design.md @ 535013cf4ce97234c1777a3ae1d7884c0578b455`

## Global Constraints

- Scientific authority is `experiments/STRUCTURE-001/SYSTEM_CONSTRUCTION_MANIFEST_V1.md @ f5874063b06997f49f3ee80d291de879c8d27a7f`.
- Parent scientific contract remains `9711a6dd1b14ade10fd43a03c424ddc840cc565e`; parent candidate ontology remains `7d1e3cf3bd61b212d6131a7e1d98c10f401aa95d`.
- Scientific changes permitted: NONE.
- Reference runtime dependencies: Python standard library only. Test dependency: pytest.
- No network access, model calls, randomness, wall-clock dependence, filesystem-enumeration dependence, locale dependence, process-scheduling dependence, or Python hash-randomization may affect semantic output.
- No candidate ID, outcome, score, or implementation may enter generation, canonicalization, validity, provenance, or replay logic.
- Every implementation mismatch with the manifest is `CONTROL_FAILURE -> STOP`; no best-effort, auto-repair, fallback sampling, or semantic patching.
- `CONTROL_RUN` outputs are quarantined implementation-control evidence only. `PRIMARY_UNIVERSE_RUN` remains blocked until a separately reviewed and authorized implementation lock exists.
- Do not implement candidate evaluation or the later F4 target-sensitive sufficiency test in this plan.
- Task 1 is an I0 custody gate and deliberately precedes TDD because the zero-state record must exist before implementation code. TDD begins at Task 2.
- After Task 1, every implementation task follows RED -> minimal implementation -> GREEN -> commit.

## File Map

- `pyproject.toml` — local project/test configuration; no runtime dependency declaration beyond the standard library.
- `experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt` — retained I0/S2 zero-state record created before `src/` code.
- `src/revisics_structure001/constants.py` — frozen SHAs, encoding version, family bounds, expected counts.
- `src/revisics_structure001/model.py` — immutable family and ledger record types plus `ControlFailure`.
- `src/revisics_structure001/encoding.py` — canonical field framing and typed record encoding.
- `src/revisics_structure001/identity.py` — SHA-256 content identities only.
- `src/revisics_structure001/families/f1.py` ... `f5.py` — family-native enumeration and transport operations.
- `src/revisics_structure001/generation.py` — family dispatch and count accounting only.
- `src/revisics_structure001/canonical.py` — exhaustive typed relabeling and representative selection.
- `src/revisics_structure001/validation.py` — typed validity checks; never repair.
- `src/revisics_structure001/provenance.py` — provenance edges and deterministic ledger emission.
- `src/revisics_structure001/audit.py` — ledger roots and `AuditBundle`.
- `src/revisics_structure001/replay.py` — run classes, quarantine, record-level replay comparison.
- `src/revisics_structure001/__main__.py` — control CLI; primary-run command guarded by an implementation-lock record.
- `tests/structure001/` — custody, encoding, each family, canonicalization, validation, provenance, audit, replay, and full-count controls.

---

### Task 1: Establish I0 custody before any generator exists

**Files:**
- Create: `pyproject.toml`
- Create: `experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt`
- Create: `tests/structure001/test_custody.py`

**Interfaces:**
- Produces: fixed line-oriented `PreImplementationCustodyRecord`, later parsed by `replay.require_custody(path: Path) -> PreImplementationCustodyRecord`.
- Depends on: three frozen scientific artifact identities only.

- [ ] **Step 1: Create the custody record before any `src/` implementation file**

Use this exact content and field order:

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

- [ ] **Step 2: Add pytest configuration without a build-time dependency surface**

```toml
[project]
name = "revisics-structure001"
version = "0.0.0"
requires-python = ">=3.12"
dependencies = []

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

- [ ] **Step 3: Add custody and Git-blob-hash verification**

```python
from hashlib import sha1
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOCKED = {
    "experiments/STRUCTURE-001/PREREGISTRATION_V1.md": "1200d1388082441ef0bfc68e52c8a14c94027458",
    "experiments/STRUCTURE-001/CANDIDATE_SPECIFICATION_MANIFEST_V1.md": "5ee1d18642ab8f7025d2db157207c8069303a050",
    "experiments/STRUCTURE-001/SYSTEM_CONSTRUCTION_MANIFEST_V1.md": "502d37b98c16086fe013bdca4c166122ed1e637e",
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return sha1(header + data).hexdigest()


def test_parent_scientific_blobs_are_unchanged():
    for relative, expected in LOCKED.items():
        assert git_blob_sha(ROOT / relative) == expected


def test_custody_record_has_all_four_zero_assertions():
    text = (ROOT / "experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt").read_text()
    for line in (
        "raw_constructions_generated=0",
        "canonical_worlds_generated=0",
        "f5_recoding_cases_generated=0",
        "candidate_case_outcomes_observed=0",
    ):
        assert line in text
```

- [ ] **Step 4: Verify I0 custody**

Run: `python -m pytest tests/structure001/test_custody.py -v`

Expected: PASS. Failure means STOP before any generator code exists.

- [ ] **Step 5: Commit**

```bash
git add pyproject.toml experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt tests/structure001/test_custody.py
git commit -m "control: record STRUCTURE-001 preimplementation custody"
```

---

### Task 2: Define immutable records, control failures, canonical encoding, and identities

**Files:**
- Create: `src/revisics_structure001/__init__.py`
- Create: `src/revisics_structure001/constants.py`
- Create: `src/revisics_structure001/model.py`
- Create: `src/revisics_structure001/encoding.py`
- Create: `src/revisics_structure001/identity.py`
- Create: `tests/structure001/test_encoding.py`

**Interfaces:**
- Produces: `ControlFailure`, `F1Object`, `F2Object`, `F3Object`, `F4Object`, `F5BaseObject`, `TransportWitness`, `CanonicalizedObject`, ledger record dataclasses, `canonical_encode(value: object) -> bytes`, `sha256_hex(data: bytes) -> str`.

- [ ] **Step 1: Write RED immutable/encoding tests**

```python
from dataclasses import FrozenInstanceError
import pytest
from revisics_structure001.encoding import canonical_encode
from revisics_structure001.model import F1Object, TransportWitness


def test_f1_object_is_immutable():
    obj = F1Object(n=1, m=1, targets=(None,))
    with pytest.raises(FrozenInstanceError):
        obj.n = 2


def test_unordered_collection_encoding_is_order_independent():
    assert canonical_encode(frozenset({3, 1, 2})) == canonical_encode(frozenset({2, 3, 1}))


def test_transport_encoding_uses_image_sequence():
    witness = TransportWitness(phi_x=(1, 0), phi_a=(0,))
    assert canonical_encode(witness) == canonical_encode(TransportWitness((1, 0), (0,)))
```

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_encoding.py -v`

Expected: FAIL because package/types do not exist.

- [ ] **Step 3: Implement constants and immutable records**

```python
MANIFEST_COMMIT_SHA = "f5874063b06997f49f3ee80d291de879c8d27a7f"
MANIFEST_BLOB_SHA = "502d37b98c16086fe013bdca4c166122ed1e637e"
PARENT_CONTRACT_SHA = "9711a6dd1b14ade10fd43a03c424ddc840cc565e"
CANDIDATE_LOCK_SHA = "7d1e3cf3bd61b212d6131a7e1d98c10f401aa95d"
ENCODING_VERSION = "structure001-canonical-v1"
EXPECTED_RAW = {"F1": 267137, "F2": 1333172, "F3": 2049144, "F4": 13056, "F5_BASE": 133899}
EXPECTED_CANONICAL = {"F1": 8344, "F2": 40839, "F3": 500079, "F4": 2862, "F5_BASE": 11718}
EXPECTED_F5_RECODINGS = 139216
EXPECTED_ASSAY_CASES = 691340
```

Represent transition targets as `tuple[int | None, ...]` indexed by `a * n + x`. Use `@dataclass(frozen=True, slots=True)` for every scientific/control record. Do not use free-form dictionaries as family payloads.

- [ ] **Step 4: Implement canonical encoding and SHA-256 helpers**

```python
def frame(tag: bytes, payload: bytes) -> bytes:
    return tag + b":" + str(len(payload)).encode("ascii") + b":" + payload
```

`canonical_encode()` domain-separates supported types, encodes dataclass fields in declared order, tuples in order, and frozensets after sorting encoded elements. Unsupported objects raise `ControlFailure(control_id="ENCODING_UNSUPPORTED", ...)`; never use `repr`, pickle, or marshal.

- [ ] **Step 5: Run GREEN**

Run: `python -m pytest tests/structure001/test_encoding.py -v`

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001 tests/structure001/test_encoding.py
git commit -m "feat: add STRUCTURE-001 typed encoding kernel"
```

---

### Task 3: Implement F1 exhaustive generation and F2 observation partitions

**Files:**
- Create: `src/revisics_structure001/families/__init__.py`
- Create: `src/revisics_structure001/families/f1.py`
- Create: `src/revisics_structure001/families/f2.py`
- Create: `src/revisics_structure001/generation.py`
- Create: `tests/structure001/test_f1.py`
- Create: `tests/structure001/test_f2.py`

**Interfaces:**
- `iter_f1(n: int, m: int) -> Iterator[F1Object]`
- `iter_partitions(n: int) -> Iterator[tuple[int, ...]]`
- `iter_f2(n: int, m: int) -> Iterator[F2Object]`
- Partition representation is a normalized restricted-growth string.

- [ ] **Step 1: Write F1 RED tests**

```python
from revisics_structure001.families.f1 import iter_f1


def test_f1_2_by_1_has_nine_tables():
    assert len(list(iter_f1(2, 1))) == 9


def test_f1_full_raw_count():
    assert sum(1 for n in range(1,4) for m in range(1,4) for _ in iter_f1(n,m)) == 267137
```

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_f1.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement F1 minimally**

```python
def iter_f1(n: int, m: int):
    alphabet = (None, *range(n))
    for targets in product(alphabet, repeat=n * m):
        yield F1Object(n=n, m=m, targets=targets)
```

Bounds outside `1 <= n,m <= 3` raise `ControlFailure("F1_BOUND", ...)`.

- [ ] **Step 4: Run F1 GREEN**

Run: `python -m pytest tests/structure001/test_f1.py -v`

Expected: PASS.

- [ ] **Step 5: Write F2 RED tests**

```python
from revisics_structure001.families.f2 import iter_partitions, iter_f2


def test_partition_counts_are_bell_1_to_3():
    assert [len(list(iter_partitions(n))) for n in (1,2,3)] == [1,2,5]


def test_f2_full_raw_count():
    assert sum(1 for n in range(1,4) for m in range(1,4) for _ in iter_f2(n,m)) == 1333172
```

- [ ] **Step 6: Run F2 RED**

Run: `python -m pytest tests/structure001/test_f2.py -v`

Expected: FAIL because F2 enumeration does not exist.

- [ ] **Step 7: Implement deterministic restricted-growth partition enumeration and F2 product**

Generate partitions directly in lexicographic restricted-growth order; do not generate arbitrary observation labels and deduplicate afterward.

- [ ] **Step 8: Run F1/F2 GREEN**

Run: `python -m pytest tests/structure001/test_f1.py tests/structure001/test_f2.py -v`

Expected: PASS.

- [ ] **Step 9: Commit**

```bash
git add src/revisics_structure001/families src/revisics_structure001/generation.py tests/structure001/test_f1.py tests/structure001/test_f2.py
git commit -m "feat: enumerate STRUCTURE-001 F1 and F2"
```

---

### Task 4: Implement exact F3 resource/regime grammar

**Files:**
- Create: `src/revisics_structure001/families/f3.py`
- Create: `tests/structure001/test_f3.py`

**Interfaces:**
- `edge_list(obj: F1Object | F3Object) -> tuple[tuple[int,int,int], ...]`
- `iter_decorations(edge_count: int) -> Iterator[tuple[tuple[int,...], tuple[int | None,...]]]`
- `iter_f3(n: int, m: int) -> Iterator[F3Object]`
- `path_is_admissible(obj: F3Object, initial_resource: int, horizon: int, edge_indices: tuple[int,...]) -> bool`
- Edge order: ascending `(a,x)` cell order. Cost tuple follows edge order. Update tuple follows `(resource,edge_index)` with resource order `0,1`, then ascending edge index; codomain enumeration order `(None,0,1)`.

- [ ] **Step 1: Write F3 RED tests**

```python
from revisics_structure001.families.f3 import iter_decorations, path_is_admissible
from revisics_structure001.model import F3Object


def test_one_edge_has_eighteen_decorations():
    assert len(list(iter_decorations(1))) == 18


def test_resource_update_can_block_second_traversal():
    obj = F3Object(n=1, m=1, targets=(0,), costs=(0,), updates=(1, None),
                   regimes=((0,1),(0,2),(1,1),(1,2)))
    assert path_is_admissible(obj, 0, 2, (0,))
    assert not path_is_admissible(obj, 0, 2, (0,0))
```

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_f3.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement exact F3 enumeration**

```python
for costs in product((0, 1), repeat=k):
    for updates in product((None, 0, 1), repeat=2 * k):
        yield F3Object(..., costs=costs, updates=updates,
                       regimes=((0,1),(0,2),(1,1),(1,2)))
```

Never filter update functions for monotonicity.

- [ ] **Step 4: Add exact raw-count test**

```python
def test_f3_full_raw_count():
    assert sum(1 for n in range(1,4) for m in range(1,4)
               if n*m <= 4 for _ in iter_f3(n,m)) == 2049144
```

- [ ] **Step 5: Run GREEN**

Run: `python -m pytest tests/structure001/test_f3.py -v`

Expected: PASS with 2,049,144 raw constructions.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/families/f3.py tests/structure001/test_f3.py
git commit -m "feat: enumerate STRUCTURE-001 F3"
```

---

### Task 5: Implement normalized F4 history-extension enumeration and validity

**Files:**
- Create: `src/revisics_structure001/families/f4.py`
- Create: `tests/structure001/test_f4.py`

**Interfaces:**
- `ExtensionKey(history: tuple[int,...], action: int, target: int)` is an immutable model record.
- `iter_f4(n: int, m: int, horizon: int) -> Iterator[F4Object]`
- `admissible_histories(obj: F4Object, t: int) -> tuple[tuple[int,...], ...]`
- `has_current_state_collision(obj: F4Object) -> bool`

- [ ] **Step 1: Write F4 RED normalization/validity tests**

```python
from revisics_structure001.families.f4 import iter_f4, has_current_state_collision


def test_forbidden_prefix_has_no_descendant_decision():
    worlds = list(iter_f4(1, 1, 2))
    blocked = next(w for w in worlds if w.decisions[0].allowed is False)
    assert len(blocked.decisions) == 1


def test_family_validity_is_current_state_collision_only():
    worlds = list(iter_f4(1, 1, 2))
    assert any(has_current_state_collision(w) for w in worlds)
    assert any(not has_current_state_collision(w) for w in worlds)
```

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_f4.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement recursive normalized enumeration**

Initial admissible histories are `(x,)` for each state. At each depth, sort executable extension keys from currently admissible histories only; enumerate every bit vector for those keys; recurse using only allowed extensions. No decision key exists below a forbidden prefix.

```python
def extend(core, horizon, depth, admissible_by_depth, decisions):
    if depth == horizon:
        yield decisions
        return
    keys = tuple(sorted(executable_extension_keys(admissible_by_depth[depth], core)))
    for bits in product((False, True), repeat=len(keys)):
        next_histories = tuple(k.extended_history for k, bit in zip(keys, bits) if bit)
        yield from extend(core, horizon, depth + 1,
                          admissible_by_depth + (next_histories,),
                          decisions + tuple(Decision(k, bit) for k, bit in zip(keys, bits)))
```

- [ ] **Step 4: Add frozen count tests**

```python
def test_f4_frozen_counts():
    assert total_normalized_specs() == 13056
    assert valid_labeled_count(2, 2, 2) == 10886
```

- [ ] **Step 5: Run GREEN**

Run: `python -m pytest tests/structure001/test_f4.py -v`

Expected: PASS with 13,056 normalized specifications and 10,886 valid labeled `(2,2,2)` cases.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/families/f4.py tests/structure001/test_f4.py
git commit -m "feat: enumerate normalized STRUCTURE-001 F4"
```

---

### Task 6: Implement F5 labeled bases and exhaustive recoding maps

**Files:**
- Create: `src/revisics_structure001/families/f5.py`
- Create: `tests/structure001/test_f5.py`

**Interfaces:**
- `iter_f5_labeled_bases(n: int, m: int) -> Iterator[F5BaseObject]`
- `iter_recoding_witnesses(n: int, m: int) -> Iterator[TransportWitness]`
- `transport_f5(base: F5BaseObject, witness: TransportWitness) -> F5BaseObject`
- `instance_id(base: F5BaseObject) -> str`
- `recoding_id(base_id: str, witness: TransportWitness) -> str`

- [ ] **Step 1: Write F5 RED tests**

```python
def test_2_by_2_has_four_recoding_maps():
    assert len(list(iter_recoding_witnesses(2, 2))) == 4


def test_f5_labeled_base_total():
    assert total_labeled_f5_bases() == 133899
```

Add a symmetric two-state base and assert two distinct witnesses produce two distinct `RecodingID`s even when transported destination bytes are equal.

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_f5.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement labeled base enumeration**

For each allowed `2 <= n,m <= 3`, `nm <= 6`, enumerate every partial transition table. If it has `k` executable edges, enumerate all `2**k` binary edge-cost assignments. Set `H=2` exactly.

- [ ] **Step 4: Implement exhaustive recoding transport without deduplication**

Witness order is lexicographic permutations of states crossed with lexicographic permutations of actions; identity is included. `RecodingID` hashes canonical encoding of `(BaseID, phi_x, phi_a)`, never destination bytes alone.

- [ ] **Step 5: Run GREEN**

Run: `python -m pytest tests/structure001/test_f5.py -v`

Expected: PASS with 133,899 labeled bases.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/families/f5.py tests/structure001/test_f5.py
git commit -m "feat: enumerate STRUCTURE-001 F5 bases and recodings"
```

---

### Task 7: Implement exhaustive family-aware canonicalization and deterministic witness ties

**Files:**
- Create: `src/revisics_structure001/canonical.py`
- Create: `tests/structure001/test_canonical.py`
- Modify: all five `src/revisics_structure001/families/f*.py` modules to expose typed `transport()`.

**Interfaces:**
- `all_witnesses(n: int, m: int) -> Iterator[TransportWitness]`
- `canonicalize(obj: FamilyObject) -> CanonicalizedObject`
- Each family exports `transport(obj, witness) -> same family type`.

- [ ] **Step 1: Write RED invariance/idempotence tests**

```python
def test_f1_relabeling_canonicalizes_identically():
    left = F1Object(n=2, m=1, targets=(1, 0))
    right = transport_f1(left, TransportWitness((1,0), (0,)))
    assert canonicalize(left).canonical_bytes == canonicalize(right).canonical_bytes


def test_canonicalization_is_idempotent():
    first = canonicalize(sample_f3())
    second = canonicalize(first.payload)
    assert first.canonical_bytes == second.canonical_bytes
```

- [ ] **Step 2: Write RED automorphism tie-break test**

```python
def test_automorphism_tie_uses_minimum_transport_bytes():
    obj = symmetric_f1_object()
    result = canonicalize(obj)
    minimizers = [(canonical_encode(transport_f1(obj, w)), canonical_encode(w), w)
                  for w in all_witnesses(obj.n, obj.m)]
    minimum_object = min(row[0] for row in minimizers)
    expected_witness = min(row for row in minimizers if row[0] == minimum_object,
                           key=lambda row: row[1])[2]
    assert result.witness == expected_witness
```

- [ ] **Step 3: Run RED**

Run: `python -m pytest tests/structure001/test_canonical.py -v`

Expected: FAIL.

- [ ] **Step 4: Implement exhaustive total-order canonicalizer**

For every typed state/action witness, transport the full family object, encode object and witness, then choose the bytewise minimum pair `(object_bytes, transport_bytes)`. F3 resource labels remain fixed. F4 transports all state/action occurrences in histories and decision keys. F5 canonicalizes bases before recoding expansion only.

- [ ] **Step 5: Add exact canonical-count controls**

```text
F1            8,344
F2           40,839
F3          500,079
F4            2,862 valid canonical total
F4 (2,2,2)    2,784 valid canonical
F5 base       11,718
```

Use canonical byte strings as set keys in the control code; never infer scientific identity from Python object hash values.

- [ ] **Step 6: Run GREEN family/canonical suite**

Run: `python -m pytest tests/structure001/test_f1.py tests/structure001/test_f2.py tests/structure001/test_f3.py tests/structure001/test_f4.py tests/structure001/test_f5.py tests/structure001/test_canonical.py -v`

Expected: PASS with every frozen canonical count.

- [ ] **Step 7: Commit**

```bash
git add src/revisics_structure001/canonical.py src/revisics_structure001/families tests/structure001/test_canonical.py
git commit -m "feat: add exhaustive STRUCTURE-001 canonicalization"
```

---

### Task 8: Implement rule-derived validation and typed negative controls

**Files:**
- Create: `src/revisics_structure001/validation.py`
- Create: `tests/structure001/test_validation.py`

**Interfaces:**
- `validate(obj: FamilyObject) -> ValidityRecord`
- `validate_f5_recoding(base: F5BaseObject, witness: TransportWitness, destination: F5BaseObject) -> ValidityRecord`

- [ ] **Step 1: Write RED negative controls**

Construct explicit malformed immutable fixtures and assert reason codes:

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

For every fixture, compare `canonical_encode(obj)` before and after validation and assert byte equality.

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_validation.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement validators**

`ValidityRecord` contains `valid: bool`, `reason_code: str`, and `observed: str`. Dispatch by explicit family type. Invalidity never returns a repaired payload.

- [ ] **Step 4: Run GREEN**

Run: `python -m pytest tests/structure001/test_validation.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/revisics_structure001/validation.py tests/structure001/test_validation.py
git commit -m "feat: validate STRUCTURE-001 family contracts"
```

---

### Task 9: Implement provenance graph, canonical framed ledgers, and dedicated `L_P`

**Files:**
- Create: `src/revisics_structure001/provenance.py`
- Create: `tests/structure001/test_provenance.py`

**Interfaces:**
- `write_canonical_ledger(path: Path, records: Iterable[bytes]) -> None`
- `read_framed_records(path: Path) -> tuple[bytes, ...]`
- `raw_to_canonical_edge(...) -> ProvenanceEdge`
- `canonical_to_assay_edge(...) -> ProvenanceEdge`

- [ ] **Step 1: Write RED ledger/provenance tests**

```python
def test_provenance_ledger_roundtrip(tmp_path):
    records = [canonical_encode(edge_b), canonical_encode(edge_a)]
    write_canonical_ledger(tmp_path / "L_P.bin", records)
    assert read_framed_records(tmp_path / "L_P.bin") == tuple(sorted(records))
```

Create a canonical world with two raw sources; assert exactly two raw-to-canonical `ProvenanceEdge`s survive in `L_P`.

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_provenance.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement canonical framed ledgers and edges**

Ledger record framing is `ASCII decimal byte length + b":" + payload`. Sort records by full canonical bytes before writing. Every edge binds manifest SHA, implementation identity, family, source ID, destination ID, edge kind, and canonical transport bytes when applicable. F5 additionally binds `BaseID`, `InstanceID`, `RecodingID`, `phi_x`, `phi_a`, and identity-recoding flag.

- [ ] **Step 4: Run GREEN**

Run: `python -m pytest tests/structure001/test_provenance.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/revisics_structure001/provenance.py tests/structure001/test_provenance.py
git commit -m "feat: add STRUCTURE-001 provenance ledger"
```

---

### Task 10: Implement deterministic ledger roots and `AuditBundle`

**Files:**
- Create: `src/revisics_structure001/audit.py`
- Create: `tests/structure001/test_audit.py`

**Interfaces:**
- `merkle_root(records: Iterable[bytes], ledger_tag: str) -> str`
- `build_audit_manifest(...) -> AuditManifest`
- `audit_bundle_digest(manifest: AuditManifest) -> str`

- [ ] **Step 1: Write RED order/provenance-binding tests**

Feed the same records in opposite orders and assert equal ledger roots. Then alter one provenance edge only and assert the `L_P` root and top-level `AuditBundle` both change.

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_audit.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement domain-separated binary Merkle roots**

```python
leaf = sha256(b"structure001-leaf-v1\0" + ledger_tag.encode() + b"\0" + record).digest()
node = sha256(b"structure001-node-v1\0" + left + right).digest()
```

Sort canonical records first. Duplicate the final node on odd levels. Empty root is `sha256(b"structure001-empty-v1\0" + ledger_tag.encode()).hexdigest()`.

- [ ] **Step 4: Bind every required root**

`AuditManifest` fields are exactly manifest SHA, implementation identity, `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, and typed counts. The bundle digest is `sha256(canonical_encode(AuditManifest)).hexdigest()`.

- [ ] **Step 5: Run GREEN**

Run: `python -m pytest tests/structure001/test_audit.py -v`

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/audit.py tests/structure001/test_audit.py
git commit -m "feat: bind STRUCTURE-001 audit bundle"
```

---

### Task 11: Build quarantined control-run orchestration and deterministic replay

**Files:**
- Create: `src/revisics_structure001/replay.py`
- Create: `src/revisics_structure001/__main__.py`
- Create: `tests/structure001/test_replay.py`

**Interfaces:**
- `require_custody(path: Path) -> PreImplementationCustodyRecord`
- `run_control(output_dir: Path, implementation_id: str, limits: TestLimits | None = None) -> ControlRunResult`
- `compare_control_runs(a: Path, b: Path) -> None`
- CLI: `python -m revisics_structure001 control-run --output PATH --implementation-id SHA`
- CLI: `python -m revisics_structure001 compare-control-runs PATH_A PATH_B`
- `primary-universe-run` exists only as a guard and returns nonzero unless a separately valid implementation-lock record is supplied. This plan never invokes it.

- [ ] **Step 1: Write RED custody/quarantine tests**

Assert control run refuses missing custody, any nonzero custody field, or a nonempty output directory. Assert `primary-universe-run` fails without an implementation-lock record.

- [ ] **Step 2: Write RED tiny-domain replay test**

Use `TestLimits` only in tests to run a small F1/F2 subset twice; assert record-level equality and identical audit digest. Mutate one provenance record and assert `ControlFailure` with `control_id == "I4_REPLAY_MISMATCH"`.

`TestLimits` must live under a test-only module or require an explicit `test_mode=True`; production `control-run` CLI must reject any bound override.

- [ ] **Step 3: Run RED**

Run: `python -m pytest tests/structure001/test_replay.py -v`

Expected: FAIL.

- [ ] **Step 4: Implement control pipeline**

Fixed family order is `F1,F2,F3,F4,F5`: generate raw records -> validate -> canonicalize valid primary objects -> write raw/canonical/validity/provenance records; then F5 expands every recoding witness without deduplication. Emit `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, typed counts, roots, and `AuditBundle`. No candidate import or applicability check occurs.

- [ ] **Step 5: Implement record-level replay comparison**

Byte-compare every framed stream for `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, then typed counts, each ledger root, and `AuditBundle`. First mismatch reports ledger and record index.

- [ ] **Step 6: Run GREEN**

Run: `python -m pytest tests/structure001/test_replay.py -v`

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add src/revisics_structure001/replay.py src/revisics_structure001/__main__.py tests/structure001/test_replay.py
git commit -m "feat: add quarantined STRUCTURE-001 replay"
```

---

### Task 12: Reproduce every frozen construction/count control before full replay

**Files:**
- Create: `tests/structure001/test_full_counts.py`
- Modify: `src/revisics_structure001/generation.py`

**Interfaces:**
- `compute_reference_counts() -> TypedCountRecord`, independent of ledger file I/O.

- [ ] **Step 1: Write RED full frozen count assertion**

```python
def test_all_frozen_reference_counts():
    counts = compute_reference_counts()
    assert counts.f1_raw == 267137
    assert counts.f1_canonical == 8344
    assert counts.f2_raw == 1333172
    assert counts.f2_canonical == 40839
    assert counts.f3_raw == 2049144
    assert counts.f3_canonical == 500079
    assert counts.f4_normalized == 13056
    assert counts.f4_valid_labeled_222 == 10886
    assert counts.f4_canonical == 2862
    assert counts.f4_canonical_222 == 2784
    assert counts.f5_labeled_bases == 133899
    assert counts.f5_canonical_bases == 11718
    assert counts.f5_recodings == 139216
    assert counts.assay_cases == 691340
```

- [ ] **Step 2: Run RED before wiring aggregate count function**

Run: `python -m pytest tests/structure001/test_full_counts.py -v`

Expected: FAIL because `compute_reference_counts` does not yet exist.

- [ ] **Step 3: Implement aggregate count function only by calling frozen family/canonical machinery**

Do not insert closed-form constants as returned observed counts. Constants are acceptance expectations only.

- [ ] **Step 4: Run GREEN full count control**

Run: `python -m pytest tests/structure001/test_full_counts.py -v`

Expected: PASS. A mismatch is blocking; never edit expected numbers to green the test.

- [ ] **Step 5: Run complete suite**

Run: `python -m pytest tests/structure001 -v`

Expected: all tests PASS.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/generation.py tests/structure001/test_full_counts.py
git commit -m "test: reproduce STRUCTURE-001 frozen counts"
```

---

### Task 13: Execute two complete quarantined control runs and prepare I0-I4 evidence

**Files:**
- Generate, outside Git history: `.structure001-control/control-run-a/`
- Generate, outside Git history: `.structure001-control/control-run-b/`
- Create: `experiments/STRUCTURE-001/implementation-controls/IMPLEMENTATION_ACCEPTANCE_V1.md`
- Create: `experiments/STRUCTURE-001/implementation-controls/CONTROL_ARTIFACT_INDEX_V1.txt`

**Interfaces:**
- Consumes: exact implementation code commit after Task 12.
- Produces: retained full control ledgers plus a committed index/acceptance candidate. It does **not** create `IMPLEMENTATION_LOCK`.

- [ ] **Step 1: Add `.structure001-control/` to `.git/info/exclude`, not repository `.gitignore`**

This prevents accidental Git addition without altering project semantics or repository-wide ignore policy.

- [ ] **Step 2: Record exact implementation identity**

Run: `git rev-parse HEAD`

Save that exact SHA as `IMPLEMENTATION_ID`; both complete control runs must use this same code identity.

- [ ] **Step 3: Run control A**

```bash
python -m revisics_structure001 control-run \
  --output .structure001-control/control-run-a \
  --implementation-id "$IMPLEMENTATION_ID"
```

Expected: exit 0 with Task 12 counts.

- [ ] **Step 4: Run control B**

```bash
python -m revisics_structure001 control-run \
  --output .structure001-control/control-run-b \
  --implementation-id "$IMPLEMENTATION_ID"
```

Expected: exit 0.

- [ ] **Step 5: Compare runs record-by-record and by bundle**

```bash
python -m revisics_structure001 compare-control-runs \
  .structure001-control/control-run-a \
  .structure001-control/control-run-b
```

Expected: exit 0 with equality of typed counts, `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, ledger roots, and `AuditBundle`.

- [ ] **Step 6: Create durable-control artifact index**

For every file in both retained control-run directories, record repository-relative control path, byte size, and SHA-256 in `CONTROL_ARTIFACT_INDEX_V1.txt`, sorted by path. The full ledgers remain retained at the indexed locations; the index is not a substitute for them.

If the execution environment cannot guarantee retention of both full run directories through independent review, record `CONTROL_ARTIFACT_RETENTION_FAILURE` and STOP. Do not claim I4 or implementation lock from roots alone.

- [ ] **Step 7: Write the acceptance candidate from observed evidence only**

`IMPLEMENTATION_ACCEPTANCE_V1.md` contains exact manifest SHA, implementation SHA, custody-record SHA-256, artifact-index SHA-256, each I0-I4 PASS/FAIL with evidence, all frozen counts, both `AuditBundle` digests, provenance roots, `primary_universe_run = NOT_EXECUTED`, `candidate_evaluation = NOT_EXECUTED`, and the implementation-fidelity-only claim ceiling. Do not write PASS before its command succeeds.

- [ ] **Step 8: Fresh final verification**

```bash
python -m pytest tests/structure001 -v
python -m revisics_structure001 compare-control-runs \
  .structure001-control/control-run-a \
  .structure001-control/control-run-b
```

Expected: test suite PASS and replay comparison exit 0.

- [ ] **Step 9: Commit only the acceptance/index records, never the full control ledgers by accident**

```bash
git add experiments/STRUCTURE-001/implementation-controls/IMPLEMENTATION_ACCEPTANCE_V1.md \
        experiments/STRUCTURE-001/implementation-controls/CONTROL_ARTIFACT_INDEX_V1.txt
git commit -m "control: record STRUCTURE-001 I0-I4 evidence index"
```

Stop for independent review. Do not create or claim `IMPLEMENTATION_LOCK`, do not invoke `primary-universe-run`, and do not evaluate candidates. If the reviewer requires a different durable location for the full ledgers, move/copy them without changing their bytes, update the artifact index prospectively as control metadata, and reverify the copied SHA-256 values before lock authorization.

---

## Plan Self-Review / Execution Gate

Before Task 1, verify:

```text
scientific contract             9711a6d unchanged
candidate ontology              7d1e3cf unchanged
construction manifest           f587406 unchanged
design                           535013c reviewed
primary universe                 not generated
candidate outcomes               none
```

Before claiming Task 13 complete, verify every design acceptance dimension maps to evidence:

```text
I0 custody                       custody record + locked blob hashes
I1 generation fidelity           raw/normalized family counts
I2 canonicalization fidelity     canonical counts + invariance/idempotence/tie tests
I3 validation/provenance         negative controls + complete L_P + content-ID reproduction
I4 deterministic replay          record equality + ledger roots + AuditBundle equality
```

Claim ceiling:

```text
Successful I0-I4 acceptance demonstrates only that the reference software faithfully realizes the frozen STRUCTURE-001 V1 construction contract. It is not a scientific result of STRUCTURE-001.
```
