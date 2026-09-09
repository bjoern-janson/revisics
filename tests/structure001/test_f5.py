from revisics_structure001.encoding import canonical_encode
from revisics_structure001.families.f5 import (
    iter_f5_labeled_bases,
    iter_recoding_witnesses,
    recoding_id,
    total_labeled_f5_bases_symbolic,
    transport_f5,
)
from revisics_structure001.identity import content_id
from revisics_structure001.model import F5BaseObject, TransportWitness


def test_two_by_two_has_four_recoding_witnesses():
    assert len(list(iter_recoding_witnesses(2, 2))) == 4


def test_distinct_maps_remain_distinct_when_destination_bytes_match():
    base = F5BaseObject(
        n=2,
        m=2,
        targets=(0, 1, 0, 1),
        costs=(0, 0, 0, 0),
        horizon=2,
    )
    identity = TransportWitness((0, 1), (0, 1))
    swap_states = TransportWitness((1, 0), (0, 1))
    assert canonical_encode(transport_f5(base, identity)) == canonical_encode(transport_f5(base, swap_states))
    base_id = content_id(base)
    assert recoding_id(base_id, identity) != recoding_id(base_id, swap_states)


def test_small_f5_base_count_matches_closed_form():
    assert len(list(iter_f5_labeled_bases(2, 2))) == (1 + 2 * 2) ** 4


def test_symbolic_f5_labeled_base_total_is_frozen_count():
    assert total_labeled_f5_bases_symbolic() == 133899
