import sys


def getMatches(s: str) -> int:
    arr = s.split(":")[1].split("|")
    winningNums = set(arr[0].split())
    nums = arr[1].split()

    matches = 0

    for n in nums:
        if n in winningNums:
            matches += 1

    return matches


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path")
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    cardMatches = [getMatches(line) for line in lines]

    sum1 = sum(map(lambda x: 2 ** (x - 1) if x > 0 else 0, cardMatches))

    cardCopies = [1] * len(cardMatches)

    for i in range(len(cardCopies)):
        extraCards = cardMatches[i]
        for j in range(extraCards):
            cardCopies[i + j + 1] += cardCopies[i]

    sum2 = sum(cardCopies)

    print(f"Sum 1: {sum1}\nSum 2: {sum2}")
