from hashlib import sha256

from .encoding import canonical_encode


def sha256_hex(data: bytes) -> str:
    return sha256(data).hexdigest()


def content_id(value: object) -> str:
    return sha256_hex(canonical_encode(value))
