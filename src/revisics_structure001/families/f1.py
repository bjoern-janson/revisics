from itertools import product
from typing import Iterator

from ..model import ControlFailure, F1Object


def iter_f1(n: int, m: int) -> Iterator[F1Object]:
    if not (1 <= n <= 3 and 1 <= m <= 3):
        raise ControlFailure(
            control_id="F1_BOUND",
            family="F1",
            expected="1 <= n,m <= 3",
            observed=f"n={n},m={m}",
        )
    alphabet = (None,) + tuple(range(n))
    for targets in product(alphabet, repeat=n * m):
        yield F1Object(n=n, m=m, targets=targets)


def validate_transport_witness(n: int, m: int, witness):
    if tuple(sorted(witness.phi_x)) != tuple(range(n)):
        raise ControlFailure(
            control_id="STATE_WITNESS_NOT_BIJECTION",
            expected=str(tuple(range(n))),
            observed=str(witness.phi_x),
        )
    if tuple(sorted(witness.phi_a)) != tuple(range(m)):
        raise ControlFailure(
            control_id="ACTION_WITNESS_NOT_BIJECTION",
            expected=str(tuple(range(m))),
            observed=str(witness.phi_a),
        )


def transport_f1(obj, witness):
    validate_transport_witness(obj.n, obj.m, witness)
    targets: list[int | None] = [None] * (obj.n * obj.m)
    for a in range(obj.m):
        for x in range(obj.n):
            y = obj.targets[a * obj.n + x]
            if y is not None:
                targets[witness.phi_a[a] * obj.n + witness.phi_x[x]] = witness.phi_x[y]
    return F1Object(n=obj.n, m=obj.m, targets=tuple(targets))
