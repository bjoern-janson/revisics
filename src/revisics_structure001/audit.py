from __future__ import annotations

from hashlib import sha256
from typing import Iterable

from .encoding import canonical_encode
from .identity import sha256_hex
from .model import AuditManifest, TypedCountRecord


def _tree_digest(records: tuple[bytes, ...], ledger_tag: str) -> bytes:
    tag = ledger_tag.encode("ascii")
    if not records:
        return sha256(b"structure001-empty-v1\0" + tag).digest()
    level = [
        sha256(b"structure001-leaf-v1\0" + tag + b"\0" + record).digest()
        for record in records
    ]
    while len(level) > 1:
        if len(level) % 2:
            level.append(level[-1])
        level = [
            sha256(b"structure001-node-v1\0" + level[i] + level[i + 1]).digest()
            for i in range(0, len(level), 2)
        ]
    return level[0]


def merkle_root(records: Iterable[bytes], ledger_tag: str) -> str:
    ordered = tuple(sorted(records))
    tag = ledger_tag.encode("ascii")
    tree_digest = _tree_digest(ordered, ledger_tag)
    return sha256(
        b"structure001-root-v2\0"
        + tag
        + b"\0"
        + str(len(ordered)).encode("ascii")
        + b"\0"
        + tree_digest
    ).hexdigest()


def build_audit_manifest(
    manifest_sha: str,
    implementation_id: str,
    raw_root: str,
    canonical_root: str,
    validity_root: str,
    provenance_root: str,
    f5_root: str,
    counts: TypedCountRecord,
) -> AuditManifest:
    return AuditManifest(
        manifest_sha=manifest_sha,
        implementation_id=implementation_id,
        raw_root=raw_root,
        canonical_root=canonical_root,
        validity_root=validity_root,
        provenance_root=provenance_root,
        f5_root=f5_root,
        counts=counts,
    )


def audit_bundle_digest(manifest: AuditManifest) -> str:
    return sha256_hex(canonical_encode(manifest))
