from __future__ import annotations

from pathlib import Path
from typing import Iterable

from .model import ControlFailure, ProvenanceEdge, TransportWitness


def _frame_record(payload: bytes) -> bytes:
    return str(len(payload)).encode("ascii") + b":" + payload


def write_canonical_ledger(path: Path, records: Iterable[bytes]) -> None:
    ordered = sorted(records)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as handle:
        for record in ordered:
            handle.write(_frame_record(record))


def read_framed_records(path: Path) -> tuple[bytes, ...]:
    data = path.read_bytes()
    out: list[bytes] = []
    cursor = 0
    length = len(data)
    while cursor < length:
        colon = data.find(b":", cursor)
        if colon < 0:
            raise ControlFailure(
                control_id="LEDGER_FRAMING",
                expected="ASCII decimal length followed by ':'",
                observed=f"missing colon at byte {cursor}",
            )
        prefix = data[cursor:colon]
        if not prefix or any(byte < ord("0") or byte > ord("9") for byte in prefix):
            raise ControlFailure(
                control_id="LEDGER_FRAMING",
                expected="ASCII decimal record length",
                observed=prefix.decode("ascii", errors="replace"),
            )
        record_length = int(prefix.decode("ascii"))
        start = colon + 1
        end = start + record_length
        if end > length:
            raise ControlFailure(
                control_id="LEDGER_FRAMING",
                expected=f"{record_length} payload bytes",
                observed=f"{length - start} payload bytes remain",
            )
        out.append(data[start:end])
        cursor = end
    return tuple(out)


def raw_to_canonical_edge(
    manifest_sha: str,
    implementation_id: str,
    family: str,
    raw_id: str,
    canonical_id: str,
    witness: TransportWitness,
) -> ProvenanceEdge:
    return ProvenanceEdge(
        manifest_sha=manifest_sha,
        implementation_id=implementation_id,
        family=family,
        source_id=raw_id,
        destination_id=canonical_id,
        edge_kind="RAW_TO_CANONICAL",
        transport=witness,
        base_id=None,
        instance_id=None,
        recoding_id=None,
        identity_recoding=None,
    )


def canonical_to_assay_edge(
    manifest_sha: str,
    implementation_id: str,
    family: str,
    canonical_id: str,
    assay_id: str,
) -> ProvenanceEdge:
    return ProvenanceEdge(
        manifest_sha=manifest_sha,
        implementation_id=implementation_id,
        family=family,
        source_id=canonical_id,
        destination_id=assay_id,
        edge_kind="CANONICAL_TO_ASSAY",
        transport=None,
        base_id=None,
        instance_id=None,
        recoding_id=None,
        identity_recoding=None,
    )


def f5_recoding_edge(
    manifest_sha: str,
    implementation_id: str,
    base_id: str,
    instance_id: str,
    recoding_id_value: str,
    witness: TransportWitness,
    identity_recoding: bool,
) -> ProvenanceEdge:
    return ProvenanceEdge(
        manifest_sha=manifest_sha,
        implementation_id=implementation_id,
        family="F5",
        source_id=base_id,
        destination_id=recoding_id_value,
        edge_kind="F5_RECODING",
        transport=witness,
        base_id=base_id,
        instance_id=instance_id,
        recoding_id=recoding_id_value,
        identity_recoding=identity_recoding,
    )
