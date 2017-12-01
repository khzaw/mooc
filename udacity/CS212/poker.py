def poker(hands):
    """
    Return the best hand: poker([hand,...]) => hand
    """
    return max(hands, key=hand_rank)


def straight(ranks):
    """
    Returns True if the ranks is a straight
    """
    return ranks == list(range(ranks[0], ranks[-1]-1, -1))


def flush(hand):
    """
    Returns True if the hand is a flush
    """
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    """
    Returns the first rank that the hand has exactly n of.
    For A hand with 4 sevens this function would return 7.
    """
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """
    if there is a two pair, this function returns their corresponding
    ranks as a tuple. e.g., a hand with 2 twos and 2 fours would cause
    this function to return (4, 2). Returns None otherwise.
    """
    pairs = set(list(filter(lambda x: ranks.count(x) == 2, ranks)))
    if len(pairs) == 2:
        return tuple(pairs)
    return None

# def two_pair(ranks):
#     pair = kind(2, ranks)
#     lowpair = kind(2, list(reversed(ranks)))
#     if pair and lowpair != pair:
#         return (pair, lowpair)
#     else:
#         return None


def card_ranks(cards):
    """
    Returns an ORDERED list of the ranks in a hand (where the order goes from
    highest to lowest rank)
    """
    ranks = ['--23456789TJQKA'.index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def hand_rank(hand):
    """
    Return a value indicating the ranking of a hand.
    """
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):     # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):                 # four of a kind
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


def test():
    """
    Test cases for the functions in poker program
    """
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    tp = "5S 5D 9H 9C 6S".split()  # Two Pairs
    s1 = "A2 2S 3S 4S 5C".split()  # A-5 Straight
    s2 = "2C 3C 4C 5S 6S".split()  # 2-6 Straight
    ah = "AS 2S 3S 4S 6C".split()  # A high
    sh = "2S 3S 4S 6C 7D".split()  # 7 high
    fkranks = card_ranks(sf)
    tpranks = card_ranks(tp)

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
