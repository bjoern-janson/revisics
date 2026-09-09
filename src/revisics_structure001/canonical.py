from itertools import permutations
from typing import Iterator

from .encoding import canonical_encode
from .families.f1 import transport_f1
from .families.f2 import transport_f2
from .families.f3 import transport_f3
from .families.f4 import transport_f4
from .families.f5 import transport_f5
from .identity import sha256_hex
from .model import (
    CanonicalizedObject,
    ControlFailure,
    F1Object,
    F2Object,
    F3Object,
    F4Object,
    F5BaseObject,
    TransportWitness,
)


def all_witnesses(n: int, m: int) -> Iterator[TransportWitness]:
    for phi_x in permutations(range(n)):
        for phi_a in permutations(range(m)):
            yield TransportWitness(tuple(phi_x), tuple(phi_a))


def family_transport(obj, witness: TransportWitness):
    if isinstance(obj, F1Object):
        return transport_f1(obj, witness)
    if isinstance(obj, F2Object):
        return transport_f2(obj, witness)
    if isinstance(obj, F3Object):
        return transport_f3(obj, witness)
    if isinstance(obj, F4Object):
        return transport_f4(obj, witness)
    if isinstance(obj, F5BaseObject):
        return transport_f5(obj, witness)
    raise ControlFailure(
        control_id="CANONICAL_UNSUPPORTED_FAMILY",
        expected="F1-F5 family object",
        observed=type(obj).__qualname__,
    )


def canonicalize(obj) -> CanonicalizedObject:
    best = None
    for witness in all_witnesses(obj.n, obj.m):
        transported = family_transport(obj, witness)
        object_bytes = canonical_encode(transported)
        transport_bytes = canonical_encode(witness)
        row = (object_bytes, transport_bytes, transported, witness)
        if best is None or (row[0], row[1]) < (best[0], best[1]):
            best = row
    if best is None:
        raise ControlFailure(
            control_id="CANONICAL_NO_WITNESS",
            expected="at least identity witness",
            observed=f"n={obj.n},m={obj.m}",
        )
    object_bytes, _transport_bytes, payload, witness = best
    return CanonicalizedObject(
        payload=payload,
        canonical_bytes=object_bytes,
        canonical_id=sha256_hex(object_bytes),
        witness=witness,
    )
