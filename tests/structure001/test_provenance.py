from pathlib import Path

import pytest

from revisics_structure001.encoding import canonical_encode
from revisics_structure001.model import ControlFailure, ProvenanceEdge, TransportWitness
from revisics_structure001.provenance import (
    canonical_to_assay_edge,
    f5_recoding_edge,
    raw_to_canonical_edge,
    read_framed_records,
    write_canonical_ledger,
)


def make_edge(source: str, destination: str) -> ProvenanceEdge:
    return raw_to_canonical_edge(
        manifest_sha="m",
        implementation_id="i",
        family="F1",
        raw_id=source,
        canonical_id=destination,
        witness=TransportWitness((0,), (0,)),
    )


def test_provenance_ledger_roundtrip_sorts_records(tmp_path: Path):
    records = [canonical_encode(make_edge("b", "c")), canonical_encode(make_edge("a", "c"))]
    path = tmp_path / "L_P.bin"
    write_canonical_ledger(path, records)
    assert read_framed_records(path) == tuple(sorted(records))


def test_two_raw_sources_remain_two_edges(tmp_path: Path):
    records = [canonical_encode(make_edge("raw-a", "canon")), canonical_encode(make_edge("raw-b", "canon"))]
    path = tmp_path / "L_P.bin"
    write_canonical_ledger(path, records)
    loaded = read_framed_records(path)
    assert len(loaded) == 2
    assert loaded[0] != loaded[1]


def test_f5_edge_binds_all_required_identity_fields():
    witness = TransportWitness((1, 0), (0, 1))
    edge = f5_recoding_edge(
        manifest_sha="manifest",
        implementation_id="impl",
        base_id="base",
        instance_id="instance",
        recoding_id_value="recoding",
        witness=witness,
        identity_recoding=False,
    )
    assert edge.family == "F5"
    assert edge.base_id == "base"
    assert edge.instance_id == "instance"
    assert edge.recoding_id == "recoding"
    assert edge.transport == witness
    assert edge.identity_recoding is False


def test_canonical_to_assay_edge_has_no_fake_transport():
    edge = canonical_to_assay_edge("m", "i", "F1", "canon", "assay")
    assert edge.edge_kind == "CANONICAL_TO_ASSAY"
    assert edge.transport is None


def test_malformed_framing_is_control_failure(tmp_path: Path):
    path = tmp_path / "bad.bin"
    path.write_bytes(b"3:ab")
    with pytest.raises(ControlFailure) as exc:
        read_framed_records(path)
    assert exc.value.control_id == "LEDGER_FRAMING"
