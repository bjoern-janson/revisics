from revisics_structure001.families.f2 import iter_f2, iter_partitions, normalize_partition


def test_partition_counts_are_bell_numbers_one_to_three():
    assert [len(list(iter_partitions(n))) for n in (1, 2, 3)] == [1, 2, 5]


def test_partition_enumerator_is_already_normalized_and_unique():
    parts = list(iter_partitions(3))
    assert len(parts) == len(set(parts))
    assert all(normalize_partition(p) == p for p in parts)


def test_f2_small_product_count():
    assert len(list(iter_f2(2, 1))) == 9 * 2
