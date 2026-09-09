from revisics_structure001.canonical import all_witnesses, canonicalize
from revisics_structure001.encoding import canonical_encode
from revisics_structure001.families.f1 import transport_f1
from revisics_structure001.families.f2 import transport_f2
from revisics_structure001.families.f3 import transport_f3
from revisics_structure001.families.f4 import transport_f4
from revisics_structure001.model import (
    ExtensionKey,
    F1Object,
    F2Object,
    F3Object,
    F4Object,
    HistoryDecision,
    TransportWitness,
)


def test_f1_relabeling_canonicalizes_to_same_bytes():
    left = F1Object(n=2, m=1, targets=(1, 0))
    right = transport_f1(left, TransportWitness((1, 0), (0,)))
    assert canonicalize(left).canonical_bytes == canonicalize(right).canonical_bytes


def test_f2_partition_transport_preserves_canonical_form():
    left = F2Object(n=2, m=1, targets=(1, 0), partition=(0, 1))
    right = transport_f2(left, TransportWitness((1, 0), (0,)))
    assert canonicalize(left).canonical_bytes == canonicalize(right).canonical_bytes


def test_f3_canonicalization_is_idempotent():
    sample = F3Object(
        n=1,
        m=1,
        targets=(0,),
        costs=(1,),
        updates=(0, 1),
        regimes=((0, 1), (0, 2), (1, 1), (1, 2)),
    )
    first = canonicalize(sample)
    second = canonicalize(first.payload)
    assert first.canonical_bytes == second.canonical_bytes


def test_f4_transport_maps_entire_history_decision():
    obj = F4Object(
        n=2,
        m=2,
        targets=(1, None, None, 0),
        horizon=1,
        decisions=(HistoryDecision(ExtensionKey((0,), 0, 1), True),),
    )
    witness = TransportWitness((1, 0), (1, 0))
    transported = transport_f4(obj, witness)
    assert transported.decisions[0].key == ExtensionKey((1,), 1, 0)


def test_automorphism_tie_uses_minimum_transport_bytes():
    obj = F1Object(n=2, m=1, targets=(0, 1))
    rows = []
    for witness in all_witnesses(obj.n, obj.m):
        rows.append((
            canonical_encode(transport_f1(obj, witness)),
            canonical_encode(witness),
            witness,
        ))
    minimum_object = min(row[0] for row in rows)
    expected = min((r for r in rows if r[0] == minimum_object), key=lambda r: r[1])[2]
    assert canonicalize(obj).witness == expected


def test_order_of_witness_generation_does_not_change_minimum_pair():
    obj = F1Object(n=2, m=2, targets=(0, 1, 1, 0))
    pairs = [
        (canonical_encode(transport_f1(obj, w)), canonical_encode(w), w)
        for w in all_witnesses(obj.n, obj.m)
    ]
    assert min(pairs, key=lambda r: (r[0], r[1]))[:2] == min(reversed(pairs), key=lambda r: (r[0], r[1]))[:2]
