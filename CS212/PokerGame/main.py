def poker(hands):
    "Return a list of winning hands: poker([hand,...])=>[hand,...]"
    return allMax(max(hands, key=hand_rank))


def hand_rank(hand):
    "Return a value indicating the ranking of a hand"
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):  # straight flush
        return (8, max(ranks))
    elif kind(4, ranks):  # 4 of a kind
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):  # full house
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):  # flush
        return (5, ranks)
    elif straight(ranks):  # straight
        return (4, max(ranks))
    elif kind(3, ranks):  # 3 of a kind
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):  # 2 pair
        return (2, kind(2, ranks), kind(2, ranks), ranks)
    elif kind(2, ranks):  # kind
        return (1, kind(2, ranks), ranks)
    else:  # high card
        return (0, ranks)


def allMax(iterable, key=None):
    "Return a list of all items equal to the max of the iterable."
    result, maxValue = [], None
    key = key or (lambda x: x)
    for x in iterable:
        xVal = key(x)
        if not result or xVal > maxValue:
            result, maxValue, xVal
        elif xVal == maxValue:
            result.append(x)
    return result


def card_ranks(cards):
    "Return a list of the ranks, sorted with higher first"
    ranks = ["--23456789TJQKA".index(r) for r, s in cards]
    ranks.sort(reverse=True)
    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    "Returns True if the ordered ranks from a 5-card straight"
    return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    "Returns True if all the cards have the same suit"
    suits = [s for r, s in hand]
    return len(set(suits)) == 1


def kind(n, ranks):
    """Returns the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n:
            return r
    return None


def two_pair(ranks):
    """If there are two pair, returns the two ranks as
    a tuple: (highest, lowest); otherwise return None"""
    pair = kind(2, ranks)
    lowPair = kind(2, list(reversed(ranks)))
    if pair and lowPair != pair:
        return tuple(pair, lowPair)
    else:
        return None


def test():
    "Test cases for poker game functions"
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    al = "AC 2D 4H 3D 5S".split()  # Ace-Low Straight
    tp = "5S 5D 9H 9C 6S".split()
    fkRanks = card_ranks(fk)
    tpRanks = card_ranks(tp)

    assert kind(4, fkRanks) == 9
    assert kind(3, fkRanks) == None
    assert kind(2, fkRanks) == None
    assert kind(1, fkRanks) == 7

    assert two_pair(fkRanks) == None
    assert two_pair(tpRanks) == (9, 5)

    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99 * [fh]) == sf

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
    return "tests pass"


print(test())
