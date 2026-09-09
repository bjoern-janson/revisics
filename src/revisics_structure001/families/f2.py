from typing import Iterator

from ..model import ControlFailure, F1Object, F2Object
from .f1 import iter_f1


def normalize_partition(labels: tuple[int, ...]) -> tuple[int, ...]:
    mapping: dict[int, int] = {}
    next_label = 0
    out: list[int] = []
    for label in labels:
        if label not in mapping:
            mapping[label] = next_label
            next_label += 1
        out.append(mapping[label])
    return tuple(out)


def iter_partitions(n: int) -> Iterator[tuple[int, ...]]:
    if n < 1:
        raise ControlFailure(
            control_id="F2_PARTITION_BOUND",
            family="F2",
            expected="n >= 1",
            observed=f"n={n}",
        )

    def rec(prefix: tuple[int, ...]) -> Iterator[tuple[int, ...]]:
        if len(prefix) == n:
            yield prefix
            return
        maximum = max(prefix)
        for label in range(maximum + 2):
            yield from rec(prefix + (label,))

    yield from rec((0,))


def iter_f2(n: int, m: int) -> Iterator[F2Object]:
    partitions = tuple(iter_partitions(n))
    for base in iter_f1(n, m):
        for partition in partitions:
            yield F2Object(n=n, m=m, targets=base.targets, partition=partition)


def transport_f2(obj, witness):
    from .f1 import transport_f1, validate_transport_witness

    validate_transport_witness(obj.n, obj.m, witness)
    base = transport_f1(F1Object(obj.n, obj.m, obj.targets), witness)
    labels = [0] * obj.n
    for old_x, block in enumerate(obj.partition):
        labels[witness.phi_x[old_x]] = block
    return F2Object(
        n=obj.n,
        m=obj.m,
        targets=base.targets,
        partition=normalize_partition(tuple(labels)),
    )
