from revisics_structure001.audit import (
    audit_bundle_digest,
    build_audit_manifest,
    merkle_root,
)
from revisics_structure001.model import TypedCountRecord


def test_ledger_root_is_order_independent_after_canonical_sort():
    left = merkle_root((b"b", b"a", b"c"), "L_P")
    right = merkle_root((b"c", b"b", b"a"), "L_P")
    assert left == right


def test_ledger_root_binds_exact_record_count():
    assert merkle_root((b"a", b"b", b"c"), "L_P") != merkle_root(
        (b"a", b"b", b"c", b"c"), "L_P"
    )


def test_ledger_tag_domain_separates_roots():
    assert merkle_root((b"a",), "L_R") != merkle_root((b"a",), "L_P")


def test_audit_bundle_binds_provenance_root():
    counts = TypedCountRecord(f1_raw=1)
    common = dict(
        manifest_sha="manifest",
        implementation_id="impl",
        raw_root="r",
        canonical_root="c",
        validity_root="v",
        f5_root="f5",
        counts=counts,
    )
    left = build_audit_manifest(provenance_root="p-left", **common)
    right = build_audit_manifest(provenance_root="p-right", **common)
    assert audit_bundle_digest(left) != audit_bundle_digest(right)


def test_empty_ledger_root_is_deterministic():
    assert merkle_root((), "L_R") == merkle_root((), "L_R")
