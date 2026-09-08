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
- No candidate ID, candidate outcome, candidate score, or candidate implementation may enter generation, canonicalization, validity, provenance, or replay logic.
- Every implementation mismatch with the manifest is `CONTROL_FAILURE -> STOP`; no best-effort, auto-repair, fallback sampling, or semantic patching.
- `CONTROL_RUN` outputs are quarantined implementation-control evidence only. `PRIMARY_UNIVERSE_RUN` must remain blocked until a separately recorded implementation lock exists.
- Do not implement candidate evaluation or the later F4 target-sensitive sufficiency test in this plan.
- Commit after each task only after the listed test command passes.

## File Map

- `pyproject.toml` — Python/package/test configuration only.
- `experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt` — retained I0/S2 zero-state record created before generator code.
- `src/revisics_structure001/constants.py` — frozen SHAs, encoding version, family bounds, expected counts.
- `src/revisics_structure001/model.py` — immutable family and ledger record types.
- `src/revisics_structure001/encoding.py` — canonical field framing and typed record encoding.
- `src/revisics_structure001/identity.py` — SHA-256 identities only.
- `src/revisics_structure001/families/f1.py` ... `f5.py` — family-native enumeration and transport operations.
- `src/revisics_structure001/generation.py` — family dispatch only.
- `src/revisics_structure001/canonical.py` — exhaustive typed relabeling and canonical representative selection.
- `src/revisics_structure001/validation.py` — typed validity checks; never repair.
- `src/revisics_structure001/provenance.py` — provenance edges and deterministic ledger emission.
- `src/revisics_structure001/audit.py` — ledger roots and `AuditBundle`.
- `src/revisics_structure001/replay.py` — run classes, quarantine, record-level replay comparison.
- `src/revisics_structure001/__main__.py` — control CLI; primary-run command guarded by implementation-lock record.
- `tests/structure001/` — custody, encoding, each family, canonicalization, validation, provenance, audit, replay, and full-count controls.

---

### Task 1: Establish I0 custody before any generator exists

**Files:**
- Create: `pyproject.toml`
- Create: `experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt`
- Create: `tests/structure001/test_custody.py`

**Interfaces:**
- Produces: a fixed line-oriented `PreImplementationCustodyRecord` consumed later by `replay.require_custody()`.
- Depends on: the three frozen scientific artifact identities only.

- [ ] **Step 1: Write the custody record before creating `src/` implementation code**

Use this exact field order and values:

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

- [ ] **Step 2: Add minimal pytest project configuration**

```toml
[build-system]
requires = ["setuptools>=70"]
build-backend = "setuptools.build_meta"

[project]
name = "revisics-structure001"
version = "0.0.0"
requires-python = ">=3.12"
dependencies = []

[project.optional-dependencies]
test = ["pytest>=8"]

[tool.pytest.ini_options]
testpaths = ["tests"]
pythonpath = ["src"]
```

- [ ] **Step 3: Write the failing custody/hash test**

```python
from hashlib import sha256
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

LOCKED = {
    "experiments/STRUCTURE-001/PREREGISTRATION_V1.md": "1200d1388082441ef0bfc68e52c8a14c94027458",
    "experiments/STRUCTURE-001/CANDIDATE_SPECIFICATION_MANIFEST_V1.md": "5ee1d18642ab8f7025d2db157207c8069303a050",
    "experiments/STRUCTURE-001/SYSTEM_CONSTRUCTION_MANIFEST_V1.md": "502d37b98c16086fe013bdca4c166122ed1e637e",
}


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

Also verify the scientific files are byte-identical by comparing their Git blob SHA using a local helper that computes Git's blob hash (`sha1(b"blob <len>\\0" + data)`), not plain SHA-256.

- [ ] **Step 4: Run the custody test**

Run: `python -m pytest tests/structure001/test_custody.py -v`

Expected: PASS. If any locked artifact hash differs or any zero assertion is missing, STOP.

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
- Produces: `ControlFailure`, immutable `F1Object`-`F5BaseObject`, `TransportWitness`, ledger record dataclasses, `canonical_encode(value) -> bytes`, `sha256_hex(data: bytes) -> str`.
- Consumes: frozen constants and custody file from Task 1.

- [ ] **Step 1: Write failing tests for immutable records and encoding**

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

- [ ] **Step 2: Run and confirm RED**

Run: `python -m pytest tests/structure001/test_encoding.py -v`

Expected: FAIL because package/types do not exist.

- [ ] **Step 3: Implement constants and immutable records**

`constants.py` must include at least:

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

Use frozen dataclasses; represent transition targets as `tuple[int | None, ...]` indexed by `a * n + x`. Define family payload types explicitly; do not use free-form dictionaries.

- [ ] **Step 4: Implement canonical encoding and SHA-256 helpers**

The encoder must domain-separate every type and length-frame every field. Use one helper:

```python
def frame(tag: bytes, payload: bytes) -> bytes:
    return tag + b":" + str(len(payload)).encode("ascii") + b":" + payload
```

`canonical_encode()` must encode dataclasses in declared field order, tuples in order, and frozensets after sorting encoded elements. It must reject unsupported objects with `ControlFailure(control_id="ENCODING_UNSUPPORTED", ...)` rather than falling back to `repr()`.

- [ ] **Step 5: Run encoding tests**

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
- Produces: `iter_f1(n, m) -> Iterator[F1Object]`, `iter_partitions(n) -> Iterator[tuple[int, ...]]`, `iter_f2(n, m) -> Iterator[F2Object]`, `iter_raw(family) -> Iterator[FamilyObject]`.
- Partition representation is a restricted-growth string normalized so first block label is `0` and each next label is at most `1 + max(previous)`.

- [ ] **Step 1: Write F1 local and count tests**

```python
from revisics_structure001.families.f1 import iter_f1


def test_f1_2_by_1_has_nine_tables():
    assert len(list(iter_f1(2, 1))) == 9


def test_f1_full_raw_count():
    assert sum(1 for n in range(1, 4) for m in range(1, 4) for _ in iter_f1(n, m)) == 267137
```

- [ ] **Step 2: Run F1 test RED**

Run: `python -m pytest tests/structure001/test_f1.py -v`

Expected: FAIL because `iter_f1` does not exist.

- [ ] **Step 3: Implement F1 with `itertools.product`**

```python
def iter_f1(n: int, m: int):
    alphabet = (None, *range(n))
    for targets in product(alphabet, repeat=n * m):
        yield F1Object(n=n, m=m, targets=targets)
```

Reject bounds outside `1 <= n,m <= 3` with `ControlFailure("F1_BOUND", ...)`.

- [ ] **Step 4: Run F1 tests GREEN**

Run: `python -m pytest tests/structure001/test_f1.py -v`

Expected: PASS with raw total 267137.

- [ ] **Step 5: Write F2 partition and count tests**

```python
from revisics_structure001.families.f2 import iter_partitions, iter_f2


def test_partition_counts_are_bell_1_to_3():
    assert [len(list(iter_partitions(n))) for n in (1, 2, 3)] == [1, 2, 5]


def test_f2_full_raw_count():
    assert sum(1 for n in range(1, 4) for m in range(1, 4) for _ in iter_f2(n, m)) == 1333172
```

- [ ] **Step 6: Implement deterministic restricted-growth partition enumeration**

Generate strings recursively in lexicographic order; do not generate arbitrary observation labels and deduplicate afterward.

- [ ] **Step 7: Run F1/F2 tests**

Run: `python -m pytest tests/structure001/test_f1.py tests/structure001/test_f2.py -v`

Expected: PASS.

- [ ] **Step 8: Commit**

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
- Produces: `edge_list(obj)`, `iter_f3(n, m)`, `path_is_admissible(obj, initial_resource, horizon, edge_indices)`.
- Edge order is fixed as ascending `(a, x)` cell order; target is supplied by the deterministic table. Cost tuples follow that edge order. Update tuples follow `(resource, edge_index)` with resource order `(0,1)` then ascending edge index; codomain enumeration order is `(None, 0, 1)`.

- [ ] **Step 1: Write small grammar tests**

```python
from revisics_structure001.families.f3 import iter_decorations


def test_one_edge_has_18_f3_decorations():
    decorations = list(iter_decorations(edge_count=1))
    assert len(decorations) == 2 * 3**2
```

Add a path test where `u(0,e)=1`, `u(1,e)=None`: one traversal from resource 0 is admissible and the second traversal is blocked.

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_f3.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement exact F3 enumeration**

For each valid `(n,m)` with `nm <= 4`, enumerate each F1 table, then:

```python
for costs in product((0, 1), repeat=k):
    for updates in product((None, 0, 1), repeat=2 * k):
        yield F3Object(..., costs=costs, updates=updates, regimes=((0,1),(0,2),(1,1),(1,2)))
```

Do not filter `updates` for monotonicity.

- [ ] **Step 4: Add full symbolic/raw count control**

```python
def test_f3_full_raw_count():
    assert sum(1 for n in range(1,4) for m in range(1,4) if n*m <= 4 for _ in iter_f3(n,m)) == 2049144
```

- [ ] **Step 5: Run F3 tests GREEN**

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
- Produces: `iter_f4(n,m,horizon)`, `admissible_histories(obj, t)`, `has_current_state_collision(obj) -> bool`.
- A history is represented as `(x0, a0, x1, ..., x_t)`; only currently admissible prefixes create next-step decision keys.

- [ ] **Step 1: Write a normalization test proving forbidden prefixes create no descendant bits**

Construct a one-state/one-action core at `H=2`; compare the serialized decision set for a world whose first extension is forbidden. Assert there is exactly one decision bit, not a second inert descendant bit.

- [ ] **Step 2: Write validity tests**

Create one F4 object with two distinct same-time admissible histories ending at the same state and assert `has_current_state_collision()` is true. Create one without such a pair and assert false.

- [ ] **Step 3: Run RED**

Run: `python -m pytest tests/structure001/test_f4.py -v`

Expected: FAIL.

- [ ] **Step 4: Implement recursive normalized enumeration**

Use this recursion shape:

```python
def extend(core, horizon, depth, admissible_by_depth, decisions):
    if depth == horizon:
        yield decisions
        return
    keys = sorted(executable_extension_keys(admissible_by_depth[depth], core))
    for bits in product((0, 1), repeat=len(keys)):
        next_histories = tuple(key.extended_history for key, bit in zip(keys, bits) if bit)
        yield from extend(core, horizon, depth + 1,
                          admissible_by_depth + (next_histories,),
                          decisions + tuple(zip(keys, bits)))
```

Initial admissible histories are all `(x,)` for `x in range(n)`. Decision keys must never be created below a prefix that failed an earlier alpha bit.

- [ ] **Step 5: Add frozen count controls**

Assert:

```python
assert total_normalized_specs() == 13056
assert valid_labeled_count(2,2,2) == 10886
```

Canonical counts are deferred until the shared canonicalizer exists.

- [ ] **Step 6: Run F4 tests GREEN**

Run: `python -m pytest tests/structure001/test_f4.py -v`

Expected: PASS with normalized total 13,056 and largest-cell valid labeled count 10,886.

- [ ] **Step 7: Commit**

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
- Produces: `iter_f5_labeled_bases(n,m)`, `iter_recoding_witnesses(n,m)`, `transport_f5(base,witness)`, `instance_id()`, `recoding_id()`.
- Recoding witnesses are the Cartesian product of all state permutations and action permutations, both in lexicographic permutation order; identity is included.

- [ ] **Step 1: Write base-count and permutation tests**

```python
def test_2_by_2_has_four_recoding_maps():
    assert len(list(iter_recoding_witnesses(2,2))) == 4


def test_f5_labeled_base_total():
    assert total_labeled_f5_bases() == 133899
```

- [ ] **Step 2: Write an automorphism-preservation test**

Use a symmetric two-state base and verify two distinct permutation witnesses remain distinct records even if transported destination bytes coincide.

- [ ] **Step 3: Run RED**

Run: `python -m pytest tests/structure001/test_f5.py -v`

Expected: FAIL.

- [ ] **Step 4: Implement labeled base enumeration**

For each allowed `2 <= n,m <= 3`, `nm <= 6`, enumerate every partial transition table. Let `k` be executable edges; enumerate `2**k` binary edge-cost assignments. Set `H=2` exactly.

- [ ] **Step 5: Implement recoding transport without post-expansion deduplication**

Transport transitions and edge-cost ownership under `(phi_x, phi_a)` exactly. `RecodingID` hashes canonical encoding of `(BaseID, phi_x, phi_a)`; it must not hash destination bytes alone.

- [ ] **Step 6: Run F5 tests GREEN**

Run: `python -m pytest tests/structure001/test_f5.py -v`

Expected: PASS with 133,899 labeled bases.

- [ ] **Step 7: Commit**

```bash
git add src/revisics_structure001/families/f5.py tests/structure001/test_f5.py
git commit -m "feat: enumerate STRUCTURE-001 F5 bases and recodings"
```

---

### Task 7: Implement exhaustive family-aware canonicalization and deterministic witness ties

**Files:**
- Create: `src/revisics_structure001/canonical.py`
- Create: `tests/structure001/test_canonical.py`
- Modify: `src/revisics_structure001/families/f1.py`
- Modify: `src/revisics_structure001/families/f2.py`
- Modify: `src/revisics_structure001/families/f3.py`
- Modify: `src/revisics_structure001/families/f4.py`
- Modify: `src/revisics_structure001/families/f5.py`

**Interfaces:**
- Each family module produces `transport(obj, witness) -> same family type`.
- `canonicalize(obj) -> CanonicalizedObject` returns canonical bytes, `WorldID`/`BaseID`, canonical payload, and unique `TransportWitness`.

- [ ] **Step 1: Write RED tests for relabeling invariance and idempotence**

```python
def test_f1_relabeling_canonicalizes_identically():
    left = F1Object(n=2, m=1, targets=(1, 0))
    right = transport_f1(left, TransportWitness((1,0),(0,)))
    assert canonicalize(left).canonical_bytes == canonicalize(right).canonical_bytes


def test_canonicalization_is_idempotent():
    first = canonicalize(sample_f3())
    second = canonicalize(first.payload)
    assert first.canonical_bytes == second.canonical_bytes
```

- [ ] **Step 2: Write the automorphism tie-break regression**

For an object with two transport witnesses yielding identical minimum object bytes, calculate both transport encodings and assert the chosen witness is the bytewise minimum, regardless of enumeration input order.

- [ ] **Step 3: Run RED**

Run: `python -m pytest tests/structure001/test_canonical.py -v`

Expected: FAIL.

- [ ] **Step 4: Implement exhaustive canonicalizer**

```python
def canonicalize(obj):
    candidates = []
    for witness in all_witnesses(obj.n, obj.m):
        transported = family_transport(obj, witness)
        object_bytes = canonical_encode(transported)
        transport_bytes = canonical_encode(witness)
        candidates.append((object_bytes, transport_bytes, transported, witness))
    object_bytes, _, payload, witness = min(candidates, key=lambda row: (row[0], row[1]))
    return CanonicalizedObject(payload, object_bytes, sha256_hex(object_bytes), witness)
```

F3 never relabels resources. F2 transports partition membership. F4 transports every state/action occurrence in histories and extension keys. F5 uses this only for bases before recoding expansion.

- [ ] **Step 5: Add full canonical count controls**

Assert exact totals:

```text
F1       8,344
F2      40,839
F3     500,079
F4       2,862 valid canonical total
F4(2,2,2) 2,784 valid canonical
F5 base 11,718
```

For count tests, maintain a `set[bytes]` of canonical bytes; do not use Python object hash as scientific identity.

- [ ] **Step 6: Run canonical/full family suite**

Run: `python -m pytest tests/structure001/test_f1.py tests/structure001/test_f2.py tests/structure001/test_f3.py tests/structure001/test_f4.py tests/structure001/test_f5.py tests/structure001/test_canonical.py -v`

Expected: PASS with all frozen canonical totals.

- [ ] **Step 7: Commit**

```bash
git add src/revisics_structure001/canonical.py src/revisics_structure001/families tests/structure001
git commit -m "feat: add exhaustive STRUCTURE-001 canonicalization"
```

---

### Task 8: Implement rule-derived validation and typed control failures

**Files:**
- Create: `src/revisics_structure001/validation.py`
- Create: `tests/structure001/test_validation.py`

**Interfaces:**
- Produces: `validate(obj) -> ValidityRecord`, `validate_f5_recoding(base,witness,destination) -> ValidityRecord`.
- Invalid records are returned with exact reason codes; no function returns a repaired object.

- [ ] **Step 1: Write negative-control tests**

Cover at least these exact invalid cases:

```text
F1_TARGET_OUT_OF_RANGE
F2_PARTITION_NOT_NORMALIZED_OR_INVALID
F3_COST_OUT_OF_RANGE
F3_UPDATE_OUT_OF_CODOMAIN
F3_REGIME_BUNDLE_MISMATCH
F4_EXTENSION_KEY_INCONSISTENT
F4_NO_CURRENT_STATE_COLLISION
F5_EXEC_TRANSPORT_MISMATCH
F5_COST_TRANSPORT_MISMATCH
```

Assert the input object bytes before and after `validate()` are identical.

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_validation.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement validators**

Each validator returns `ValidityRecord(valid: bool, reason_code: str, observed: str)` and never mutates input. `validate()` dispatches by explicit family type, not class-name strings or candidate metadata.

- [ ] **Step 4: Run validation tests GREEN**

Run: `python -m pytest tests/structure001/test_validation.py -v`

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/revisics_structure001/validation.py tests/structure001/test_validation.py
git commit -m "feat: validate STRUCTURE-001 family contracts"
```

---

### Task 9: Implement provenance graph, framed ledgers, and dedicated `L_P`

**Files:**
- Create: `src/revisics_structure001/provenance.py`
- Create: `tests/structure001/test_provenance.py`

**Interfaces:**
- Produces: `ProvenanceEdge`, `append_framed_record(path, bytes)`, `read_framed_records(path)`, and deterministic edge constructors for raw -> canonical -> assay relationships.
- Ledger framing is `ASCII decimal byte length + b":" + payload`; records are emitted only after sorting by canonical record bytes.

- [ ] **Step 1: Write framed-ledger roundtrip and provenance coverage tests**

```python
def test_provenance_ledger_roundtrip(tmp_path):
    records = [canonical_encode(edge_b), canonical_encode(edge_a)]
    write_canonical_ledger(tmp_path / "L_P.bin", records)
    assert read_framed_records(tmp_path / "L_P.bin") == sorted(records)
```

Add a test that a canonical world with two raw sources yields two distinct provenance edges and both are present in `L_P`.

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_provenance.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement append-only-in-run provenance**

Every edge includes manifest SHA, implementation identity, family, source ID, destination ID, edge kind, and canonical transport bytes where applicable. F5 edges additionally bind `BaseID`, `InstanceID`, `RecodingID`, `phi_x`, `phi_a`, and identity-recoding flag.

- [ ] **Step 4: Run provenance tests GREEN**

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
- Produces: `merkle_root(records: Iterable[bytes], ledger_tag: str) -> str`, `build_audit_manifest(...) -> AuditManifest`, `audit_bundle_digest(manifest) -> str`.

- [ ] **Step 1: Write RED tests proving order normalization and provenance binding**

Create two identical record sets in different input orders and assert equal roots after canonical sorting. Change one `ProvenanceEdge` only and assert both `L_P` root and top-level `AuditBundle` change.

- [ ] **Step 2: Run RED**

Run: `python -m pytest tests/structure001/test_audit.py -v`

Expected: FAIL.

- [ ] **Step 3: Implement domain-separated binary Merkle roots**

Use:

```python
leaf = sha256(b"structure001-leaf-v1\0" + ledger_tag.encode() + b"\0" + record).digest()
node = sha256(b"structure001-node-v1\0" + left + right).digest()
```

Sort canonical records first. For an odd level, duplicate the final node. For an empty ledger, hash `b"structure001-empty-v1\0" + ledger_tag.encode()`.

- [ ] **Step 4: Bind every required root into the top-level bundle**

`AuditManifest` fields must be exactly: manifest SHA, implementation identity, `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, and typed counts. Hash only `canonical_encode(AuditManifest)`.

- [ ] **Step 5: Run audit tests GREEN**

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
- Produces: `require_custody(path)`, `run_control(output_dir, implementation_id) -> ControlRunResult`, `compare_control_runs(a,b)`, CLI `python -m revisics_structure001 control-run --output <dir> --implementation-id <id>`.
- A `primary-universe-run` subcommand exists only as a guard and must fail unless a separate implementation-lock record path is supplied and validates; this plan never invokes it.

- [ ] **Step 1: Write RED custody and quarantine tests**

Assert `run_control()` refuses to start if custody record is missing or any zero field is nonzero. Assert it refuses a nonempty output directory. Assert `primary-universe-run` exits nonzero when no implementation-lock record exists.

- [ ] **Step 2: Write a tiny replay equality test**

Use a test-only subset configuration to run the same small F1/F2 domain twice and assert record-level equality and identical audit digest. Mutate only one provenance edge and assert `compare_control_runs()` raises `ControlFailure("I4_REPLAY_MISMATCH", ...)`.

- [ ] **Step 3: Run RED**

Run: `python -m pytest tests/structure001/test_replay.py -v`

Expected: FAIL.

- [ ] **Step 4: Implement control-run pipeline**

Within one run, for each family in fixed order `F1,F2,F3,F4,F5`:

```text
generate raw records
validate raw/family record
canonicalize valid primary objects
retain raw -> canonical provenance
for F5: freeze canonical bases in-memory for the run, then expand every recoding witness without deduplication
emit sorted L_R, L_C, L_V, L_P, L_F5
emit typed counts
compute ledger roots and AuditBundle
```

No candidate imports or applicability checks occur.

- [ ] **Step 5: Implement record-level replay comparison**

Comparison must byte-compare every framed record stream for `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, compare typed counts, compare each ledger root, then compare `AuditBundle`. Stop at first mismatch but report ledger and record index.

- [ ] **Step 6: Run replay tests GREEN**

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
- Produces: `compute_reference_counts() -> TypedCountRecord` independent of ledger file I/O.

- [ ] **Step 1: Write the full frozen count assertion**

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

- [ ] **Step 2: Run the full count control**

Run: `python -m pytest tests/structure001/test_full_counts.py -v`

Expected: PASS. Any mismatch is a blocking control failure; do not modify expected numbers to make the test green.

- [ ] **Step 3: Run the complete unit/control suite**

Run: `python -m pytest tests/structure001 -v`

Expected: all tests PASS.

- [ ] **Step 4: Commit**

```bash
git add src/revisics_structure001/generation.py tests/structure001/test_full_counts.py
git commit -m "test: reproduce STRUCTURE-001 frozen counts"
```

---

### Task 13: Execute two complete quarantined control runs and produce the I0-I4 acceptance record

**Files:**
- Generated control evidence only under: `experiments/STRUCTURE-001/implementation-controls/control-run-a/`
- Generated control evidence only under: `experiments/STRUCTURE-001/implementation-controls/control-run-b/`
- Create: `experiments/STRUCTURE-001/implementation-controls/IMPLEMENTATION_ACCEPTANCE_V1.md`

**Interfaces:**
- Consumes: exact implementation commit identity after Task 12.
- Produces: retained control ledgers and an acceptance record. It does **not** produce `IMPLEMENTATION_LOCK` itself unless the user separately authorizes fossilization after review.

- [ ] **Step 1: Record exact implementation identity**

Run:

```bash
git rev-parse HEAD
```

Save that exact SHA as `IMPLEMENTATION_ID`; do not run control A and B on different code commits.

- [ ] **Step 2: Run control A from a clean directory**

```bash
python -m revisics_structure001 control-run \
  --output experiments/STRUCTURE-001/implementation-controls/control-run-a \
  --implementation-id "$IMPLEMENTATION_ID"
```

Expected: exit 0 and typed counts exactly matching Task 12.

- [ ] **Step 3: Run control B from a second clean directory**

```bash
python -m revisics_structure001 control-run \
  --output experiments/STRUCTURE-001/implementation-controls/control-run-b \
  --implementation-id "$IMPLEMENTATION_ID"
```

Expected: exit 0.

- [ ] **Step 4: Compare runs record-by-record and by bundle**

```bash
python -m revisics_structure001 compare-control-runs \
  experiments/STRUCTURE-001/implementation-controls/control-run-a \
  experiments/STRUCTURE-001/implementation-controls/control-run-b
```

Expected: exit 0 with equality for typed counts, `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, all ledger roots, and `AuditBundle`.

- [ ] **Step 5: Write the acceptance record from observed evidence only**

`IMPLEMENTATION_ACCEPTANCE_V1.md` must contain:

```text
manifest_sha
implementation_sha
custody_record_sha256
I0 = PASS/FAIL + evidence paths
I1 = PASS/FAIL + exact counts
I2 = PASS/FAIL + exact canonical counts + tie-break test reference
I3 = PASS/FAIL + provenance-root evidence
I4 = PASS/FAIL + both AuditBundle digests + record-comparison result
claim_ceiling = implementation fidelity only; no scientific result
primary_universe_run = NOT_EXECUTED
candidate_evaluation = NOT_EXECUTED
```

Do not write PASS before the corresponding command has succeeded.

- [ ] **Step 6: Run final verification against the acceptance record**

Run:

```bash
python -m pytest tests/structure001 -v
python -m revisics_structure001 compare-control-runs \
  experiments/STRUCTURE-001/implementation-controls/control-run-a \
  experiments/STRUCTURE-001/implementation-controls/control-run-b
```

Expected: test suite PASS and replay comparison exit 0.

- [ ] **Step 7: Commit control evidence and acceptance candidate**

```bash
git add experiments/STRUCTURE-001/implementation-controls
git commit -m "control: record STRUCTURE-001 I0-I4 evidence"
```

Stop here for review. Do **not** create or claim `IMPLEMENTATION_LOCK`, do not invoke `primary-universe-run`, and do not evaluate candidates until the acceptance evidence is independently reviewed and the user explicitly authorizes the implementation lock.

---

## Plan self-check before execution

The executor must confirm before Task 1:

```text
scientific contract             9711a6d unchanged
candidate ontology              7d1e3cf unchanged
construction manifest           f587406 unchanged
design                           535013c reviewed
primary universe                 not generated
candidate outcomes               none
```

The implementation claim ceiling remains:

```text
A successful I0-I4 acceptance demonstrates only that the reference software faithfully realizes the frozen STRUCTURE-001 V1 construction contract. It is not a scientific result of STRUCTURE-001.
```
