from dataclasses import FrozenInstanceError
import pytest

from revisics_structure001.encoding import canonical_encode
from revisics_structure001.model import ControlFailure, F1Object, TransportWitness


def test_f1_object_is_immutable():
    obj = F1Object(n=1, m=1, targets=(None,))
    with pytest.raises(FrozenInstanceError):
        obj.n = 2


def test_control_failure_constructor_retains_fields():
    err = ControlFailure(control_id="X", expected="a", observed="b")
    assert err.control_id == "X"
    assert err.expected == "a"
    assert err.observed == "b"


def test_frozenset_encoding_is_order_independent():
    assert canonical_encode(frozenset({3, 1, 2})) == canonical_encode(frozenset({2, 3, 1}))


def test_transport_encoding_uses_explicit_image_sequences():
    left = TransportWitness(phi_x=(1, 0), phi_a=(0,))
    right = TransportWitness(phi_x=(1, 0), phi_a=(0,))
    assert canonical_encode(left) == canonical_encode(right)


def test_unsupported_object_fails_instead_of_repr_fallback():
    with pytest.raises(ControlFailure) as exc:
        canonical_encode(object())
    assert exc.value.control_id == "ENCODING_UNSUPPORTED"
