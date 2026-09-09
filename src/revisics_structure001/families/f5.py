from itertools import permutations, product
from math import factorial
from typing import Iterator

from ..encoding import canonical_encode
from ..identity import content_id, sha256_hex
from ..model import ControlFailure, F5BaseObject, TransportWitness
from .f1 import iter_f1
from .f3 import edge_list


def iter_f5_labeled_bases(n: int, m: int) -> Iterator[F5BaseObject]:
    if not (2 <= n <= 3 and 2 <= m <= 3 and n * m <= 6):
        raise ControlFailure(
            control_id="F5_BOUND",
            family="F5",
            expected="2 <= n,m <= 3 and n*m <= 6",
            observed=f"n={n},m={m}",
        )
    for base in iter_f1(n, m):
        k = len(edge_list(n, m, base.targets))
        for costs in product((0, 1), repeat=k):
            yield F5BaseObject(
                n=n,
                m=m,
                targets=base.targets,
                costs=costs,
                horizon=2,
            )


def total_labeled_f5_bases_symbolic() -> int:
    return sum(
        (1 + 2 * n) ** (n * m)
        for n in (2, 3)
        for m in (2, 3)
        if n * m <= 6
    )


def iter_recoding_witnesses(n: int, m: int) -> Iterator[TransportWitness]:
    for phi_x in permutations(range(n)):
        for phi_a in permutations(range(m)):
            yield TransportWitness(tuple(phi_x), tuple(phi_a))


def _validate_witness(base: F5BaseObject, witness: TransportWitness) -> None:
    if tuple(sorted(witness.phi_x)) != tuple(range(base.n)):
        raise ControlFailure(
            control_id="F5_STATE_WITNESS_NOT_BIJECTION",
            family="F5",
            expected=str(tuple(range(base.n))),
            observed=str(witness.phi_x),
        )
    if tuple(sorted(witness.phi_a)) != tuple(range(base.m)):
        raise ControlFailure(
            control_id="F5_ACTION_WITNESS_NOT_BIJECTION",
            family="F5",
            expected=str(tuple(range(base.m))),
            observed=str(witness.phi_a),
        )


def transport_f5(base: F5BaseObject, witness: TransportWitness) -> F5BaseObject:
    _validate_witness(base, witness)
    old_edges = edge_list(base.n, base.m, base.targets)
    old_cost_by_edge = {edge: cost for edge, cost in zip(old_edges, base.costs, strict=True)}

    new_targets: list[int | None] = [None] * (base.n * base.m)
    transported_cost_by_edge: dict[tuple[int, int, int], int] = {}
    for old_edge, cost in old_cost_by_edge.items():
        old_x, old_a, old_y = old_edge
        new_x = witness.phi_x[old_x]
        new_a = witness.phi_a[old_a]
        new_y = witness.phi_x[old_y]
        new_targets[new_a * base.n + new_x] = new_y
        transported_cost_by_edge[(new_x, new_a, new_y)] = cost

    targets = tuple(new_targets)
    new_edges = edge_list(base.n, base.m, targets)
    costs = tuple(transported_cost_by_edge[edge] for edge in new_edges)
    return F5BaseObject(
        n=base.n,
        m=base.m,
        targets=targets,
        costs=costs,
        horizon=base.horizon,
    )


def instance_id(base: F5BaseObject) -> str:
    return content_id(base)


def recoding_id(base_id: str, witness: TransportWitness) -> str:
    return sha256_hex(canonical_encode((base_id, witness.phi_x, witness.phi_a)))


def expected_recoding_count_for_base(base: F5BaseObject) -> int:
    return factorial(base.n) * factorial(base.m)
