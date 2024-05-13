import sys


def getType1(hand: str) -> int:
    """Returns the type of a hand given the input integer
    0: high card
    1: one pair
    2: two pair
    3: three of a kind
    4: full house (triple and pair)
    5: four of a kind
    6: five of a kind
    """
    tracker = {}
    for ch in hand:
        if ch in tracker:
            tracker[ch] += 1
        else:
            tracker[ch] = 1

    if len(tracker) == 1:
        return 6

    if len(tracker) == 2:
        # four of a kind or full house
        for v in tracker.values():
            if v == 4:
                return 5
        return 4

    if len(tracker) == 3:
        # three of a kind or two pair
        for v in tracker.values():
            if v == 3:
                return 3
        return 2

    if len(tracker) == 4:
        return 1

    return 0


def cardValue1(a: str) -> int:
    vals = {
        "A": 14,
        "K": 13,
        "Q": 12,
        "J": 11,
        "T": 10,
    }

    return int(a) if a.isnumeric() else vals[a]


def getType2(hand: str) -> int:
    """Returns the type of a hand given the input integer, performing optimal joker substitution
    0: high card
    1: one pair
    2: two pair
    3: three of a kind
    4: full house (triple and pair)
    5: four of a kind
    6: five of a kind
    """
    tracker = {}
    for ch in hand:
        if ch in tracker:
            tracker[ch] += 1
        else:
            tracker[ch] = 1

    if "J" in tracker:
        jCount = tracker["J"]

        if jCount == 5:
            return 6

        del tracker["J"]

        maxCount = 1
        maxChar = ""

        for k, v in tracker.items():
            if v >= maxCount:
                maxChar = k
                maxCount = v

        tracker[maxChar] += jCount

    if len(tracker) == 1:
        return 6

    if len(tracker) == 2:
        # four of a kind or full house
        for v in tracker.values():
            if v == 4:
                return 5
        return 4

    if len(tracker) == 3:
        # three of a kind or two pair
        for v in tracker.values():
            if v == 3:
                return 3
        return 2

    if len(tracker) == 4:
        return 1

    return 0


def cardValue2(a: str) -> int:
    vals = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "T": 10,
        "J": 1,
    }

    return int(a) if a.isnumeric() else vals[a]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path")
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # Part 1
    valAndBid: list[tuple[list[int], int]] = []

    for l in lines:
        hand, bid = l.split()
        vals = [getType1(hand)]
        for ch in hand:
            vals.append(cardValue1(ch))

        valAndBid.append((vals, int(bid)))

    valAndBid.sort(key=lambda x: x[0])

    sum1 = 0

    for rank, vnb in enumerate(valAndBid, 1):
        sum1 += rank * vnb[1]

    print(f"Part 1: {sum1}")

    # Part 2
    valAndBid: list[tuple[list[int], int]] = []

    for l in lines:
        hand, bid = l.split()
        vals = [getType2(hand)]
        for ch in hand:
            vals.append(cardValue2(ch))

        valAndBid.append((vals, int(bid)))

    valAndBid.sort(key=lambda x: x[0])

    sum2 = 0

    for rank, vnb in enumerate(valAndBid, 1):
        sum2 += rank * vnb[1]

    print(f"Part 2: {sum2}")
