import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_exact_reference_runtime():
    assert sys.version_info[:3] == (3, 13, 5)


def test_preimplementation_record_asserts_all_four_zero_states():
    path = ROOT / "experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt"
    lines = path.read_text(encoding="utf-8").splitlines()
    assert "raw_constructions_generated=0" in lines
    assert "canonical_worlds_generated=0" in lines
    assert "f5_recoding_cases_generated=0" in lines
    assert "candidate_case_outcomes_observed=0" in lines


def test_preimplementation_record_binds_frozen_scientific_shas():
    lines = set((ROOT / "experiments/STRUCTURE-001/implementation-controls/PRE_IMPLEMENTATION_CUSTODY_V1.txt").read_text(encoding="utf-8").splitlines())
    assert "manifest_sha=f5874063b06997f49f3ee80d291de879c8d27a7f" in lines
    assert "parent_scientific_contract_sha=9711a6dd1b14ade10fd43a03c424ddc840cc565e" in lines
    assert "parent_candidate_ontology_sha=7d1e3cf3bd61b212d6131a7e1d98c10f401aa95d" in lines
