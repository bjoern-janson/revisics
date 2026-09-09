import pytest

from revisics_structure001.families.f3 import edge_list, iter_decorations, iter_f3, path_is_admissible
from revisics_structure001.model import ControlFailure, F3Object


def test_one_edge_has_eighteen_decorations():
    assert len(list(iter_decorations(1))) == 18


def test_edge_order_is_action_major_then_state():
    assert edge_list(2, 1, (1, 0)) == ((0, 0, 1), (1, 0, 0))


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


def test_f3_rejects_nm_above_four():
    with pytest.raises(ControlFailure) as exc:
        list(iter_f3(3, 2))
    assert exc.value.control_id == "F3_BOUND"
