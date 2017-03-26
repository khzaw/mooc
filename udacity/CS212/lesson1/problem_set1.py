from poker import *
import itertools


def best_hand(hand):
    "From a 7-cardhand, return the 5 card hand."
    return max(itertools.combinations(hand, 5), key=hand_rank)

def best_wild_hand(hand):
    """
    Deck adds two cards
    # '?B': black joker; can be used as any black card(S or C)
    # '?R': red joker; can be used as any red card (H or D)
    """
    "Try all values for jokers in all 5-card selections."
    pass


def test_best_hand():
    assert (sorted(best_hand('6C 7C 8C 9C TC 5C JS'.split()))
            == ['6C', '7C', '8C', '9C', 'TC'])
    assert (sorted(best_hand('TD TC TH 7C 7D 8C 8S'.split()))
            == ['8C', '8S', 'TC', 'TD', 'TH'])
    assert (sorted(best_hand('JD TC TH 7C 7D 7S 7H'.split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    assert (sorted(best_wild_hand('6C 7C 8C TC 5C ?B'.split()))
            == ['7C', '8C', '9C', 'JC', 'TC'])
    assert (sorted(best_wild_hand('TD TC 5H 5C 7C ?R ?B'.split()))
            == ['7C' 'TC', 'TD', 'TH', 'TS'])
    assert (sorted(best_wild_hand('JD TC TH 7C 7D 7S 7H'.split()))
            == ['7C', '7D', '7H', '7S', 'JD'])
    return 'test_best_hand passes'

print test_best_hand()
