# pyright: basic
import random
import itertools
from typing import Any
from collections.abc import Sequence

mydeck: list[str] = [r + s for r in "23456789TJQKA" for s in "SHDC"]


def deal(numhands: int, n: int = 5, deck: list[str] = mydeck) -> list[list[str]]:
    random.shuffle(deck)
    return [deck[n * i : n * (i + 1)] for i in range(numhands)]


def poker(hands: Sequence[Sequence[str]]):
    "Return the best hand: poker([hand,...]) => hand"
    return max(hands, key=hand_rank)


def allmax(iterable, key=None) -> list[Any]:
    "Return a list of all items equal to the max of the iterable."
    key = key or (lambda x: x)
    m = max(map(lambda x: key(x)[0], iterable))
    return [x for x in iterable if key(x)[0] == m]


def straight(ranks: Sequence[int]) -> bool:
    """
    Returns True if the ranks is a straight
    """
    return ranks == list(range(ranks[0], ranks[-1] - 1, -1))


def flush(hand: Sequence[str]):
    """
    Returns True if the hand is a flush
    """
    suits = [s for _, s in hand]
    return len(set(suits)) == 1


def kind(n: int, ranks: Sequence[int]):
    """
    Returns the first rank that the hand has exactly n of.
    For A hand with 4 sevens this function would return 7.
    """
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks: Sequence[int]) -> tuple[int, ...] | None:
    """
    if there is a two pair, this function returns their corresponding
    ranks as a tuple. e.g., a hand with 2 twos and 2 fours would cause
    this function to return (4, 2). Returns None otherwise.
    """
    pairs = set(list(filter(lambda x: ranks.count(x) == 2, ranks)))
    if len(pairs) == 2:
        return tuple(pairs)
    return None


def card_ranks(cards: Sequence[str]) -> Sequence[int]:
    """
    Returns an ORDERED list of the ranks in a hand (where the order goes from
    highest to lowest rank)
    """
    ranks = ["--23456789TJQKA".index(r) for r, _ in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def hand_rank(hand: Sequence[str]):
    """
    Return a value indicating the ranking of a hand.
    """
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):  # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):  # four of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):  # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, sorted(ranks))
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):  # three of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):  # two pairs
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):  # one pair
        return (1, kind(2, ranks), ranks)
    else:  # high card
        return (0, max(ranks), ranks)


count_rankings = {
    (5,): 10,
    (4, 1): 7,
    (3, 2): 6,
    (3, 1, 1): 3,
    (2, 2, 1): 2,
    (2, 1, 1, 1): 1,
    (1, 1, 1, 1, 1): 0,
}


def better_hand_rank(hand: Sequence[str]):
    # "Return a value indicating how high the hand ranks."
    # counts is the count of each rank; ranks lists corresponding ranks
    # e.g., '7 T 7 9 7' => counts = (3, 1, 1); ranks = (7, 10, 9)
    groups = group(["--23456789TJQKA".index(r) for r, _ in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for _, s in hand])) == 1
    return max(count_rankings[counts], 4 * straight + 5 * flush), ranks


def group(items):
    "Return a list of [(count, x)...], highest count first, then highest x first"
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)


def unzip(pairs) -> zip[tuple[Any, ...]]:
    return zip(*pairs)


def test():
    """
    Test cases for the functions in poker program
    """
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    # tp = "5S 5D 9H 9C 6S".split()  # Two Pairs
    s1 = "A2 2S 3S 4S 5C".split()  # A-5 Straight
    s2 = "2C 3C 4C 5S 6S".split()  # 2-6 Straight
    ah = "AS 2S 3S 4S 6C".split()  # A high
    sh = "2S 3S 4S 6C 7D".split()  # 7 high
    fkranks = card_ranks(sf)
    # tpranks = card_ranks(tp)

    assert poker([s1, s2, ah, sh]) == s2

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    assert card_ranks(sf) == range(10, 5, -1)
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]
    assert straight([9, 8, 7, 6, 5]) is True
    assert straight([9, 8, 8, 6, 5]) is False
    assert flush(sf) is True
    assert flush(fh) is False
    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99 * [fh]) == sf
    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)


def best_hand(hand):
    "From a 7-card hand, return the best 5 card hand."
    pass


def test_best_hand():
    assert sorted(best_hand("6C 7C 8C 9C TC 5C JS".split())) == [
        "6C",
        "7C",
        "8C",
        "9C",
        "TC",
    ]
    assert sorted(best_hand("TD TC TH 7C 7D 8C 8S".split())) == [
        "8C",
        "8S",
        "TC",
        "TD",
        "TH",
    ]
    assert sorted(best_hand("JD TC TH 7C 7D 7S 7H".split())) == [
        "7C",
        "7D",
        "7H",
        "7S",
        "JD",
    ]
    return "test_best_hand passes"


print(test_best_hand())
