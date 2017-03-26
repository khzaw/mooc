import random

def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first."
    ranks = sorted(('xx23456789TJQKA'.index(r) for r,s in cards), reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks

def straight(ranks):
    "Return True if the ordered ranks from a 5-card straight."
    return (max(ranks) - min(ranks) == 4) and (len(set(ranks)) == 5)

def flush(hand):
    "Return True if all the cards have the same suit"
    return len(set([s for r, s in hand])) == 1

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    two_pairs = set(r for r in ranks if ranks.count(r) == 2)
    if len(two_pairs) == 2:
        two_pairs = sorted(list(two_pairs), reverse=True)
        return (two_pairs[0], two_pairs[1])
    return None

def kind(n, ranks):
    """ Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None

def hand_rank(hand):
    "Return a value indicating the ranking of a hand."
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):                 # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                                # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):             # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2), ranks)
    else:
        return (0, ranks)

def group(items):
    "Return a list of [(count, x) ..], highest count first, then highest x first."
    groups = [(items.count(x), x) for x in set(items)]
    return sorted(groups, reverse=True)

def unzip(pairs):
    return zip(*pairs)

def better_hand_rank(hand):
    "Return a value indicating how high the hand ranks"
    groups = group(['xx23456789JQKA'.index(r) for r,s in hand])
    counts, ranks = unzip(groups)
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)

    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([s for r,s in hand])) == 1
    return (9 if (5,) == counts else
            8 if straight and flush else
            7 if (4, 1) == counts else
            6 if (3, 2) == counts else
            5 if flush else
            4 if straight else
            3 if (3, 1, 1) == counts else
            2 if (2, 1, 1) == counts else
            1 if (2, 1, 1, 1) == counts else
            0, ranks)

def allmax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable"
    key = key or (lambda x: x)
    maxitem = max(iterable, key=key)
    return [item for sublist in filter(lambda x: x == maxitem, iterable) for item in sublist]

def poker(hands):
    "Return the best hand: poker([hand, ...]) => [hand, ...]"
    return allmax(hands, key=hand_rank)

def deal(numhands, n=5, deck=[r+s for r in '23456789JQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]


def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()   # straight flush
    fk = "9D 9H 9S 9C 7D".split()   # four of a kind
    fh = "TD TC TH 7C 7D".split()   # full house
    tp = "5S 5D 9H 9C 6S".split()   # two pair
    s1 = "AS 2S 3S 4S 5C".split()   # A-5 straight
    s2 = "2C 3C 4C 5S 6S".split()   # 2-6 straight
    ah = "AS 2S 3S 4S 6C".split()   # A high
    sh = "2S 3S 4S 6C 7D".split()   # 7 high
    assert poker([sf, fk, fh]) == sf

    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fk]) == sf

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    assert kind(4, card_ranks(fk)) == 9
    assert kind(3, card_ranks(fh)) == 10

    return "tests pass"
# print test()
