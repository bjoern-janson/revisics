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
