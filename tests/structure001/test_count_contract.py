from dataclasses import replace

import pytest

from revisics_structure001.constants import (
    EXPECTED_ASSAY_CASES,
    EXPECTED_F1_CANONICAL,
    EXPECTED_F1_RAW,
    EXPECTED_F2_CANONICAL,
    EXPECTED_F2_RAW,
    EXPECTED_F3_CANONICAL,
    EXPECTED_F3_RAW,
    EXPECTED_F4_222_CANONICAL,
    EXPECTED_F4_222_VALID_LABELED,
    EXPECTED_F4_CANONICAL,
    EXPECTED_F4_NORMALIZED,
    EXPECTED_F5_CANONICAL_BASES,
    EXPECTED_F5_LABELED_BASES,
    EXPECTED_F5_RECODINGS,
)
from revisics_structure001.model import ControlFailure, TypedCountRecord
from revisics_structure001.replay import _check_production_counts, expected_counts_record


def bell(n: int) -> int:
    rows = [[0] * (n + 1) for _ in range(n + 1)]
    rows[0][0] = 1
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            rows[i][k] = rows[i - 1][k - 1] + k * rows[i - 1][k]
    return sum(rows[n])


def test_frozen_acceptance_table_is_exact():
    assert expected_counts_record() == TypedCountRecord(
        f1_raw=267137,
        f1_canonical=8344,
        f2_raw=1333172,
        f2_canonical=40839,
        f3_raw=2049144,
        f3_canonical=500079,
        f4_normalized=13056,
        f4_valid_labeled_222=10886,
        f4_canonical=2862,
        f4_canonical_222=2784,
        f5_labeled_bases=133899,
        f5_canonical_bases=11718,
        f5_recodings=139216,
        assay_cases=691340,
    )


def test_f1_raw_closed_form_matches_frozen_total():
    observed = sum((n + 1) ** (n * m) for n in range(1, 4) for m in range(1, 4))
    assert observed == EXPECTED_F1_RAW == 267137


def test_f2_raw_closed_form_matches_frozen_total():
    observed = sum(
        bell(n) * (n + 1) ** (n * m)
        for n in range(1, 4)
        for m in range(1, 4)
    )
    assert observed == EXPECTED_F2_RAW == 1333172


def test_f3_raw_closed_form_matches_frozen_total():
    observed = sum(
        (1 + 18 * n) ** (n * m)
        for n in range(1, 4)
        for m in range(1, 4)
        if n * m <= 4
    )
    assert observed == EXPECTED_F3_RAW == 2049144


def test_f5_labeled_base_closed_form_matches_frozen_total():
    observed = sum(
        (1 + 2 * n) ** (n * m)
        for n in (2, 3)
        for m in (2, 3)
        if n * m <= 6
    )
    assert observed == EXPECTED_F5_LABELED_BASES == 133899


def test_canonical_and_assay_constants_are_frozen_controls_not_derived_here():
    assert (
        EXPECTED_F1_CANONICAL,
        EXPECTED_F2_CANONICAL,
        EXPECTED_F3_CANONICAL,
        EXPECTED_F4_NORMALIZED,
        EXPECTED_F4_222_VALID_LABELED,
        EXPECTED_F4_CANONICAL,
        EXPECTED_F4_222_CANONICAL,
        EXPECTED_F5_CANONICAL_BASES,
        EXPECTED_F5_RECODINGS,
        EXPECTED_ASSAY_CASES,
    ) == (8344, 40839, 500079, 13056, 10886, 2862, 2784, 11718, 139216, 691340)


def test_production_checker_accepts_only_observed_record_equal_to_frozen_table():
    _check_production_counts(expected_counts_record())
    corrupted = replace(expected_counts_record(), f5_recodings=EXPECTED_F5_RECODINGS - 1)
    with pytest.raises(ControlFailure) as exc:
        _check_production_counts(corrupted)
    assert exc.value.control_id == "FROZEN_COUNT_MISMATCH"
