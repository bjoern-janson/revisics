from __future__ import annotations

from .families.f2 import normalize_partition
from .families.f3 import REGIMES, edge_list
from .families.f4 import executable_extension_keys, has_current_state_collision
from .families.f5 import transport_f5
from .identity import content_id
from .model import (
    F1Object,
    F2Object,
    F3Object,
    F4Object,
    F5BaseObject,
    TransportWitness,
    ValidityRecord,
)


def _record(
    obj: object,
    family: str,
    valid: bool,
    reason_code: str,
    expected: str = "",
    observed: str = "",
) -> ValidityRecord:
    return ValidityRecord(
        family=family,
        record_id=content_id(obj),
        valid=valid,
        reason_code=reason_code,
        expected=expected,
        observed=observed,
    )


def _targets_valid(n: int, m: int, targets: tuple[int | None, ...]) -> bool:
    return len(targets) == n * m and all(
        target is None or (isinstance(target, int) and 0 <= target < n)
        for target in targets
    )


def _validate_f1(obj: F1Object) -> ValidityRecord:
    if not _targets_valid(obj.n, obj.m, obj.targets):
        return _record(
            obj,
            "F1",
            False,
            "F1_TARGET_OUT_OF_RANGE",
            expected=f"{obj.n * obj.m} targets, each None or in [0,{obj.n})",
            observed=str(obj.targets),
        )
    return _record(obj, "F1", True, "VALID")


def _validate_f2(obj: F2Object) -> ValidityRecord:
    if not _targets_valid(obj.n, obj.m, obj.targets):
        return _record(
            obj,
            "F2",
            False,
            "F1_TARGET_OUT_OF_RANGE",
            expected=f"{obj.n * obj.m} targets, each None or in [0,{obj.n})",
            observed=str(obj.targets),
        )
    partition_valid = (
        len(obj.partition) == obj.n
        and all(isinstance(label, int) and label >= 0 for label in obj.partition)
        and normalize_partition(obj.partition) == obj.partition
    )
    if not partition_valid:
        return _record(
            obj,
            "F2",
            False,
            "F2_PARTITION_INVALID",
            expected="normalized restricted-growth partition of X",
            observed=str(obj.partition),
        )
    return _record(obj, "F2", True, "VALID")


def _validate_f3(obj: F3Object) -> ValidityRecord:
    if not _targets_valid(obj.n, obj.m, obj.targets):
        return _record(
            obj,
            "F3",
            False,
            "F1_TARGET_OUT_OF_RANGE",
            expected=f"{obj.n * obj.m} targets, each None or in [0,{obj.n})",
            observed=str(obj.targets),
        )
    k = len(edge_list(obj.n, obj.m, obj.targets))
    if len(obj.costs) != k or any(cost not in (0, 1) for cost in obj.costs):
        return _record(
            obj,
            "F3",
            False,
            "F3_COST_OUT_OF_RANGE",
            expected=f"{k} binary edge costs",
            observed=str(obj.costs),
        )
    if len(obj.updates) != 2 * k or any(update not in (None, 0, 1) for update in obj.updates):
        return _record(
            obj,
            "F3",
            False,
            "F3_UPDATE_OUT_OF_CODOMAIN",
            expected=f"{2 * k} values in {{None,0,1}}",
            observed=str(obj.updates),
        )
    if obj.regimes != REGIMES:
        return _record(
            obj,
            "F3",
            False,
            "F3_REGIME_BUNDLE_MISMATCH",
            expected=str(REGIMES),
            observed=str(obj.regimes),
        )
    return _record(obj, "F3", True, "VALID")


def _validate_f4(obj: F4Object) -> ValidityRecord:
    if not _targets_valid(obj.n, obj.m, obj.targets):
        return _record(
            obj,
            "F4",
            False,
            "F1_TARGET_OUT_OF_RANGE",
            expected=f"{obj.n * obj.m} targets, each None or in [0,{obj.n})",
            observed=str(obj.targets),
        )
    if obj.horizon not in (1, 2):
        return _record(
            obj,
            "F4",
            False,
            "F4_EXTENSION_KEY_INCONSISTENT",
            expected="horizon in {1,2}",
            observed=str(obj.horizon),
        )

    histories = tuple((x,) for x in range(obj.n))
    by_depth: dict[int, list] = {depth: [] for depth in range(obj.horizon)}
    for decision in obj.decisions:
        history_len = len(decision.key.history)
        if history_len < 1 or history_len % 2 == 0:
            return _record(
                obj,
                "F4",
                False,
                "F4_EXTENSION_KEY_INCONSISTENT",
                expected="odd-length alternating history key",
                observed=str(decision.key),
            )
        depth = (history_len - 1) // 2
        if depth not in by_depth:
            return _record(
                obj,
                "F4",
                False,
                "F4_EXTENSION_KEY_INCONSISTENT",
                expected=f"decision depth < {obj.horizon}",
                observed=str(decision.key),
            )
        by_depth[depth].append(decision)

    for depth in range(obj.horizon):
        expected_keys = executable_extension_keys(histories, obj.n, obj.m, obj.targets)
        actual = by_depth[depth]
        actual_keys = tuple(decision.key for decision in actual)
        if actual_keys != expected_keys or len(set(actual_keys)) != len(actual_keys):
            return _record(
                obj,
                "F4",
                False,
                "F4_EXTENSION_KEY_INCONSISTENT",
                expected=str(expected_keys),
                observed=str(actual_keys),
            )
        histories = tuple(
            decision.key.extended_history
            for decision in actual
            if decision.allowed
        )

    if not has_current_state_collision(obj):
        return _record(
            obj,
            "F4",
            False,
            "F4_NO_CURRENT_STATE_COLLISION",
            expected="at least one same-time distinct-history current-state collision",
            observed="none",
        )
    return _record(obj, "F4", True, "VALID")


def _validate_f5_base(obj: F5BaseObject) -> ValidityRecord:
    if not _targets_valid(obj.n, obj.m, obj.targets):
        return _record(
            obj,
            "F5",
            False,
            "F1_TARGET_OUT_OF_RANGE",
            expected=f"{obj.n * obj.m} targets, each None or in [0,{obj.n})",
            observed=str(obj.targets),
        )
    k = len(edge_list(obj.n, obj.m, obj.targets))
    if len(obj.costs) != k or any(cost not in (0, 1) for cost in obj.costs):
        return _record(
            obj,
            "F5",
            False,
            "F5_COST_OUT_OF_RANGE",
            expected=f"{k} binary edge costs",
            observed=str(obj.costs),
        )
    if obj.horizon != 2:
        return _record(
            obj,
            "F5",
            False,
            "F5_HORIZON_MISMATCH",
            expected="2",
            observed=str(obj.horizon),
        )
    return _record(obj, "F5", True, "VALID")


def validate(obj: object) -> ValidityRecord:
    if isinstance(obj, F1Object):
        return _validate_f1(obj)
    if isinstance(obj, F2Object):
        return _validate_f2(obj)
    if isinstance(obj, F3Object):
        return _validate_f3(obj)
    if isinstance(obj, F4Object):
        return _validate_f4(obj)
    if isinstance(obj, F5BaseObject):
        return _validate_f5_base(obj)
    return ValidityRecord(
        family="UNKNOWN",
        record_id=content_id(obj),
        valid=False,
        reason_code="VALIDATION_UNSUPPORTED_FAMILY",
        expected="F1-F5 family object",
        observed=type(obj).__qualname__,
    )


def validate_f5_recoding(
    base: F5BaseObject,
    witness: TransportWitness,
    destination: F5BaseObject,
) -> ValidityRecord:
    expected = transport_f5(base, witness)
    record_id = content_id((base, witness, destination))
    if destination.targets != expected.targets:
        return ValidityRecord(
            family="F5",
            record_id=record_id,
            valid=False,
            reason_code="F5_EXEC_TRANSPORT_MISMATCH",
            expected=str(expected.targets),
            observed=str(destination.targets),
        )
    if destination.costs != expected.costs or destination.horizon != expected.horizon:
        return ValidityRecord(
            family="F5",
            record_id=record_id,
            valid=False,
            reason_code="F5_COST_TRANSPORT_MISMATCH",
            expected=f"costs={expected.costs},horizon={expected.horizon}",
            observed=f"costs={destination.costs},horizon={destination.horizon}",
        )
    return ValidityRecord(
        family="F5",
        record_id=record_id,
        valid=True,
        reason_code="VALID",
        expected="exact F5 execution/accounting transport",
        observed="exact",
    )
