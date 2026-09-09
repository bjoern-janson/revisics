# STRUCTURE-001 Reference Implementation Design — Amendment V1

**Status:** Prospective implementation-design amendment only  
**Applies to:** `docs/superpowers/specs/2026-09-08-structure-001-reference-implementation-design.md @ 535013cf4ce97234c1777a3ae1d7884c0578b455`  
**Scientific authority remains:** `experiments/STRUCTURE-001/SYSTEM_CONSTRUCTION_MANIFEST_V1.md @ f5874063b06997f49f3ee80d291de879c8d27a7f`  
**Scientific changes permitted:** NONE

This amendment changes implementation controls only. It does not alter the scientific contract, candidate ontology, construction manifest, family semantics, numerical bounds, or claim ceiling.

## A1. Exact runtime

The reference runtime is changed prospectively from Python 3.12 to exactly:

```text
Python 3.13.5
```

The implementation and both complete control runs must execute under `sys.version_info[:3] == (3, 13, 5)`. A runtime mismatch is `CONTROL_FAILURE -> STOP`.

Runtime dependencies remain Python standard library only. `pytest` remains a test dependency only.

## A2. Cost discipline

Before implementation lock, the reference program performs only the two complete V1 control traversals required for deterministic replay:

```text
CONTROL_RUN A
CONTROL_RUN B
```

No redundant third full-domain dry run is required. Local TDD uses hand-checkable fixtures, symbolic raw-count controls where exact closed forms exist, and bounded metamorphic tests. Exact observed raw, canonical, validity, provenance, and F5 recoding counts are asserted inside each complete control run.

This is an execution-cost rule only. It does not weaken any I0-I4 acceptance condition.

## A3. F5 recoding validation is mandatory per emitted case

For every canonical F5 base and every emitted recoding witness, the implementation must:

1. construct the destination by exact transport;
2. call `validate_f5_recoding(base, witness, destination)`;
3. retain the resulting `ValidityRecord` in `L_V`;
4. stop immediately on execution-transport or cost-transport mismatch;
5. emit the F5 recoding record only after validation passes.

Deterministic reproduction of the same transport bug in both runs is therefore not sufficient for acceptance.

## A4. F5 recoding completeness is measured from the emitted stream

`f5_recodings` is the count of emitted, validated F5 recoding records. It must not be assigned from `n!m!` or from the frozen expected total.

For each canonical F5 base, independently verify the emitted witness stream by all of:

```text
all phi_X values are bijections on [n]
all phi_A values are bijections on [m]
identity witness is present
no duplicate (phi_X, phi_A) witness occurs
emitted witness count == factorial(n) * factorial(m)
```

Failure is `CONTROL_FAILURE -> STOP`. After all bases, the observed emitted total must equal the frozen `139216`.

## A5. Ledger roots bind exact record cardinality

The binary tree may duplicate the final node on odd levels, but the final ledger root must additionally bind the exact record count.

For a ledger tag `T`, sorted record stream `R`, record count `N`, and binary tree digest `D`, define:

```text
Root(T,R) = SHA256(
    b"structure001-root-v2\0" ||
    ASCII(T) || b"\0" ||
    ASCII_decimal(N) || b"\0" ||
    D
)
```

Leaf and internal-node domain separation remains:

```text
leaf = SHA256(b"structure001-leaf-v1\0" || T || b"\0" || record)
node = SHA256(b"structure001-node-v1\0" || left || right)
```

The empty tree digest is domain-separated before the count-bound final root is formed.

Required regression:

```text
Root([a,b,c]) != Root([a,b,c,c])
```

for the same ledger tag.

## A6. Each control run is integrity-verified before cross-run comparison

Add:

```python
verify_run_integrity(run_dir) -> VerifiedRun
```

For each run independently, it must:

1. read every retained ledger stream;
2. recompute `L_R`, `L_C`, `L_V`, `L_P`, and `L_F5` roots from the retained records and exact lengths;
3. compare those recomputed roots with the stored run metadata;
4. reconstruct the `AuditManifest` from the validated roots, manifest SHA, implementation identity, and retained typed counts;
5. recompute the `AuditBundle` digest;
6. compare that digest with the stored digest;
7. fail on any stale or inconsistent retained artifact.

Only two independently verified runs may then enter `compare_control_runs`.

## A7. F4 local controls

The normalization regression must select a world with at least one decision before reading `decisions[0]`:

```python
blocked = next(
    w for w in iter_f4(1, 1, 2)
    if w.decisions and w.decisions[0].allowed is False
)
assert len(blocked.decisions) == 1
```

The `n=m=1` carrier is retained as a negative collision control. A positive collision control uses two states and one action with both raw transitions targeting the same state and both first-step extensions allowed, yielding two distinct same-time histories with the same terminal state.

## A8. Production CLI bootstrap without package installation

To minimize setup cost and avoid network/build isolation, add a repository script:

```text
scripts/structure001
```

It resolves repository root, verifies exact Python 3.13.5, prepends `<repo>/src` to `PYTHONPATH`, and executes:

```text
python -m revisics_structure001 "$@"
```

All production control-run commands use this wrapper. A smoke check outside pytest is mandatory:

```bash
./scripts/structure001 --help
```

No editable install, wheel build, or network package operation is required.

## A9. `ControlFailure` has an explicit constructor

The implementation contract is:

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

Keyword construction must therefore be valid and test-covered.

## A10. Test-only replay limits are explicitly gated

The replay interface is:

```python
run_control(
    output_dir: Path,
    implementation_id: str,
    *,
    test_mode: bool = False,
    test_limits: TestLimits | None = None,
) -> ControlRunResult
```

If `test_limits is not None` while `test_mode is False`, fail with `CONTROL_FAILURE`. The production CLI exposes no `test_mode` or bound-override argument.

## A11. Claim ceiling and stop boundary unchanged

Passing the amended implementation controls supports only:

```text
The locked reference software faithfully realizes the frozen STRUCTURE-001 V1 construction contract under I0-I4.
```

It remains not a scientific result. `PRIMARY_UNIVERSE_RUN`, world-universe freeze, candidate evaluation, and scientific interpretation remain prohibited until independent review and explicit authorization of the implementation lock.
