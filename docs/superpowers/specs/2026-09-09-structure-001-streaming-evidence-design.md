# STRUCTURE-001 Streaming Evidence Amendment — Design

Status: PROSPECTIVE IMPLEMENTATION-CONTROL AMENDMENT ONLY

Scientific authority remains unchanged:

- `experiments/STRUCTURE-001/PREREGISTRATION_V1.md @ 9711a6dd1b14ade10fd43a03c424ddc840cc565e`
- `experiments/STRUCTURE-001/CANDIDATE_SPECIFICATION_MANIFEST_V1.md @ 7d1e3cf3bd61b212d6131a7e1d98c10f401aa95d`
- `experiments/STRUCTURE-001/SYSTEM_CONSTRUCTION_MANIFEST_V1.md @ f5874063b06997f49f3ee80d291de879c8d27a7f`

This amendment changes only how implementation-control evidence is committed, retained, and replay-compared. It does not change any candidate, family, bound, grammar, canonicalization semantics, validity rule, F5 recoding requirement, expected count, assay membership rule, or scientific claim ceiling.

## 1. Why this amendment exists

The first complete control traversal under implementation `d01e9676c9ff2f96772105f17adac56de86ab975` demonstrated that full canonical-ledger retention is operationally expensive: approximately 9.7 GB of retained control material for one run. The traversal reached the frozen expected cardinalities, but the retained artifacts are no longer available in the current execution environment, so that run cannot satisfy the retained-artifact verification gate.

That run is therefore classified prospectively and permanently as:

```text
CONTROL_RUN_A0
traversal_completed=YES
frozen_counts_matched=YES
independent_retained_artifact_verification=NOT_ESTABLISHED
authorizing_status=NON_AUTHORIZING
```

A0 may motivate an engineering-cost reduction because artifact retention itself proved impractical. A0 must not be used as evidence for I0-I4 acceptance, implementation lock, a world-universe freeze, candidate evaluation, or a scientific claim.

## 2. Design objective

Preserve the falsification-relevant information of the complete control streams while reducing retained storage by orders of magnitude.

The target is:

```text
one complete A1 traversal with compact commitments
+
one complete B1 replay with the same compact commitments
+
exact count/root/bundle equality
```

not:

```text
retain every multi-gigabyte canonical record stream twice
+
re-read both complete streams repeatedly
```

The acceptance object becomes a compact cryptographic commitment to every scientifically meaningful emitted record, together with exact typed counts and a small diagnostic witness bundle.

## 3. Approaches considered

### A. Full retained ledgers

Strongest direct replay evidence, but operationally wasteful. One observed traversal produced about 9.7 GB of retained material. Rejected for the amended protocol because retention cost is disproportionate to the bounded implementation-fidelity claim.

### B. Sorted fixed-width leaf commitments — CHOSEN

Each canonical record is immediately reduced to a domain-separated 32-byte leaf digest. Only leaf digests are spooled transiently. They are externally sorted using a deterministic stdlib-only chunk/merge procedure, duplicates preserved, and reduced to a count-bound Merkle root. Full canonical records are not retained after local validation and diagnostic sampling.

Advantages:

- commits to every emitted canonical record;
- preserves multiplicity;
- remains invariant to generation order;
- retains the existing canonical-set comparison intent;
- transient storage becomes fixed-width digest storage rather than full record storage;
- retained evidence is compact.

### C. Pure commutative streaming accumulator

Cheapest storage, but would introduce a less familiar multiset-commitment construction and a larger cryptographic-review burden. Rejected for V1 implementation controls.

## 4. Exact commitment algorithm

For each ledger tag `T` in:

```text
L_R
L_C
L_V
L_P
L_F5
```

and each canonical record byte string `r`, compute:

```text
leaf = SHA256(
    b"structure001-leaf-v2\0"
    + T.encode("ascii")
    + b"\0"
    + r
)
```

Append only the 32-byte `leaf` value to a transient leaf spool for `T`.

No leaf may be omitted because its source record is large, duplicated, invalid, or inconvenient. Duplicate leaf values remain duplicate records and remain present in the spool.

### 4.1 Deterministic fixed-width external sort

At finalization:

1. read bounded chunks of 32-byte leaf values;
2. sort each chunk lexicographically;
3. write sorted fixed-width chunk files;
4. perform a deterministic k-way merge of all chunks;
5. preserve duplicates exactly;
6. emit one sorted level-0 digest stream.

No platform `sort` command, database, network service, or third-party package is allowed. Python 3.13.5 standard library only.

### 4.2 Merkle reduction

Given the sorted level-0 leaf stream:

- pair adjacent 32-byte nodes;
- for an odd final node at a level, duplicate that node exactly once for the final pair;
- compute each parent as:

```text
SHA256(
    b"structure001-node-v2\0"
    + T.encode("ascii")
    + b"\0"
    + left
    + right
)
```

- write the next fixed-width level transiently;
- continue until one tree digest remains.

The empty-tree digest is:

```text
SHA256(
    b"structure001-empty-v2\0"
    + T.encode("ascii")
)
```

The final ledger root binds exact record count:

```text
Root_v3(T,R) = SHA256(
    b"structure001-root-v3\0"
    + T.encode("ascii")
    + b"\0"
    + ASCII_decimal(record_count)
    + b"\0"
    + tree_digest
).hexdigest()
```

Therefore duplication or deletion changes either the count, the tree digest, or both.

All leaf, chunk, and intermediate Merkle-level files are transient control machinery and are deleted only after the compact retained receipt has been durably written and self-checked.

## 5. Retained evidence

Each authoritative amended control run retains only:

```text
RUN_RECEIPT_V2.json
TYPED_COUNTS_V2.bin
LEDGER_ROOTS_V2.txt
AUDIT_BUNDLE_V2.txt
F5_COMPLETENESS_SUMMARY_V2.bin
DIAGNOSTIC_WITNESSES_V2.bin
CONTROL_FAILURES_V2.bin
RUN_LOG_V2.txt
```

No full `L_R`, `L_C`, `L_V`, `L_P`, or `L_F5` canonical-record ledger is retained.

### 5.1 F5 completeness summary

For every canonical F5 base retain one compact summary containing at least:

```text
BaseID
n
m
emitted_count
expected_count = n! * m!
identity_seen
witness_set_root
all_recodings_valid
```

`witness_set_root` commits to the complete emitted `(phi_X,phi_A)` witness multiset for that base. The run fails immediately if:

- a witness is not a bijection;
- a witness is duplicated;
- identity is absent;
- emitted count differs from `n!m!`;
- any `validate_f5_recoding` result is invalid.

The global F5 recoding count remains the actual number of emitted recoding records, never a value manufactured from factorials.

### 5.2 Diagnostic witnesses

Retain a small deterministic diagnostic sample from each ledger so later review has inspectable concrete records without retaining the full universe.

Sampling rule:

```text
sample_key = SHA256(
    b"structure001-diagnostic-v1\0"
    + T.encode("ascii")
    + b"\0"
    + canonical_record
)
```

Retain the 32 records with lexicographically smallest `sample_key` values per ledger, with full canonical record bytes and source metadata. This rule is outcome-independent and fixed before A1.

Diagnostic witnesses are for inspection/debugging only. Acceptance depends on full-stream commitments and exact counts, not sample behavior.

## 6. Audit bundle V2

The compact audit manifest binds:

```text
scientific_manifest_sha
implementation_id
python_version=3.13.5
commitment_protocol=structure001-streaming-evidence-v2
Root_v3(L_R)
Root_v3(L_C)
Root_v3(L_V)
Root_v3(L_P)
Root_v3(L_F5)
TypedCountRecord
F5CompletenessSummaryRoot
DiagnosticWitnessBundleRoot
```

Then:

```text
AuditBundleV2 = SHA256(CanonicalEncode(AuditManifestV2))
```

The commitment protocol version is explicit so A0/V1 roots cannot be confused with A1/B1 roots.

## 7. Commitment implementation verification

Because full ledgers are not retained, correctness of the commitment machinery must be established before A1 by local TDD controls against the transparent in-memory reference root.

Required tests include:

- empty stream;
- one record;
- even and odd record counts;
- duplicate records;
- `[a,b,c] != [a,b,c,c]`;
- every permutation of a small record multiset gives the same root;
- chunk boundary sizes 1, 2, 3, and several nontrivial values;
- multiple external-sort chunks;
- transient chunk merge preserves multiplicity;
- external digest-spool root equals an in-memory reference implementation on exhaustive small synthetic multisets;
- changing any canonical record changes the expected root except with cryptographic hash collision;
- changing ledger tag changes the root;
- changing count changes the final root;
- transient files are deleted only after retained receipt verification succeeds.

A failure in commitment equivalence is `CONTROL_FAILURE -> STOP` and forbids A1.

## 8. A1/B1 protocol

A0 is not replayed or repaired.

After the amendment implementation is complete and all cheap controls pass, record the exact new implementation commit as `IMPLEMENTATION_ID_V2`.

Then execute exactly two authoritative complete traversals:

```text
CONTROL_RUN_A1
    complete frozen arena traversal
    exact observed-count checks
    live validity/F5/provenance controls
    compact Root_v3 commitments
    compact retained evidence

CONTROL_RUN_B1
    same exact implementation identity
    same complete frozen arena traversal
    same controls
    same compact commitments
```

No third complete traversal is part of the amended acceptance path.

## 9. Acceptance comparison

A1 and B1 each independently fail unless every frozen expected count matches.

Cross-run I4 requires exact equality of:

```text
implementation_id
scientific_manifest_sha
python_version
commitment_protocol
TypedCountRecord
Root_v3(L_R)
Root_v3(L_C)
Root_v3(L_V)
Root_v3(L_P)
Root_v3(L_F5)
F5CompletenessSummaryRoot
DiagnosticWitnessBundleRoot
AuditBundleV2
```

The retained compact artifacts from both runs are then indexed by path, byte size, and SHA-256 for independent review.

## 10. Mapping to I0-I4

```text
I0 CUSTODY
    unchanged scientific blobs
    retained four-zero preimplementation custody record
    exact Python 3.13.5
    A0 explicitly NON_AUTHORIZING

I1 GENERATION FIDELITY
    observed complete-traversal counts in A1 and B1
    exact equality to frozen count table

I2 CANONICALIZATION FIDELITY
    existing invariance/idempotence/tie controls
    observed canonical counts
    full L_C Root_v3 equality A1 == B1

I3 VALIDATION / PROVENANCE FIDELITY
    existing negative controls
    every actual F5 recoding validated live
    complete L_V and L_P commitments
    compact F5 per-base completeness summaries

I4 DETERMINISTIC REPLAY
    A1 == B1 exact typed counts
    A1 == B1 all full-stream roots
    A1 == B1 compact F5 summary root
    A1 == B1 AuditBundleV2
```

Successful I0-I4 acceptance still establishes implementation fidelity only.

## 11. Failure policy

Any of the following is a hard stop:

```text
scientific blob mismatch
commitment-equivalence test failure
observed frozen-count mismatch
invalid family object where validity is required
F5 witness omission/duplication/non-bijection
F5 recoding validation failure
provenance construction failure
A1/B1 root mismatch
A1/B1 count mismatch
A1/B1 AuditBundle mismatch
retained compact evidence missing after run
```

No mismatch may be repaired by changing the scientific manifest, candidate definitions, world bounds, family semantics, or observed counts.

## 12. Cost target

This amendment is explicitly intended to spend CPU on the two necessary complete traversals while avoiding multi-gigabyte retained evidence.

Expected shape:

```text
transient fixed-width digest spools: hundreds of MB, not ~10 GB canonical ledgers
retained evidence: MB-scale or less
complete authoritative traversals: exactly two
full post-run 10 GB rereads: zero
```

No numerical storage ceiling is a scientific acceptance condition; it is an engineering objective. If the fixed-width implementation unexpectedly remains impractical, stop and review rather than silently weakening controls.

## 13. Authority and claim ceiling

This amendment does not authorize any new scientific statement.

It does not establish:

- candidate survival or refutation;
- a forced Revisics structure;
- representativeness beyond the frozen finite arena;
- an implementation lock by itself;
- a world-universe freeze;
- any candidate evaluation result.

The maximum post-acceptance implementation claim remains:

> Successful I0-I4 acceptance demonstrates only that the reference software faithfully realizes the frozen STRUCTURE-001 V1 construction contract under the amended compact evidence protocol.

## 14. Prospective execution order

```text
scientific stones remain untouched
        ↓
this amendment design review
        ↓
TDD implementation-plan amendment
        ↓
commitment-equivalence controls
        ↓
cheap full local preflight
        ↓
freeze IMPLEMENTATION_ID_V2
        ↓
CONTROL_RUN_A1
        ↓
CONTROL_RUN_B1
        ↓
compact evidence comparison
        ↓
I0-I4 acceptance record
        ↓
STOP FOR REVIEW
```

Still prohibited at the terminal point:

```text
DO NOT create IMPLEMENTATION_LOCK automatically
DO NOT run PRIMARY_UNIVERSE_RUN
DO NOT freeze a world universe
DO NOT evaluate candidates
DO NOT make a STRUCTURE-001 scientific claim
```
