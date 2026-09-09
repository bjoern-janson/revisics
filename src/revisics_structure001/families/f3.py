from itertools import product
from typing import Iterator

from ..model import ControlFailure, F3Object
from .f1 import iter_f1

REGIMES = ((0, 1), (0, 2), (1, 1), (1, 2))


def edge_list(
    n: int,
    m: int,
    targets: tuple[int | None, ...],
) -> tuple[tuple[int, int, int], ...]:
    edges: list[tuple[int, int, int]] = []
    for a in range(m):
        for x in range(n):
            target = targets[a * n + x]
            if target is not None:
                edges.append((x, a, target))
    return tuple(edges)


def iter_decorations(
    edge_count: int,
) -> Iterator[tuple[tuple[int, ...], tuple[int | None, ...]]]:
    for costs in product((0, 1), repeat=edge_count):
        for updates in product((None, 0, 1), repeat=2 * edge_count):
            yield costs, updates


def iter_f3(n: int, m: int) -> Iterator[F3Object]:
    if not (1 <= n <= 3 and 1 <= m <= 3 and n * m <= 4):
        raise ControlFailure(
            control_id="F3_BOUND",
            family="F3",
            expected="1 <= n,m <= 3 and n*m <= 4",
            observed=f"n={n},m={m}",
        )
    for base in iter_f1(n, m):
        k = len(edge_list(n, m, base.targets))
        for costs, updates in iter_decorations(k):
            yield F3Object(
                n=n,
                m=m,
                targets=base.targets,
                costs=costs,
                updates=updates,
                regimes=REGIMES,
            )


def path_is_admissible(
    obj: F3Object,
    initial_resource: int,
    horizon: int,
    edge_indices: tuple[int, ...],
) -> bool:
    if initial_resource not in (0, 1) or horizon not in (1, 2):
        return False
    if len(edge_indices) > horizon:
        return False
    edges = edge_list(obj.n, obj.m, obj.targets)
    k = len(edges)
    resource = initial_resource
    previous_target: int | None = None
    for position, edge_index in enumerate(edge_indices):
        if not (0 <= edge_index < k):
            return False
        source, _action, target = edges[edge_index]
        if position and source != previous_target:
            return False
        update = obj.updates[resource * k + edge_index]
        if update is None:
            return False
        resource = update
        previous_target = target
    return True


def transport_f3(obj, witness):
    from .f1 import transport_f1, validate_transport_witness
    from ..model import F1Object

    validate_transport_witness(obj.n, obj.m, witness)
    base = transport_f1(F1Object(obj.n, obj.m, obj.targets), witness)
    old_edges = edge_list(obj.n, obj.m, obj.targets)
    new_edges = edge_list(obj.n, obj.m, base.targets)
    new_index = {edge: index for index, edge in enumerate(new_edges)}
    k = len(old_edges)
    new_costs = [0] * k
    new_updates: list[int | None] = [None] * (2 * k)
    for old_index, (x, a, y) in enumerate(old_edges):
        transported_edge = (witness.phi_x[x], witness.phi_a[a], witness.phi_x[y])
        ni = new_index[transported_edge]
        new_costs[ni] = obj.costs[old_index]
        for resource in (0, 1):
            new_updates[resource * k + ni] = obj.updates[resource * k + old_index]
    return F3Object(
        n=obj.n,
        m=obj.m,
        targets=base.targets,
        costs=tuple(new_costs),
        updates=tuple(new_updates),
        regimes=obj.regimes,
    )
