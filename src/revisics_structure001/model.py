from __future__ import annotations

from dataclasses import dataclass
from typing import Any


class ControlFailure(RuntimeError):
    def __init__(
        self,
        control_id: str,
        family: str | None = None,
        record_id: str | None = None,
        expected: str = "",
        observed: str = "",
    ) -> None:
        self.control_id = control_id
        self.family = family
        self.record_id = record_id
        self.expected = expected
        self.observed = observed
        super().__init__(
            f"{control_id}: family={family!r} record_id={record_id!r} "
            f"expected={expected!r} observed={observed!r}"
        )


@dataclass(frozen=True, slots=True)
class PreImplementationCustodyRecord:
    record_type: str
    record_version: str
    manifest_sha: str
    parent_scientific_contract_sha: str
    parent_candidate_ontology_sha: str
    implementation_branch_base_sha: str
    raw_constructions_generated: int
    canonical_worlds_generated: int
    f5_recoding_cases_generated: int
    candidate_case_outcomes_observed: int


@dataclass(frozen=True, slots=True)
class TransportWitness:
    phi_x: tuple[int, ...]
    phi_a: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class F1Object:
    n: int
    m: int
    targets: tuple[int | None, ...]


@dataclass(frozen=True, slots=True)
class F2Object:
    n: int
    m: int
    targets: tuple[int | None, ...]
    partition: tuple[int, ...]


@dataclass(frozen=True, slots=True)
class F3Object:
    n: int
    m: int
    targets: tuple[int | None, ...]
    costs: tuple[int, ...]
    updates: tuple[int | None, ...]
    regimes: tuple[tuple[int, int], ...]


@dataclass(frozen=True, slots=True, order=True)
class ExtensionKey:
    history: tuple[int, ...]
    action: int
    target: int

    @property
    def extended_history(self) -> tuple[int, ...]:
        return self.history + (self.action, self.target)


@dataclass(frozen=True, slots=True)
class HistoryDecision:
    key: ExtensionKey
    allowed: bool


@dataclass(frozen=True, slots=True)
class F4Object:
    n: int
    m: int
    targets: tuple[int | None, ...]
    horizon: int
    decisions: tuple[HistoryDecision, ...]


@dataclass(frozen=True, slots=True)
class F5BaseObject:
    n: int
    m: int
    targets: tuple[int | None, ...]
    costs: tuple[int, ...]
    horizon: int


@dataclass(frozen=True, slots=True)
class CanonicalizedObject:
    payload: Any
    canonical_bytes: bytes
    canonical_id: str
    witness: TransportWitness


@dataclass(frozen=True, slots=True)
class ValidityRecord:
    family: str
    record_id: str
    valid: bool
    reason_code: str
    expected: str
    observed: str


@dataclass(frozen=True, slots=True)
class RawConstructionRecord:
    family: str
    raw_id: str
    payload_bytes: bytes


@dataclass(frozen=True, slots=True)
class CanonicalWorldRecord:
    family: str
    canonical_id: str
    canonical_bytes: bytes


@dataclass(frozen=True, slots=True)
class ProvenanceEdge:
    manifest_sha: str
    implementation_id: str
    family: str
    source_id: str
    destination_id: str
    edge_kind: str
    transport: TransportWitness | None
    base_id: str | None
    instance_id: str | None
    recoding_id: str | None
    identity_recoding: bool | None


@dataclass(frozen=True, slots=True)
class F5RecodingRecord:
    base_id: str
    instance_id: str
    recoding_id: str
    witness: TransportWitness
    destination_bytes: bytes
    identity_recoding: bool


@dataclass(frozen=True, slots=True)
class TypedCountRecord:
    f1_raw: int = 0
    f1_canonical: int = 0
    f2_raw: int = 0
    f2_canonical: int = 0
    f3_raw: int = 0
    f3_canonical: int = 0
    f4_normalized: int = 0
    f4_valid_labeled_222: int = 0
    f4_canonical: int = 0
    f4_canonical_222: int = 0
    f5_labeled_bases: int = 0
    f5_canonical_bases: int = 0
    f5_recodings: int = 0
    assay_cases: int = 0


@dataclass(frozen=True, slots=True)
class AuditManifest:
    manifest_sha: str
    implementation_id: str
    raw_root: str
    canonical_root: str
    validity_root: str
    provenance_root: str
    f5_root: str
    counts: TypedCountRecord


@dataclass(frozen=True, slots=True)
class ControlRunResult:
    output_dir: str
    implementation_id: str
    counts: TypedCountRecord
    raw_root: str
    canonical_root: str
    validity_root: str
    provenance_root: str
    f5_root: str
    audit_digest: str
