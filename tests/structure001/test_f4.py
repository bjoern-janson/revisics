from revisics_structure001.families.f4 import (
    admissible_histories,
    has_current_state_collision,
    iter_f4,
)
from revisics_structure001.model import ExtensionKey, F4Object, HistoryDecision


def test_forbidden_prefix_generates_no_descendant_decision():
    blocked = next(
        w for w in iter_f4(1, 1, 2)
        if w.decisions and w.decisions[0].allowed is False
    )
    assert len(blocked.decisions) == 1


def test_one_state_one_action_is_negative_collision_control():
    assert all(not has_current_state_collision(w) for w in iter_f4(1, 1, 2))


def test_two_state_one_action_can_create_positive_collision():
    # Raw transitions 0->0 and 1->0; both first-step extensions admitted.
    obj = F4Object(
        n=2,
        m=1,
        targets=(0, 0),
        horizon=1,
        decisions=(
            HistoryDecision(ExtensionKey((0,), 0, 0), True),
            HistoryDecision(ExtensionKey((1,), 0, 0), True),
        ),
    )
    assert has_current_state_collision(obj)
    assert admissible_histories(obj, 1) == ((0, 0, 0), (1, 0, 0))


def test_f4_total_normalized_specs_is_frozen_count():
    total = sum(
        1
        for n in (1, 2)
        for m in (1, 2)
        for horizon in (1, 2)
        for _ in iter_f4(n, m, horizon)
    )
    assert total == 13056
