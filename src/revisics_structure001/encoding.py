from __future__ import annotations

from dataclasses import fields, is_dataclass

from .constants import ENCODING_VERSION
from .model import ControlFailure


def frame(tag: bytes, payload: bytes) -> bytes:
    return tag + b":" + str(len(payload)).encode("ascii") + b":" + payload


def _sequence(tag: bytes, values: tuple[object, ...]) -> bytes:
    payload = b"".join(frame(b"item", canonical_encode(v)) for v in values)
    return frame(tag, payload)


def canonical_encode(value: object) -> bytes:
    if value is None:
        return frame(b"none", b"")
    if isinstance(value, bool):
        return frame(b"bool", b"1" if value else b"0")
    if isinstance(value, int):
        return frame(b"int", str(value).encode("ascii"))
    if isinstance(value, str):
        return frame(b"str", value.encode("utf-8"))
    if isinstance(value, bytes):
        return frame(b"bytes", value)
    if isinstance(value, tuple):
        return _sequence(b"tuple", value)
    if isinstance(value, frozenset):
        encoded = tuple(sorted(canonical_encode(v) for v in value))
        payload = b"".join(frame(b"item", item) for item in encoded)
        return frame(b"frozenset", payload)
    if is_dataclass(value) and not isinstance(value, type):
        type_tag = f"{value.__class__.__module__}.{value.__class__.__qualname__}".encode("utf-8")
        body = [frame(b"version", ENCODING_VERSION.encode("ascii")), frame(b"type", type_tag)]
        for f in fields(value):
            field_payload = frame(b"name", f.name.encode("utf-8")) + frame(
                b"value", canonical_encode(getattr(value, f.name))
            )
            body.append(frame(b"field", field_payload))
        return frame(b"dataclass", b"".join(body))
    raise ControlFailure(
        control_id="ENCODING_UNSUPPORTED",
        expected="supported canonical type",
        observed=f"type={type(value).__module__}.{type(value).__qualname__}",
    )
