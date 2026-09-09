import pytest

from revisics_structure001.model import ControlFailure
from revisics_structure001.families.f1 import iter_f1


def test_f1_two_states_one_action_has_nine_tables():
    assert len(list(iter_f1(2, 1))) == 9


def test_f1_cell_order_is_action_major_then_state():
    first_defined = next(obj for obj in iter_f1(2, 1) if obj.targets != (None, None))
    assert len(first_defined.targets) == 2


def test_f1_rejects_out_of_bound_carrier():
    with pytest.raises(ControlFailure) as exc:
        list(iter_f1(4, 1))
    assert exc.value.control_id == "F1_BOUND"
