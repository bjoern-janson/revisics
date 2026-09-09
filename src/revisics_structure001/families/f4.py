from itertools import product
from typing import Iterator

from ..model import ControlFailure, ExtensionKey, F4Object, HistoryDecision
from .f1 import iter_f1


def _terminal_state(history: tuple[int, ...]) -> int:
    return history[-1]


def executable_extension_keys(
    histories: tuple[tuple[int, ...], ...],
    n: int,
    m: int,
    targets: tuple[int | None, ...],
) -> tuple[ExtensionKey, ...]:
    keys: list[ExtensionKey] = []
    for history in histories:
        x = _terminal_state(history)
        for action in range(m):
            target = targets[action * n + x]
            if target is not None:
                keys.append(ExtensionKey(history=history, action=action, target=target))
    return tuple(sorted(keys))


def _enumerate_decisions(
    n: int,
    m: int,
    targets: tuple[int | None, ...],
    horizon: int,
    depth: int,
    histories_by_depth: tuple[tuple[tuple[int, ...], ...], ...],
    decisions: tuple[HistoryDecision, ...],
) -> Iterator[tuple[HistoryDecision, ...]]:
    if depth == horizon:
        yield decisions
        return
    keys = executable_extension_keys(histories_by_depth[depth], n, m, targets)
    for bits in product((False, True), repeat=len(keys)):
        next_histories = tuple(
            key.extended_history
            for key, bit in zip(keys, bits)
            if bit
        )
        next_decisions = decisions + tuple(
            HistoryDecision(key=key, allowed=bit)
            for key, bit in zip(keys, bits)
        )
        yield from _enumerate_decisions(
            n,
            m,
            targets,
            horizon,
            depth + 1,
            histories_by_depth + (next_histories,),
            next_decisions,
        )


def iter_f4(n: int, m: int, horizon: int) -> Iterator[F4Object]:
    if not (1 <= n <= 2 and 1 <= m <= 2 and horizon in (1, 2)):
        raise ControlFailure(
            control_id="F4_BOUND",
            family="F4",
            expected="1 <= n,m <= 2 and horizon in {1,2}",
            observed=f"n={n},m={m},H={horizon}",
        )
    initial_histories = tuple((x,) for x in range(n))
    for core in iter_f1(n, m):
        for decisions in _enumerate_decisions(
            n,
            m,
            core.targets,
            horizon,
            0,
            (initial_histories,),
            (),
        ):
            yield F4Object(
                n=n,
                m=m,
                targets=core.targets,
                horizon=horizon,
                decisions=decisions,
            )


def admissible_histories(obj: F4Object, t: int) -> tuple[tuple[int, ...], ...]:
    if not (0 <= t <= obj.horizon):
        raise ControlFailure(
            control_id="F4_HISTORY_TIME",
            family="F4",
            expected=f"0 <= t <= {obj.horizon}",
            observed=f"t={t}",
        )
    decision_map = {decision.key: decision.allowed for decision in obj.decisions}
    histories = tuple((x,) for x in range(obj.n))
    if t == 0:
        return histories
    for _depth in range(t):
        next_histories: list[tuple[int, ...]] = []
        for key in executable_extension_keys(histories, obj.n, obj.m, obj.targets):
            if decision_map.get(key) is True:
                next_histories.append(key.extended_history)
        histories = tuple(next_histories)
    return histories


def has_current_state_collision(obj: F4Object) -> bool:
    for t in range(1, obj.horizon + 1):
        histories = admissible_histories(obj, t)
        by_terminal: dict[int, int] = {}
        for history in histories:
            terminal = _terminal_state(history)
            by_terminal[terminal] = by_terminal.get(terminal, 0) + 1
            if by_terminal[terminal] >= 2:
                return True
    return False


def _transport_history(history, witness):
    return tuple(
        witness.phi_x[value] if index % 2 == 0 else witness.phi_a[value]
        for index, value in enumerate(history)
    )


def transport_f4(obj, witness):
    from .f1 import transport_f1, validate_transport_witness
    from ..model import F1Object

    validate_transport_witness(obj.n, obj.m, witness)
    base = transport_f1(F1Object(obj.n, obj.m, obj.targets), witness)
    transported_decisions = []
    for decision in obj.decisions:
        key = decision.key
        new_key = ExtensionKey(
            history=_transport_history(key.history, witness),
            action=witness.phi_a[key.action],
            target=witness.phi_x[key.target],
        )
        transported_decisions.append(HistoryDecision(new_key, decision.allowed))
    transported_decisions.sort(key=lambda d: d.key)
    return F4Object(
        n=obj.n,
        m=obj.m,
        targets=base.targets,
        horizon=obj.horizon,
        decisions=tuple(transported_decisions),
    )
