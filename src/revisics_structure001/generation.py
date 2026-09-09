from typing import Iterator

from .families.f1 import iter_f1
from .families.f2 import iter_f2


def iter_raw(family: str) -> Iterator[object]:
    if family == "F1":
        for n in range(1, 4):
            for m in range(1, 4):
                yield from iter_f1(n, m)
        return
    if family == "F2":
        for n in range(1, 4):
            for m in range(1, 4):
                yield from iter_f2(n, m)
        return
    raise ValueError(f"family not implemented: {family}")
