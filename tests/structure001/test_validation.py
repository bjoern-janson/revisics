from revisics_structure001.encoding import canonical_encode
from revisics_structure001.model import (
    ExtensionKey,
    F1Object,
    F2Object,
    F3Object,
    F4Object,
    F5BaseObject,
    HistoryDecision,
    TransportWitness,
)
from revisics_structure001.validation import validate, validate_f5_recoding


def assert_invalid(obj, reason):
    before = canonical_encode(obj)
    result = validate(obj)
    after = canonical_encode(obj)
    assert before == after
    assert not result.valid
    assert result.reason_code == reason


def test_f1_target_out_of_range():
    assert_invalid(F1Object(1, 1, (2,)), "F1_TARGET_OUT_OF_RANGE")


def test_f2_partition_invalid():
    assert_invalid(F2Object(2, 1, (None, None), (0, 2)), "F2_PARTITION_INVALID")


def test_f3_negative_controls():
    regimes = ((0, 1), (0, 2), (1, 1), (1, 2))
    assert_invalid(F3Object(1, 1, (0,), (2,), (0, 0), regimes), "F3_COST_OUT_OF_RANGE")
    assert_invalid(F3Object(1, 1, (0,), (0,), (7, 0), regimes), "F3_UPDATE_OUT_OF_CODOMAIN")
    assert_invalid(F3Object(1, 1, (0,), (0,), (0, 0), ((0, 1), (1, 1))), "F3_REGIME_BUNDLE_MISMATCH")


def test_f4_extension_key_inconsistent():
    obj = F4Object(
        n=2,
        m=1,
        targets=(1, None),
        horizon=1,
        decisions=(HistoryDecision(ExtensionKey((1,), 0, 1), True),),
    )
    assert_invalid(obj, "F4_EXTENSION_KEY_INCONSISTENT")


def test_f4_no_collision_is_invalid_family_object():
    obj = F4Object(
        n=1,
        m=1,
        targets=(0,),
        horizon=1,
        decisions=(HistoryDecision(ExtensionKey((0,), 0, 0), True),),
    )
    assert_invalid(obj, "F4_NO_CURRENT_STATE_COLLISION")


def test_f5_recoding_detects_execution_and_cost_mismatches():
    base = F5BaseObject(2, 2, (0, 1, 0, 1), (0, 1, 0, 1), 2)
    witness = TransportWitness((1, 0), (0, 1))
    from revisics_structure001.families.f5 import transport_f5
    good = transport_f5(base, witness)
    bad_exec = F5BaseObject(good.n, good.m, (None,) + good.targets[1:], good.costs[1:] if good.targets[0] is not None else good.costs, good.horizon)
    result = validate_f5_recoding(base, witness, bad_exec)
    assert not result.valid
    assert result.reason_code == "F5_EXEC_TRANSPORT_MISMATCH"

    bad_costs = list(good.costs)
    bad_costs[0] = 1 - bad_costs[0]
    bad_cost = F5BaseObject(good.n, good.m, good.targets, tuple(bad_costs), good.horizon)
    result2 = validate_f5_recoding(base, witness, bad_cost)
    assert not result2.valid
    assert result2.reason_code == "F5_COST_TRANSPORT_MISMATCH"


def test_valid_f1_passes():
    result = validate(F1Object(2, 1, (1, None)))
    assert result.valid
    assert result.reason_code == "VALID"
