# STRUCTURE-001 Reference Implementation Plan V2

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Every implementation task uses RED → minimal implementation → GREEN → commit.

**Goal:** Build the transparent Python 3.12 reference implementation that mechanically realizes `SYSTEM_CONSTRUCTION_MANIFEST_V1.md @ f5874063b06997f49f3ee80d291de879c8d27a7f`, then demonstrate I0–I4 with two quarantined complete control runs without generating the primary frozen universe.

**Architecture:** A standard-library-only `src/revisics_structure001/` package holds immutable typed family records, one canonical encoder, SHA-256 identities, exhaustive F1–F5 generators, exhaustive state/action relabeling, deterministic transport tie-breaking, rule-derived validation, canonical provenance ledgers, deterministic ledger roots, and replay orchestration. The manifest is semantic authority. Any code/manifest mismatch is `CONTROL_FAILURE -> STOP`.

**Tech Stack:** Python 3.12; Python standard library at runtime; pytest as the only test dependency.

**Spec:** `docs/superpowers/specs/2026-09-08-structure-001-reference-implementation-design.md @ 535013cf4ce97234c1777a3ae1d7884c0578b455`

## Global Constraints

- Scientific contract: `9711a6dd1b14ade10fd43a03c424ddc840cc565e`.
- Candidate ontology lock: `7d1e3cf3bd61b212d6131a7e1d98c10f401aa95d`.
- System-construction authority: `f5874063b06997f49f3ee80d291de879c8d27a7f`.
- Scientific changes permitted: NONE.
- Runtime semantic output may not depend on network access, model calls, randomness, wall clock, locale, process scheduling, filesystem enumeration order, or Python hash randomization.
- Candidate IDs, candidate outcomes, candidate scores, candidate applicability, and candidate implementations are forbidden inputs to generation, canonicalization, validation, provenance, and replay.
- No best-effort mode, semantic repair, skip-invalid mode, fallback sampler, or post-lock bound override.
- `CONTROL_RUN` output is implementation-control evidence only. `PRIMARY_UNIVERSE_RUN` remains blocked until a separately reviewed and explicitly authorized implementation lock exists.
- Task 1 is a custody gate that must occur before implementation source exists. TDD begins at Task 2.
- Exact expected counts are acceptance values, never substitute observed values returned by implementation code.

## Exact File Map

```text
pyproject.toml
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
    families/
        __init__.py
        f1.py
        f2.py
        f3.py
        f4.py
        f5.py
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
    test_full_counts.py
```

---

## Task 1: Record I0/S2 custody before implementation code

**Files:**
- Create: `pyproject.toml`
- Create: `experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt`
- Create: `tests/structure001/test_custody.py`

**Produces:** retained preimplementation custody evidence only. No `src/` file is created in this task.

- [ ] **Step 1: Create the zero-state custody record with exact field order**

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

- [ ] **Step 2: Add local pytest configuration**

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

- [ ] **Step 3: Add frozen-blob and four-zero assertions**

```python
from hashlib import sha1
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

LOCKED_BLOBS = {
    "experiments/STRUCTURE-001/PREREGISTRATION_V1.md":
        "1200d1388082441ef0bfc68e52c8a14c94027458",
    "experiments/STRUCTURE-001/CANDIDATE_SPECIFICATION_MANIFEST_V1.md":
        "5ee1d18642ab8f7025d2db157207c8069303a050",
    "experiments/STRUCTURE-001/SYSTEM_CONSTRUCTION_MANIFEST_V1.md":
        "502d37b98c16086fe013bdca4c166122ed1e637e",
}


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode("ascii")
    return sha1(header + data).hexdigest()


def test_locked_scientific_blobs_are_byte_identical():
    for relative, expected in LOCKED_BLOBS.items():
        assert git_blob_sha(ROOT / relative) == expected


def test_preimplementation_record_asserts_all_four_zero_states():
    path = ROOT / "experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt"
    lines = path.read_text(encoding="utf-8").splitlines()
    assert "raw_constructions_generated=0" in lines
    assert "canonical_worlds_generated=0" in lines
    assert "f5_recoding_cases_generated=0" in lines
    assert "candidate_case_outcomes_observed=0" in lines
```

- [ ] **Step 4: Verify custody**

Run:

```bash
python -m pytest tests/structure001/test_custody.py -v
```

Expected: PASS. Any failure means STOP before Task 2.

- [ ] **Step 5: Commit the custody gate**

```bash
git add pyproject.toml \
  experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt \
  tests/structure001/test_custody.py
git commit -m "control: record STRUCTURE-001 preimplementation custody"
```

---

## Task 2: Define immutable types, control failures, canonical encoding, and IDs

**Files:**
- Create: `src/revisics_structure001/__init__.py`
- Create: `src/revisics_structure001/constants.py`
- Create: `src/revisics_structure001/model.py`
- Create: `src/revisics_structure001/encoding.py`
- Create: `src/revisics_structure001/identity.py`
- Create: `tests/structure001/test_encoding.py`

**Produces exact interfaces:**

```python
class ControlFailure(RuntimeError):
    control_id: str
    family: str | None
    record_id: str | None
    expected: str
    observed: str

@dataclass(frozen=True, slots=True)
class TransportWitness:
    phi_x: tuple[int, ...]
    phi_a: tuple[int, ...]

@dataclass(frozen=True, slots=True)
class F1Object:
    n: int
    m: int
    targets: tuple[int | None, ...]

@dataclass(frozen=True, slots=True)
class F2Object:
    n: int
    m: int
    targets: tuple[int | None, ...]
    partition: tuple[int, ...]

@dataclass(frozen=True, slots=True)
class F3Object:
    n: int
    m: int
    targets: tuple[int | None, ...]
    costs: tuple[int, ...]
    updates: tuple[int | None, ...]
    regimes: tuple[tuple[int, int], ...]

@dataclass(frozen=True, slots=True)
class ExtensionKey:
    history: tuple[int, ...]
    action: int
    target: int

@dataclass(frozen=True, slots=True)
class HistoryDecision:
    key: ExtensionKey
    allowed: bool

@dataclass(frozen=True, slots=True)
class F4Object:
    n: int
    m: int
    targets: tuple[int | None, ...]
    horizon: int
    decisions: tuple[HistoryDecision, ...]

@dataclass(frozen=True, slots=True)
class F5BaseObject:
    n: int
    m: int
    targets: tuple[int | None, ...]
    costs: tuple[int, ...]
    horizon: int
```

Also define `PreImplementationCustodyRecord`, `CanonicalizedObject`, `ValidityRecord`, `RawConstructionRecord`, `CanonicalWorldRecord`, `ProvenanceEdge`, `F5RecodingRecord`, `TypedCountRecord`, `AuditManifest`, and `ControlRunResult` as frozen slotted dataclasses.

`ProvenanceEdge` fields are fixed as:

```python
manifest_sha: str
implementation_id: str
family: str
source_id: str
destination_id: str
edge_kind: str
transport: TransportWitness | None
base_id: str | None
instance_id: str | None
recoding_id: str | None
identity_recoding: bool | None
```

- [ ] **Step 1: Write RED immutability and encoding tests**

```python
from dataclasses import FrozenInstanceError
import pytest

from revisics_structure001.encoding import canonical_encode
from revisics_structure001.model import F1Object, TransportWitness


def test_f1_object_is_immutable():
    obj = F1Object(n=1, m=1, targets=(None,))
    with pytest.raises(FrozenInstanceError):
        obj.n = 2


def test_frozenset_encoding_is_order_independent():
    assert canonical_encode(frozenset({3, 1, 2})) == canonical_encode(frozenset({2, 3, 1}))


def test_transport_encoding_uses_explicit_image_sequences():
    left = TransportWitness(phi_x=(1, 0), phi_a=(0,))
    right = TransportWitness(phi_x=(1, 0), phi_a=(0,))
    assert canonical_encode(left) == canonical_encode(right)
```

- [ ] **Step 2: Run RED**

```bash
python -m pytest tests/structure001/test_encoding.py -v
```

Expected: FAIL because the package does not yet exist.

- [ ] **Step 3: Implement frozen constants**

```python
MANIFEST_COMMIT_SHA = "f5874063b06997f49f3ee80d291de879c8d27a7f"
MANIFEST_BLOB_SHA = "502d37b98c16086fe013bdca4c166122ed1e637e"
PARENT_CONTRACT_SHA = "9711a6dd1b14ade10fd43a03c424ddc840cc565e"
CANDIDATE_LOCK_SHA = "7d1e3cf3bd61b212d6131a7e1d98c10f401aa95d"
ENCODING_VERSION = "structure001-canonical-v1"
EXPECTED_F1_RAW = 267137
EXPECTED_F2_RAW = 1333172
EXPECTED_F3_RAW = 2049144
EXPECTED_F4_NORMALIZED = 13056
EXPECTED_F5_LABELED_BASES = 133899
EXPECTED_F1_CANONICAL = 8344
EXPECTED_F2_CANONICAL = 40839
EXPECTED_F3_CANONICAL = 500079
EXPECTED_F4_CANONICAL = 2862
EXPECTED_F4_222_VALID_LABELED = 10886
EXPECTED_F4_222_CANONICAL = 2784
EXPECTED_F5_CANONICAL_BASES = 11718
EXPECTED_F5_RECODINGS = 139216
EXPECTED_ASSAY_CASES = 691340
```

- [ ] **Step 4: Implement canonical encoding**

Use one framing primitive:

```python
def frame(tag: bytes, payload: bytes) -> bytes:
    return tag + b":" + str(len(payload)).encode("ascii") + b":" + payload
```

`canonical_encode(value)` must support `None`, bool, int, str, bytes, tuple, frozenset, and frozen dataclasses. Dataclass encoding includes fully qualified type tag plus fields in dataclass declaration order. Frozenset elements are encoded independently and sorted by encoded bytes. Unsupported values raise `ControlFailure` with `control_id="ENCODING_UNSUPPORTED"`. Never use `repr`, pickle, or marshal.

- [ ] **Step 5: Implement identity helpers**

```python
from hashlib import sha256


def sha256_hex(data: bytes) -> str:
    return sha256(data).hexdigest()


def content_id(value: object) -> str:
    return sha256_hex(canonical_encode(value))
```

- [ ] **Step 6: Run GREEN**

```bash
python -m pytest tests/structure001/test_encoding.py -v
```

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add src/revisics_structure001 tests/structure001/test_encoding.py
git commit -m "feat: add STRUCTURE-001 typed encoding kernel"
```

---

## Task 3: Implement F1 and F2 exhaustive generation

**Files:**
- Create: `src/revisics_structure001/families/__init__.py`
- Create: `src/revisics_structure001/families/f1.py`
- Create: `src/revisics_structure001/families/f2.py`
- Create: `src/revisics_structure001/generation.py`
- Create: `tests/structure001/test_f1.py`
- Create: `tests/structure001/test_f2.py`

**Interfaces:**

```python
iter_f1(n: int, m: int) -> Iterator[F1Object]
iter_partitions(n: int) -> Iterator[tuple[int, ...]]
normalize_partition(labels: tuple[int, ...]) -> tuple[int, ...]
iter_f2(n: int, m: int) -> Iterator[F2Object]
```

Partition representation is a restricted-growth string. `normalize_partition` relabels blocks by first occurrence in ascending state-label order.

- [ ] **Step 1: Write F1 RED tests**

```python
from revisics_structure001.families.f1 import iter_f1


def test_f1_two_states_one_action_has_nine_tables():
    assert len(list(iter_f1(2, 1))) == 9


def test_f1_full_raw_total():
    total = sum(1 for n in range(1, 4) for m in range(1, 4) for _ in iter_f1(n, m))
    assert total == 267137
```

- [ ] **Step 2: Run F1 RED**

```bash
python -m pytest tests/structure001/test_f1.py -v
```

Expected: FAIL.

- [ ] **Step 3: Implement F1**

```python
from itertools import product


def iter_f1(n: int, m: int):
    if not (1 <= n <= 3 and 1 <= m <= 3):
        raise ControlFailure(
            control_id="F1_BOUND",
            family="F1",
            record_id=None,
            expected="1 <= n,m <= 3",
            observed=f"n={n},m={m}",
        )
    alphabet = (None,) + tuple(range(n))
    for targets in product(alphabet, repeat=n * m):
        yield F1Object(n=n, m=m, targets=targets)
```

- [ ] **Step 4: Run F1 GREEN**

```bash
python -m pytest tests/structure001/test_f1.py -v
```

Expected: PASS.

- [ ] **Step 5: Write F2 RED tests**

```python
from revisics_structure001.families.f2 import iter_f2, iter_partitions


def test_partition_counts_are_bell_numbers_one_to_three():
    assert [len(list(iter_partitions(n))) for n in (1, 2, 3)] == [1, 2, 5]


def test_f2_full_raw_total():
    total = sum(1 for n in range(1, 4) for m in range(1, 4) for _ in iter_f2(n, m))
    assert total == 1333172
```

- [ ] **Step 6: Run F2 RED**

```bash
python -m pytest tests/structure001/test_f2.py -v
```

Expected: FAIL.

- [ ] **Step 7: Implement restricted-growth partitions exactly**

```python
def iter_partitions(n: int):
    if n < 1:
        raise ControlFailure("F2_PARTITION_BOUND", "F2", None, "n >= 1", f"n={n}")

    def rec(prefix: tuple[int, ...]):
        if len(prefix) == n:
            yield prefix
            return
        maximum = max(prefix)
        for label in range(maximum + 2):
            yield from rec(prefix + (label,))

    yield from rec((0,))
```

`iter_f2` is the direct Cartesian product of each F1 table and every partition returned by `iter_partitions(n)`.

- [ ] **Step 8: Run F1/F2 GREEN**

```bash
python -m pytest tests/structure001/test_f1.py tests/structure001/test_f2.py -v
```

Expected: PASS.

- [ ] **Step 9: Commit**

```bash
git add src/revisics_structure001/families src/revisics_structure001/generation.py \
  tests/structure001/test_f1.py tests/structure001/test_f2.py
git commit -m "feat: enumerate STRUCTURE-001 F1 and F2"
```

---

## Task 4: Implement exact F3 resource/regime grammar

**Files:**
- Create: `src/revisics_structure001/families/f3.py`
- Create: `tests/structure001/test_f3.py`

**Interfaces:**

```python
edge_list(n: int, m: int, targets: tuple[int | None, ...]) -> tuple[tuple[int,int,int], ...]
iter_decorations(edge_count: int) -> Iterator[tuple[tuple[int, ...], tuple[int | None, ...]]]
iter_f3(n: int, m: int) -> Iterator[F3Object]
path_is_admissible(obj: F3Object, initial_resource: int, horizon: int, edge_indices: tuple[int, ...]) -> bool
```

Edge order is ascending transition-table cell index `a*n+x`; each edge tuple is `(x,a,target)`. Cost tuple follows edge order. Update tuple index is `resource*k + edge_index`, with resource order `(0,1)` and update codomain order `(None,0,1)`.

- [ ] **Step 1: Write F3 RED tests**

```python
from revisics_structure001.families.f3 import iter_decorations, path_is_admissible
from revisics_structure001.model import F3Object


def test_one_edge_has_eighteen_decorations():
    assert len(list(iter_decorations(1))) == 18


def test_resource_update_can_block_second_traversal():
    obj = F3Object(
        n=1,
        m=1,
        targets=(0,),
        costs=(0,),
        updates=(1, None),
        regimes=((0, 1), (0, 2), (1, 1), (1, 2)),
    )
    assert path_is_admissible(obj, 0, 2, (0,))
    assert not path_is_admissible(obj, 0, 2, (0, 0))
```

- [ ] **Step 2: Run RED**

```bash
python -m pytest tests/structure001/test_f3.py -v
```

Expected: FAIL.

- [ ] **Step 3: Implement F3 decoration enumeration**

```python
from itertools import product


def iter_decorations(edge_count: int):
    for costs in product((0, 1), repeat=edge_count):
        for updates in product((None, 0, 1), repeat=2 * edge_count):
            yield costs, updates
```

For each F1 base with allowed `1 <= n,m <= 3` and `n*m <= 4`, compute `k=len(edge_list(...))` and emit:

```python
yield F3Object(
    n=n,
    m=m,
    targets=base.targets,
    costs=costs,
    updates=updates,
    regimes=((0, 1), (0, 2), (1, 1), (1, 2)),
)
```

No update function is filtered for monotonicity.

- [ ] **Step 4: Add exact full raw-count control**

```python
def test_f3_full_raw_total():
    total = sum(
        1
        for n in range(1, 4)
        for m in range(1, 4)
        if n * m <= 4
        for _ in iter_f3(n, m)
    )
    assert total == 2049144
```

- [ ] **Step 5: Run GREEN**

```bash
python -m pytest tests/structure001/test_f3.py -v
```

Expected: PASS with 2,049,144 raw constructions.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/families/f3.py tests/structure001/test_f3.py
git commit -m "feat: enumerate STRUCTURE-001 F3"
```

---

## Task 5: Implement normalized F4 history-extension enumeration and family validity

**Files:**
- Create: `src/revisics_structure001/families/f4.py`
- Create: `tests/structure001/test_f4.py`

**Interfaces:**

```python
iter_f4(n: int, m: int, horizon: int) -> Iterator[F4Object]
admissible_histories(obj: F4Object, t: int) -> tuple[tuple[int, ...], ...]
has_current_state_collision(obj: F4Object) -> bool
executable_extension_keys(histories: tuple[tuple[int, ...], ...], n: int, m: int, targets: tuple[int | None, ...]) -> tuple[ExtensionKey, ...]
```

A history tuple alternates state/action/state. For example `(0,1,2,0,1)` means `x0=0,a0=1,x1=2,a1=0,x2=1`.

- [ ] **Step 1: Write F4 RED normalization and validity tests**

```python
from revisics_structure001.families.f4 import has_current_state_collision, iter_f4


def test_forbidden_prefix_generates_no_descendant_decision():
    worlds = list(iter_f4(1, 1, 2))
    blocked = next(w for w in worlds if w.decisions[0].allowed is False)
    assert len(blocked.decisions) == 1


def test_f4_family_validity_is_collision_not_future_difference():
    worlds = list(iter_f4(1, 1, 2))
    assert any(has_current_state_collision(w) for w in worlds)
    assert any(not has_current_state_collision(w) for w in worlds)
```

- [ ] **Step 2: Run RED**

```bash
python -m pytest tests/structure001/test_f4.py -v
```

Expected: FAIL.

- [ ] **Step 3: Implement normalized recursive decision enumeration**

```python
def extend(core, horizon, depth, histories_by_depth, decisions):
    if depth == horizon:
        yield decisions
        return
    keys = executable_extension_keys(
        histories_by_depth[depth], core.n, core.m, core.targets
    )
    for bits in product((False, True), repeat=len(keys)):
        next_histories = tuple(
            key.history + (key.action, key.target)
            for key, bit in zip(keys, bits)
            if bit
        )
        next_decisions = decisions + tuple(
            HistoryDecision(key=key, allowed=bit)
            for key, bit in zip(keys, bits)
        )
        yield from extend(
            core,
            horizon,
            depth + 1,
            histories_by_depth + (next_histories,),
            next_decisions,
        )
```

Initial histories are `tuple((x,) for x in range(n))`. `executable_extension_keys` sorts by `(history, action, target)` and is called only on currently admissible histories, so no decision exists below a forbidden prefix.

- [ ] **Step 4: Add frozen count controls**

```python
def test_f4_frozen_normalized_and_largest_cell_counts():
    assert total_normalized_specs() == 13056
    assert valid_labeled_count(2, 2, 2) == 10886
```

- [ ] **Step 5: Run GREEN**

```bash
python -m pytest tests/structure001/test_f4.py -v
```

Expected: PASS with 13,056 normalized specifications and 10,886 valid labeled `(2,2,2)` cases.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/families/f4.py tests/structure001/test_f4.py
git commit -m "feat: enumerate normalized STRUCTURE-001 F4"
```

---

## Task 6: Implement F5 labeled bases and exhaustive recoding maps

**Files:**
- Create: `src/revisics_structure001/families/f5.py`
- Create: `tests/structure001/test_f5.py`

**Interfaces:**

```python
iter_f5_labeled_bases(n: int, m: int) -> Iterator[F5BaseObject]
iter_recoding_witnesses(n: int, m: int) -> Iterator[TransportWitness]
transport_f5(base: F5BaseObject, witness: TransportWitness) -> F5BaseObject
instance_id(base: F5BaseObject) -> str
recoding_id(base_id: str, witness: TransportWitness) -> str
```

- [ ] **Step 1: Write F5 RED tests**

```python
from revisics_structure001.encoding import canonical_encode
from revisics_structure001.families.f5 import (
    iter_recoding_witnesses,
    recoding_id,
    transport_f5,
)
from revisics_structure001.identity import content_id
from revisics_structure001.model import F5BaseObject, TransportWitness


def test_two_by_two_has_four_recoding_witnesses():
    assert len(list(iter_recoding_witnesses(2, 2))) == 4


def test_distinct_maps_remain_distinct_when_destination_bytes_match():
    base = F5BaseObject(
        n=2,
        m=2,
        targets=(0, 1, 0, 1),
        costs=(0, 0, 0, 0),
        horizon=2,
    )
    identity = TransportWitness((0, 1), (0, 1))
    swap_states = TransportWitness((1, 0), (0, 1))
    assert canonical_encode(transport_f5(base, identity)) == canonical_encode(transport_f5(base, swap_states))
    base_id = content_id(base)
    assert recoding_id(base_id, identity) != recoding_id(base_id, swap_states)
```

Also add `assert total_labeled_f5_bases() == 133899`.

- [ ] **Step 2: Run RED**

```bash
python -m pytest tests/structure001/test_f5.py -v
```

Expected: FAIL.

- [ ] **Step 3: Implement labeled base enumeration**

For every allowed `2 <= n,m <= 3` and `n*m <= 6`, enumerate every partial transition table. If the table has `k` executable edges, enumerate all `2**k` cost tuples in edge order. Every emitted base has `horizon=2`.

- [ ] **Step 4: Implement exhaustive witness enumeration and exact transport**

Witness order is `itertools.permutations(range(n))` crossed with `itertools.permutations(range(m))`, both native lexicographic order. A transport maps old state `x` to `phi_x[x]`, old action `a` to `phi_a[a]`, and old target `y` to `phi_x[y]`. Rebuild edge costs in the new edge order. Never deduplicate witnesses after transport.

`RecodingID` is:

```python
sha256_hex(canonical_encode((base_id, witness.phi_x, witness.phi_a)))
```

- [ ] **Step 5: Run GREEN**

```bash
python -m pytest tests/structure001/test_f5.py -v
```

Expected: PASS with 133,899 labeled bases.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/families/f5.py tests/structure001/test_f5.py
git commit -m "feat: enumerate STRUCTURE-001 F5 bases and recodings"
```

---

## Task 7: Implement exhaustive family-aware canonicalization and deterministic witness ties

**Files:**
- Create: `src/revisics_structure001/canonical.py`
- Create: `tests/structure001/test_canonical.py`
- Modify: `src/revisics_structure001/families/f1.py`
- Modify: `src/revisics_structure001/families/f2.py`
- Modify: `src/revisics_structure001/families/f3.py`
- Modify: `src/revisics_structure001/families/f4.py`
- Modify: `src/revisics_structure001/families/f5.py`

**Interfaces:**

```python
all_witnesses(n: int, m: int) -> Iterator[TransportWitness]
transport_f1(obj: F1Object, witness: TransportWitness) -> F1Object
transport_f2(obj: F2Object, witness: TransportWitness) -> F2Object
transport_f3(obj: F3Object, witness: TransportWitness) -> F3Object
transport_f4(obj: F4Object, witness: TransportWitness) -> F4Object
transport_f5(obj: F5BaseObject, witness: TransportWitness) -> F5BaseObject
canonicalize(obj: F1Object | F2Object | F3Object | F4Object | F5BaseObject) -> CanonicalizedObject
```

- [ ] **Step 1: Write RED relabeling and idempotence tests**

```python
from revisics_structure001.canonical import canonicalize
from revisics_structure001.families.f1 import transport_f1
from revisics_structure001.model import F1Object, F3Object, TransportWitness


def test_relabeling_canonicalizes_to_same_bytes():
    left = F1Object(n=2, m=1, targets=(1, 0))
    right = transport_f1(left, TransportWitness((1, 0), (0,)))
    assert canonicalize(left).canonical_bytes == canonicalize(right).canonical_bytes


def test_canonicalization_is_idempotent():
    sample = F3Object(
        n=1,
        m=1,
        targets=(0,),
        costs=(1,),
        updates=(0, 1),
        regimes=((0, 1), (0, 2), (1, 1), (1, 2)),
    )
    first = canonicalize(sample)
    second = canonicalize(first.payload)
    assert first.canonical_bytes == second.canonical_bytes
```

- [ ] **Step 2: Write RED automorphism tie test with an explicit symmetric object**

```python
from revisics_structure001.canonical import all_witnesses
from revisics_structure001.encoding import canonical_encode


def test_automorphism_tie_uses_minimum_transport_bytes():
    obj = F1Object(n=2, m=1, targets=(0, 1))
    rows = []
    for witness in all_witnesses(obj.n, obj.m):
        rows.append((
            canonical_encode(transport_f1(obj, witness)),
            canonical_encode(witness),
            witness,
        ))
    minimum_object = min(row[0] for row in rows)
    expected = min(
        (row for row in rows if row[0] == minimum_object),
        key=lambda row: row[1],
    )[2]
    assert canonicalize(obj).witness == expected
```

- [ ] **Step 3: Run RED**

```bash
python -m pytest tests/structure001/test_canonical.py -v
```

Expected: FAIL.

- [ ] **Step 4: Implement all family transports**

For F2, after state permutation, rebuild partition labels in new state order and call `normalize_partition`. For F3 and F5, map each old edge to its transported edge, then rebuild cost/update tuples in the transported object's edge order. F3 resource labels `0,1` are fixed and never permuted. For F4, map every state at even history positions, every action at odd positions, decision action, and decision target; then sort transported decisions by `(history, action, target)`.

- [ ] **Step 5: Implement canonical total order**

For every witness:

```python
transported = family_transport(obj, witness)
object_bytes = canonical_encode(transported)
transport_bytes = canonical_encode(witness)
```

Select the bytewise minimum `(object_bytes, transport_bytes)` pair. Return `CanonicalizedObject(payload=transported, canonical_bytes=object_bytes, canonical_id=sha256_hex(object_bytes), witness=witness)`. Do not select the first encountered minimum object.

- [ ] **Step 6: Add exact canonical-count tests**

Assert:

```text
F1 canonical total            8344
F2 canonical total           40839
F3 canonical total          500079
F4 valid canonical total      2862
F4 (2,2,2) canonical          2784
F5 canonical bases           11718
```

Use `set[bytes]` of canonical bytes for these controls.

- [ ] **Step 7: Run GREEN family/canonical suite**

```bash
python -m pytest \
  tests/structure001/test_f1.py \
  tests/structure001/test_f2.py \
  tests/structure001/test_f3.py \
  tests/structure001/test_f4.py \
  tests/structure001/test_f5.py \
  tests/structure001/test_canonical.py -v
```

Expected: PASS with every frozen canonical count.

- [ ] **Step 8: Commit**

```bash
git add src/revisics_structure001/canonical.py src/revisics_structure001/families \
  tests/structure001/test_canonical.py
git commit -m "feat: add exhaustive STRUCTURE-001 canonicalization"
```

---

## Task 8: Implement rule-derived validation and negative controls

**Files:**
- Create: `src/revisics_structure001/validation.py`
- Create: `tests/structure001/test_validation.py`

**Interfaces:**

```python
validate(obj: F1Object | F2Object | F3Object | F4Object | F5BaseObject) -> ValidityRecord
validate_f5_recoding(base: F5BaseObject, witness: TransportWitness, destination: F5BaseObject) -> ValidityRecord
```

`ValidityRecord` fields are `family`, `record_id`, `valid`, `reason_code`, `expected`, and `observed`.

- [ ] **Step 1: Write RED malformed-fixture tests**

Use these exact fixtures and reason codes:

```python
invalid_f1 = F1Object(n=1, m=1, targets=(2,))
invalid_f2 = F2Object(n=2, m=1, targets=(None, None), partition=(0, 2))
invalid_f3_cost = F3Object(1, 1, (0,), (2,), (0, 0), ((0,1),(0,2),(1,1),(1,2)))
invalid_f3_update = F3Object(1, 1, (0,), (0,), (7, 0), ((0,1),(0,2),(1,1),(1,2)))
invalid_f3_regimes = F3Object(1, 1, (0,), (0,), (0, 0), ((0,1),(1,1)))
```

Expected reason codes:

```text
F1_TARGET_OUT_OF_RANGE
F2_PARTITION_INVALID
F3_COST_OUT_OF_RANGE
F3_UPDATE_OUT_OF_CODOMAIN
F3_REGIME_BUNDLE_MISMATCH
```

For F4, create a decision whose history does not terminate at the source state implied by the raw edge and expect `F4_EXTENSION_KEY_INCONSISTENT`; create a syntactically consistent no-collision object and expect `F4_NO_CURRENT_STATE_COLLISION`. For F5, transport a valid base, alter one destination transition and expect `F5_EXEC_TRANSPORT_MISMATCH`; restore execution, alter one transported cost and expect `F5_COST_TRANSPORT_MISMATCH`.

For every validation call, assert `canonical_encode(input)` is identical before and after validation.

- [ ] **Step 2: Run RED**

```bash
python -m pytest tests/structure001/test_validation.py -v
```

Expected: FAIL.

- [ ] **Step 3: Implement validators without repair**

Dispatch by explicit family type. Return `ValidityRecord` only; never mutate or return a corrected object. F4 validity includes the current-state collision condition. F5 recoding validity separately checks exact execution transport and cost transport.

- [ ] **Step 4: Run GREEN**

```bash
python -m pytest tests/structure001/test_validation.py -v
```

Expected: PASS.

- [ ] **Step 5: Commit**

```bash
git add src/revisics_structure001/validation.py tests/structure001/test_validation.py
git commit -m "feat: validate STRUCTURE-001 family contracts"
```

---

## Task 9: Implement canonical ledgers and dedicated provenance graph `L_P`

**Files:**
- Create: `src/revisics_structure001/provenance.py`
- Create: `tests/structure001/test_provenance.py`

**Interfaces:**

```python
write_canonical_ledger(path: Path, records: Iterable[bytes]) -> None
read_framed_records(path: Path) -> tuple[bytes, ...]
raw_to_canonical_edge(
    manifest_sha: str,
    implementation_id: str,
    family: str,
    raw_id: str,
    canonical_id: str,
    witness: TransportWitness,
) -> ProvenanceEdge
canonical_to_assay_edge(
    manifest_sha: str,
    implementation_id: str,
    family: str,
    canonical_id: str,
    assay_id: str,
) -> ProvenanceEdge
f5_recoding_edge(
    manifest_sha: str,
    implementation_id: str,
    base_id: str,
    instance_id: str,
    recoding_id_value: str,
    witness: TransportWitness,
    identity_recoding: bool,
) -> ProvenanceEdge
```

- [ ] **Step 1: Write RED framed-ledger and provenance tests**

```python
from pathlib import Path

from revisics_structure001.encoding import canonical_encode
from revisics_structure001.model import ProvenanceEdge, TransportWitness
from revisics_structure001.provenance import read_framed_records, write_canonical_ledger


def make_edge(source: str, destination: str) -> ProvenanceEdge:
    return ProvenanceEdge(
        manifest_sha="m",
        implementation_id="i",
        family="F1",
        source_id=source,
        destination_id=destination,
        edge_kind="RAW_TO_CANONICAL",
        transport=TransportWitness((0,), (0,)),
        base_id=None,
        instance_id=None,
        recoding_id=None,
        identity_recoding=None,
    )


def test_provenance_ledger_roundtrip_sorts_records(tmp_path: Path):
    records = [canonical_encode(make_edge("b", "c")), canonical_encode(make_edge("a", "c"))]
    path = tmp_path / "L_P.bin"
    write_canonical_ledger(path, records)
    assert read_framed_records(path) == tuple(sorted(records))


def test_two_raw_sources_remain_two_edges(tmp_path: Path):
    records = [canonical_encode(make_edge("raw-a", "canon")), canonical_encode(make_edge("raw-b", "canon"))]
    path = tmp_path / "L_P.bin"
    write_canonical_ledger(path, records)
    assert len(read_framed_records(path)) == 2
```

- [ ] **Step 2: Run RED**

```bash
python -m pytest tests/structure001/test_provenance.py -v
```

Expected: FAIL.

- [ ] **Step 3: Implement framed canonical ledgers**

Each record is written as `ASCII decimal payload length + b":" + payload`. Sort full canonical record bytes before emission. Reader parses length prefix and returns exact payload bytes. Malformed framing raises `ControlFailure(control_id="LEDGER_FRAMING", ...)`.

- [ ] **Step 4: Implement exact provenance edge constructors**

All edges bind manifest SHA and implementation identity. `raw_to_canonical_edge` stores the unique canonicalization witness. `f5_recoding_edge` stores BaseID, InstanceID, RecodingID, witness, and identity-recoding flag. Every provenance edge destined for a control run must be written to `L_P`; it may not exist only in memory.

- [ ] **Step 5: Run GREEN**

```bash
python -m pytest tests/structure001/test_provenance.py -v
```

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/provenance.py tests/structure001/test_provenance.py
git commit -m "feat: add STRUCTURE-001 provenance ledger"
```

---

## Task 10: Implement deterministic ledger roots and `AuditBundle`

**Files:**
- Create: `src/revisics_structure001/audit.py`
- Create: `tests/structure001/test_audit.py`

**Interfaces:**

```python
merkle_root(records: Iterable[bytes], ledger_tag: str) -> str
build_audit_manifest(
    manifest_sha: str,
    implementation_id: str,
    raw_root: str,
    canonical_root: str,
    validity_root: str,
    provenance_root: str,
    f5_root: str,
    counts: TypedCountRecord,
) -> AuditManifest
audit_bundle_digest(manifest: AuditManifest) -> str
```

- [ ] **Step 1: Write RED ordering and provenance-binding tests**

Create two record sequences containing the same bytes in opposite order; assert equal roots. Then build two audit manifests that differ only in `provenance_root` and assert different bundle digests.

- [ ] **Step 2: Run RED**

```bash
python -m pytest tests/structure001/test_audit.py -v
```

Expected: FAIL.

- [ ] **Step 3: Implement domain-separated binary Merkle roots**

```python
leaf = sha256(
    b"structure001-leaf-v1\0" + ledger_tag.encode("ascii") + b"\0" + record
).digest()
node = sha256(b"structure001-node-v1\0" + left + right).digest()
```

Sort canonical records before leaf hashing. Duplicate the final node on odd levels. Empty ledger root is `sha256(b"structure001-empty-v1\0" + ledger_tag.encode("ascii")).hexdigest()`.

- [ ] **Step 4: Implement exact audit manifest binding**

`AuditManifest` contains exactly manifest SHA, implementation identity, roots for `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, and `TypedCountRecord`. `audit_bundle_digest` returns `sha256_hex(canonical_encode(manifest))`.

- [ ] **Step 5: Run GREEN**

```bash
python -m pytest tests/structure001/test_audit.py -v
```

Expected: PASS.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/audit.py tests/structure001/test_audit.py
git commit -m "feat: bind STRUCTURE-001 audit bundle"
```

---

## Task 11: Implement quarantined control-run orchestration and replay

**Files:**
- Create: `src/revisics_structure001/replay.py`
- Create: `src/revisics_structure001/__main__.py`
- Create: `tests/structure001/test_replay.py`

**Interfaces:**

```python
require_custody(path: Path) -> PreImplementationCustodyRecord
run_control(output_dir: Path, implementation_id: str, test_limits: TestLimits | None = None) -> ControlRunResult
compare_control_runs(left: Path, right: Path) -> None
```

Production CLI commands:

```text
python -m revisics_structure001 control-run --output PATH --implementation-id SHA
python -m revisics_structure001 compare-control-runs PATH_A PATH_B
python -m revisics_structure001 primary-universe-run --output PATH --implementation-lock PATH
```

`primary-universe-run` must return nonzero unless a later implementation-lock record passes validation. This plan never invokes it.

- [ ] **Step 1: Write RED custody and quarantine tests**

Assert `run_control` rejects: missing custody file, any nonzero custody field, and a nonempty output directory. Assert production CLI has no bound-override flag. Assert `primary-universe-run` returns nonzero without an implementation-lock record.

- [ ] **Step 2: Write RED tiny-domain replay tests**

Define `TestLimits` in `tests/structure001/support.py`, not production code. `run_control(..., test_limits=...)` accepts it only when explicit `test_mode=True` is passed by test helper; production CLI never exposes it. Run a tiny F1/F2 subset twice and assert every ledger and audit digest matches. Mutate one `L_P` framed record and assert `compare_control_runs` raises `ControlFailure` with `control_id="I4_REPLAY_MISMATCH"`.

- [ ] **Step 3: Run RED**

```bash
python -m pytest tests/structure001/test_replay.py -v
```

Expected: FAIL.

- [ ] **Step 4: Implement fixed control pipeline**

Family order is exactly `F1,F2,F3,F4,F5`. For each family: generate raw object; create raw record; validate; canonicalize only family-valid primary objects; create canonical record and raw-to-canonical provenance. For F5, canonicalize bases first, then expand every state/action witness and create an `F5RecodingRecord` plus `f5_recoding_edge` for each witness without deduplication.

Emit these files in every control-run directory:

```text
L_R.bin
L_C.bin
L_V.bin
L_P.bin
L_F5.bin
counts.bin
audit_manifest.bin
audit_bundle.txt
```

No candidate code or applicability matrix is imported or computed.

- [ ] **Step 5: Implement record-level comparison**

Compare framed record streams for `L_R`, `L_C`, `L_V`, `L_P`, `L_F5` record-by-record; then compare `counts.bin`, every ledger root embedded in `audit_manifest.bin`, and `audit_bundle.txt`. On first difference raise `I4_REPLAY_MISMATCH` with ledger name and record index.

- [ ] **Step 6: Run GREEN**

```bash
python -m pytest tests/structure001/test_replay.py -v
```

Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add src/revisics_structure001/replay.py src/revisics_structure001/__main__.py \
  tests/structure001/test_replay.py tests/structure001/support.py
git commit -m "feat: add quarantined STRUCTURE-001 replay"
```

---

## Task 12: Reproduce every frozen construction and canonical count

**Files:**
- Modify: `src/revisics_structure001/generation.py`
- Create: `tests/structure001/test_full_counts.py`

**Interface:**

```python
compute_reference_counts() -> TypedCountRecord
```

`compute_reference_counts` must derive counts by iterating family and canonicalization machinery; it may not return frozen constants as observations.

- [ ] **Step 1: Write RED full count test**

```python
from revisics_structure001.generation import compute_reference_counts


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

- [ ] **Step 2: Run RED**

```bash
python -m pytest tests/structure001/test_full_counts.py -v
```

Expected: FAIL because aggregate count wiring does not yet exist.

- [ ] **Step 3: Implement aggregate observed counting**

Call the exact family iterators and canonicalizer. Count F5 recodings by summing `n! * m!` over the actual canonical F5 base stream, not by returning 139216 directly. Compute assay cases as observed canonical F1 + F2 + F3 + valid canonical F4 + observed F5 recodings.

- [ ] **Step 4: Run GREEN full count control**

```bash
python -m pytest tests/structure001/test_full_counts.py -v
```

Expected: PASS. Any mismatch is `CONTROL_FAILURE -> STOP`; never change expected counts to make the test pass.

- [ ] **Step 5: Run complete suite**

```bash
python -m pytest tests/structure001 -v
```

Expected: all tests PASS.

- [ ] **Step 6: Commit**

```bash
git add src/revisics_structure001/generation.py tests/structure001/test_full_counts.py
git commit -m "test: reproduce STRUCTURE-001 frozen counts"
```

---

## Task 13: Execute two complete quarantined control runs and prepare I0–I4 evidence

**Files produced outside Git history:**

```text
.structure001-control/control-run-a/
.structure001-control/control-run-b/
```

**Files committed as control metadata:**

```text
experiments/STRUCTURE-001/implementation-controls/IMPLEMENTATION_ACCEPTANCE_V1.md
experiments/STRUCTURE-001/implementation-controls/CONTROL_ARTIFACT_INDEX_V1.txt
```

**Important:** this task prepares an acceptance candidate only. It does not create or claim `IMPLEMENTATION_LOCK`.

- [ ] **Step 1: Locally exclude the full control directories**

Append `.structure001-control/` to `.git/info/exclude`. Do not modify repository `.gitignore` for this purpose.

- [ ] **Step 2: Record the exact code identity**

```bash
git rev-parse HEAD
```

Save the returned SHA as `IMPLEMENTATION_ID`. Control A and B must use exactly that SHA and no code changes may occur between them.

- [ ] **Step 3: Run complete control A**

```bash
python -m revisics_structure001 control-run \
  --output .structure001-control/control-run-a \
  --implementation-id "$IMPLEMENTATION_ID"
```

Expected: exit 0 and typed counts equal Task 12.

- [ ] **Step 4: Run complete control B**

```bash
python -m revisics_structure001 control-run \
  --output .structure001-control/control-run-b \
  --implementation-id "$IMPLEMENTATION_ID"
```

Expected: exit 0.

- [ ] **Step 5: Compare A and B**

```bash
python -m revisics_structure001 compare-control-runs \
  .structure001-control/control-run-a \
  .structure001-control/control-run-b
```

Expected: exit 0 with equality of typed counts, every record in `L_R`, `L_C`, `L_V`, `L_P`, `L_F5`, all ledger roots, and `AuditBundle`.

- [ ] **Step 6: Create the durable artifact index**

Write one line per file under both control-run directories with this exact tab-separated schema:

```text
run\tpath\tbytes\tsha256
```

Sort by `(run,path)`. Hash file bytes with SHA-256. The full ledgers remain retained at the indexed paths; the index is not a substitute for them.

If the execution environment cannot guarantee retention of both full run directories through independent review, write `CONTROL_ARTIFACT_RETENTION_FAILURE` into `IMPLEMENTATION_ACCEPTANCE_V1.md` and STOP. Do not claim I4 from roots alone.

- [ ] **Step 7: Write acceptance candidate only from observed evidence**

The file must contain exact values for:

```text
manifest_sha
implementation_sha
custody_record_sha256
control_artifact_index_sha256
I0 status + evidence
I1 status + raw/normalized counts
I2 status + canonical counts + automorphism tie-test reference
I3 status + L_P roots + validation/provenance test reference
I4 status + both AuditBundle digests + compare command result
primary_universe_run=NOT_EXECUTED
candidate_evaluation=NOT_EXECUTED
claim_ceiling=implementation fidelity only; no STRUCTURE-001 scientific result
```

Never write PASS before the corresponding verification command has succeeded.

- [ ] **Step 8: Run fresh final verification**

```bash
python -m pytest tests/structure001 -v
python -m revisics_structure001 compare-control-runs \
  .structure001-control/control-run-a \
  .structure001-control/control-run-b
```

Expected: test suite PASS and replay comparison exit 0.

- [ ] **Step 9: Commit only control metadata, not full control ledgers**

```bash
git add \
  experiments/STRUCTURE-001/implementation-controls/IMPLEMENTATION_ACCEPTANCE_V1.md \
  experiments/STRUCTURE-001/implementation-controls/CONTROL_ARTIFACT_INDEX_V1.txt
git commit -m "control: record STRUCTURE-001 I0-I4 evidence index"
```

Stop for independent review. Do not create or claim `IMPLEMENTATION_LOCK`, invoke `primary-universe-run`, generate the frozen primary universe, or evaluate candidates until the user explicitly authorizes that next custody transition.

---

## Plan Self-Review / Execution Gate

Before Task 1, verify:

```text
scientific contract              9711a6d unchanged
candidate ontology               7d1e3cf unchanged
construction manifest            f587406 unchanged
design                            535013c reviewed
primary frozen universe          not generated
candidate outcomes                none
```

Evidence mapping at the end of Task 13:

```text
I0 custody                       retained zero-state record + frozen Git blob hashes
I1 generation fidelity           exact raw/normalized observed counts
I2 canonicalization fidelity     exact canonical counts + invariance/idempotence/tie tests
I3 validation/provenance         negative controls + complete L_P + content-ID checks
I4 deterministic replay          record equality + all roots + AuditBundle equality
```

**Claim ceiling:** A successful I0–I4 acceptance demonstrates only that the reference software faithfully realizes the frozen STRUCTURE-001 V1 construction contract. It is not a scientific result of STRUCTURE-001.
