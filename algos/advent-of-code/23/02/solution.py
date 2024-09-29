import sys


def getSum1(line: str) -> int:
    arr = line.split(":")
    gameId: int = int(arr[0].split()[1])

    return gameId if validGame(arr[1]) else 0


def validGame(line: str) -> bool:
    limits: dict[str, int] = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }

    games = line.split(";")
    for game in games:
        colorCount = game.split(",")
        for e in colorCount:
            arr = e.split()
            count = int(arr[0])
            color = arr[1]

            if count > limits[color]:
                return False

    return True


def getSum2(line: str) -> int:
    limits: dict[str, int] = {
        "red": 0,
        "green": 0,
        "blue": 0,
    }

    gameStr = line.split(":")[1]
    games = gameStr.split(";")

    for game in games:
        colorCount = game.split(",")
        for e in colorCount:
            arr = e.split()
            count = int(arr[0])
            color = arr[1]

            if limits[color] < count:
                limits[color] = count

    return limits["red"] * limits["blue"] * limits["green"]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path")
        exit(1)

    sum1, sum2 = 0, 0

    with open(sys.argv[1]) as f:
        for line in f:
            sum1 += getSum1(line)
            sum2 += getSum2(line)

    print(f"Sum1: {sum1}\nSum2: {sum2}")
