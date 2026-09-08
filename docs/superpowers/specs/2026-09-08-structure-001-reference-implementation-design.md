# STRUCTURE-001 Reference Implementation Design

**Status:** Implementation design only  
**Scientific authority:** `experiments/STRUCTURE-001/SYSTEM_CONSTRUCTION_MANIFEST_V1.md @ f5874063b06997f49f3ee80d291de879c8d27a7f`  
**Parent scientific contract:** `9711a6dd1b14ade10fd43a03c424ddc840cc565e`  
**Parent candidate ontology:** `7d1e3cf3bd61b212d6131a7e1d98c10f401aa95d`  
**Scientific changes permitted:** NONE

## 1. Purpose

Build a transparent executable reference specification for STRUCTURE-001 V1. The implementation exists only to realize the frozen construction manifest mechanically.

The governing rule is:

```math
\boxed{\operatorname{Impl}(f587406)=\text{mechanical realization of }f587406}
```

The machine inherits authority from the three locked scientific artifacts; it has no authority to reinterpret or amend them.

A code/manifest semantic mismatch is always:

```text
CONTROL_FAILURE -> STOP
```

not permission to alter the frozen arena.

## 2. Scope

The reference implementation has exactly five responsibilities:

1. **GENERATE** — enumerate exactly the frozen raw constructions.
2. **CANONICALIZE** — quotient only under the frozen family equivalence rules.
3. **VALIDATE** — apply the frozen family-validity and construction-control rules.
4. **ACCOUNT / PROVENANCE** — retain deterministic, reconstructible lineage from raw construction through assay case.
5. **REPLAY** — reproduce the same typed ledgers and identities from the same frozen inputs.

Explicitly out of scope:

- candidate implementations;
- candidate evaluation;
- scientific interpretation;
- optimization;
- sampling;
- changing any family bound or semantic rule;
- changing candidate scope or applicability semantics;
- generating the primary frozen universe before implementation lock.

## 3. Authority hierarchy

```text
f587406 manifest
      | defines scientific meaning
      v
REFERENCE implementation
      | after validation, executable comparison oracle only
      v
future OPTIMIZED implementation
```

If the reference implementation disagrees with the manifest, the manifest wins and the implementation fails control.

The reference implementation is never evidence that the manifest "really meant" something not written there.

## 4. Technology and determinism

Reference implementation language: **Python 3.12**.

Runtime dependencies: Python standard library only.

Test dependency: `pytest`.

No network access, model calls, randomness, wall-clock dependence, filesystem enumeration dependence, locale dependence, process scheduling dependence, or hash-randomization dependence may affect semantic output.

All semantic collections must be explicitly sorted by frozen canonical keys before serialization, hashing, comparison, or ledger emission.

## 5. Package structure

```text
src/revisics_structure001/
    __init__.py
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
    test_replay.py
```

Each module has one responsibility:

- `constants.py`: frozen implementation constants copied from `f587406`, including manifest identity and exact family bounds.
- `model.py`: immutable typed records only; no generation logic.
- `encoding.py`: canonical byte encoding with explicit framing/versioning.
- `identity.py`: SHA-256 content identities from canonical bytes only.
- `generation.py`: family dispatch, no candidate awareness.
- `canonical.py`: family-specific representation quotienting and canonical representative selection.
- `validation.py`: family validity and construction controls.
- `provenance.py`: raw-to-canonical-to-assay lineage records.
- `audit.py`: canonical audit-bundle construction.
- `replay.py`: quarantined control-run orchestration and record-level comparison.
- `families/f*.py`: exact family-native raw enumeration and family-local transforms required by the manifest.

No candidate IDs or candidate result types may appear in generation/canonicalization modules.

## 6. Core immutable records

Implementation records must be immutable dataclasses/tuples with explicit primitive fields. No object identity, insertion order, or Python hash value may carry scientific meaning.

Minimum record classes:

```text
RawConstructionRecord
CanonicalWorldRecord
ValidityRecord
ProvenanceEdge
F5RecodingRecord
TypedCountRecord
AuditManifest
ControlRunResult
```

Family-native payloads are represented with explicit tagged records for F1-F5; they are not free-form dictionaries.

## 7. Canonical encoding

Every hashed or replay-compared artifact must first pass through one canonical encoder.

The encoding contract is:

```text
magic/version
record type tag
field count
for each field in schema order:
    field tag
    byte length
    canonical field bytes
```

Rules:

- UTF-8 for declared text tokens only;
- integers encoded as signed base-10 ASCII with length framing;
- booleans encoded as one byte `0` or `1`;
- finite sequences encoded in declared semantic order;
- unordered mathematical collections sorted by canonical element bytes before encoding;
- no JSON object-order dependence;
- no pickle/marshal/repr as scientific serialization;
- encoding version fixed as `structure001-canonical-v1`.

The exact underlying bytes are retained wherever a SHA-256 identifier is emitted.

## 8. Identity

Use SHA-256 exactly as required by the construction manifest.

```text
WorldID     = SHA256(canonical family-object bytes)
BaseID      = SHA256(canonical F5 base bytes)
InstanceID  = SHA256(label-preserving normalized instance bytes)
RecodingID  = SHA256(canonical encoding of BaseID, phi_X, phi_A)
```

A digest is an integrity/identity field, never a substitute for the underlying record.

## 9. Family generation fidelity

### F1

Enumerate every deterministic partial-action table for `1 <= n,m <= 3`.

Each cell `(a,x)` takes one of `n+1` values: `bot` or a target state in `[n]`.

Required raw total:

```text
267137
```

Graph statistics are derived metadata only and never generation inputs.

### F2

For every F1 table, enumerate every set partition of `X` as the observation partition.

Required raw total:

```text
1333172
```

Future-transformational relation patterns are derived after generation and never used as generation selectors.

### F3

For every deterministic partial table satisfying `1 <= n,m <= 3` and `nm <= 4`, let `k` be the number of executable edges.

Enumerate exactly:

```text
2^k     edge-cost assignments c:E->{0,1}
3^(2k)  resource-update functions u:B x E -> B union {bot}
```

with fixed ordered resource carrier `0 <_B 1` and fixed regime bundle:

```text
R = B x {1,2}
```

No monotonicity filter is applied to `u`.

Required raw total:

```text
2049144
```

### F4

Enumerate deterministic raw cores for `1 <= n,m <= 2` and `H in {1,2}`.

Generate raw histories through the frozen horizon and assign every reachable history-extension admissibility bit `alpha_kappa` exactly as specified by the manifest. Decisions below an already-inadmissible prefix are not separate semantic choices.

Family validity requires at least one same-time pair of distinct admissible histories ending in the same current state.

Required normalized/specification counts:

```text
13056 normalized specifications
10886 valid labeled in the largest (2,2,2) cell
2862 valid canonical total
2784 valid canonical in the largest (2,2,2) cell
```

The reference implementation must use complete T-blind quotient enumeration only when implementing the later F4 construction-control surface required before candidate evaluation; it may not consult future-transformability when generating quotient candidates.

### F5

Primary base bound:

```text
2 <= n,m <= 3
nm <= 6
H = 2
edge cost in {0,1}
```

Enumerate and canonicalize all labeled bases first.

Required counts:

```text
133899 labeled primary bases
11718 canonical primary bases
139216 exhaustive recoding assay cases
```

For each canonical base retain every state bijection and every action bijection, identity included. Distinct recoding maps remain distinct assay cases even if destination serialization coincides.

## 10. Canonicalization design

The reference canonicalizer uses exhaustive relabeling because V1 carriers are small.

For a family object with state carrier size `n` and action carrier size `m`:

1. enumerate every admissible state-label permutation;
2. enumerate every admissible action-label permutation;
3. transport all family-native metadata exactly;
4. canonical-encode each transported object;
5. select the lexicographically least canonical byte string as the representative;
6. retain the winning transport and source provenance.

F3 keeps the ordered resource carrier fixed; it is not relabeled.

F2 transports the observation partition.

F4 transports raw state/action labels through the complete history-extension object.

F5 canonicalizes bases before recoding expansion and never canonical-deduplicates the required recoding ledger afterward.

This deliberately slow method is the reference semantic oracle for canonicalization.

## 11. Validation

Validation is separate from generation and canonicalization.

A validator returns a typed `ValidityRecord`, never a repaired object.

Invalid objects remain in provenance with their failure reason and are excluded only where the manifest says invalid family objects are not members of the canonical primary universe.

Required checks include:

- family bounds/type correctness;
- deterministic partial execution;
- F2 partition validity;
- F3 complete fixed regime bundle, edge-cost range, exact update-function codomain, and regime semantics;
- F4 exact history/extension-table consistency and nonvacuous current-state collision;
- F5 exact execution/accounting transport under every recoding;
- identity and canonical serialization consistency;
- no forbidden F5 deduplication.

No validator may inspect candidate behavior.

## 12. Provenance

Every retained object must support reconstruction of:

```text
manifest SHA
implementation SHA/version
family
raw grammar coordinates
raw canonical bytes or reconstructible primitive payload
raw identity
validity decision + reason
canonical representative identity
canonicalization transport
assay-case identity
```

F5 additionally records:

```text
BaseID
InstanceID
phi_X
phi_A
RecodingID
identity-recoding flag
```

Provenance is append-only within a run. Corrections require a fresh run, not in-place mutation.

## 13. Run classes

Two run classes are mandatory:

```text
CONTROL_RUN
PRIMARY_UNIVERSE_RUN
```

### CONTROL_RUN

Purpose: prove implementation fidelity before implementation lock.

A control run may enumerate the complete V1 domain in quarantine, but its outputs:

- are not scientific assay membership;
- are not the frozen V1 world universe;
- are never supplied to candidate implementations;
- cannot alter bounds, semantics, canonicalization, or validation rules;
- exist only as implementation-control evidence.

### PRIMARY_UNIVERSE_RUN

Forbidden before implementation lock.

After implementation lock, it starts from a clean output directory/state and regenerates the universe under the exact locked implementation.

Only the successful primary run may feed the later world-universe freeze.

## 14. Audit bundle and replay

Each run emits retained canonical ledgers plus an integrity bundle.

Conceptually:

```math
AuditBundle = SHA256(CanonicalEncode(M,I,L_R,L_C,L_V,L_{F5},N))
```

where:

- `M` = exact manifest SHA;
- `I` = exact implementation identity;
- `L_R` = raw-construction ledger/root;
- `L_C` = canonical-world ledger/root;
- `L_V` = validity ledger/root;
- `L_F5` = F5 recoding ledger/root;
- `N` = typed count record.

For scalability, each ledger is written as canonically ordered records and summarized by a deterministic Merkle-style/root digest whose construction is itself specified and tested. The full ledgers remain retained.

Replay acceptance requires both:

```text
record-level equality
AND
AuditBundle_A == AuditBundle_B
```

A matching top-level hash without record-level equality is insufficient evidence.

## 15. Implementation-lock acceptance gates

### I0 — CUSTODY

- implementation branch starts from exact `f5874063b06997f49f3ee80d291de879c8d27a7f`;
- parent scientific artifacts byte-identical to the locked versions;
- no committed generated-world, recoding-output, or candidate-outcome artifacts at implementation start;
- no candidate code imported by construction machinery.

### I1 — GENERATION FIDELITY

- every permitted raw construction generated;
- no prohibited raw construction generated;
- exact manifest raw/normalized counts reproduced;
- family-local enumeration controls pass.

### I2 — CANONICALIZATION FIDELITY

- equivalent representations canonicalize identically exactly where frozen rules require;
- distinct canonical classes are not merged;
- canonicalization is idempotent;
- F5 required recodings are never removed by canonical deduplication;
- exact canonical count controls reproduce the manifest values.

### I3 — VALIDATION / PROVENANCE FIDELITY

- family validity is rule-derived and reproducible;
- invalidity never triggers repair;
- every canonical object has complete raw provenance;
- every F5 recoding has complete base/instance/map provenance;
- all content IDs reproduce from retained canonical bytes.

### I4 — DETERMINISTIC REPLAY

Two clean quarantined complete control runs under the same implementation identity must produce:

- identical typed counts;
- identical canonical record streams;
- identical validity streams;
- identical provenance edges;
- identical F5 recoding ledger;
- identical ledger roots;
- identical `AuditBundle`.

Any mismatch is `CONTROL_FAILURE -> STOP`.

Passing I0-I4 establishes only faithful implementation, not any scientific result.

## 16. Reference versus optimization

No optimized implementation is part of the first implementation lock.

A future optimized implementation is admissible only if it proves extensional equality to the locked reference implementation over the complete frozen V1 domain for:

```text
generation membership
canonical bytes
canonical identities
validity decisions
provenance edges
F5 recoding membership and IDs
typed counts
```

Equal final counts alone are insufficient.

## 17. Testing strategy

Development follows TDD.

Tests are divided into:

1. **local semantic unit tests** — tiny hand-checkable carriers and known canonical transports;
2. **metamorphic tests** — relabeling invariance, canonicalization idempotence, order independence;
3. **count controls** — exact F1-F5 declared totals;
4. **negative controls** — malformed partitions, invalid resource updates, invalid F5 transports, provenance mismatch;
5. **replay controls** — two clean control runs compare record-by-record and by audit digest;
6. **custody tests** — manifest SHA and parent lock identities are hard failures on mismatch.

No test may use candidate pass/fail outcomes as fixtures for construction behavior.

## 18. Failure handling

All control failures are explicit typed exceptions/results carrying:

```text
control_id
family if applicable
record identity if available
expected contract
observed value
```

The CLI exits nonzero on any control failure.

There is no best-effort mode, skip-invalid mode, auto-repair mode, or fallback sampler for primary/control fidelity runs.

## 19. Scientific claim ceiling

A successful implementation lock supports only:

```math
\boxed{\text{The locked reference software faithfully realizes the frozen STRUCTURE-001 V1 construction contract under I0-I4.}}
```

It does not establish the scientific correctness of any candidate, representativeness beyond the frozen finite arena, or any law of Revisics.

## 20. Delivery sequence

```text
f587406
   -> isolated implementation branch
   -> reference package + tests
   -> CONTROL_RUN A
   -> CONTROL_RUN B
   -> I0-I4 acceptance record
   -> IMPLEMENTATION_LOCK
   -> fresh PRIMARY_UNIVERSE_RUN
   -> later WORLD-UNIVERSE FREEZE
```

No primary universe run or candidate evaluation belongs to this design's implementation phase before implementation lock.
