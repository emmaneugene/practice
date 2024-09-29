import sys

# Load input file as 2D array with padding, check line by line and accumulate


def getSum1(matr: list[str]) -> int:
    result = 0

    for i in range(len(matr)):
        numFound: bool = False
        numStr, numStart = "", 0
        for j in range(len(matr[0])):
            if matr[i][j].isdecimal():
                if not numFound:
                    numFound = True
                    numStart = j
                    numStr = matr[i][j]
                else:
                    numStr += matr[i][j]
            elif numFound:
                if adjToSymbol(matr, i, numStart, j):
                    result += int(numStr)

                numFound = False
                numStr = ""

    return result


def adjToSymbol(matr: list[str], row: int, colStart: int, colEnd: int):
    toCheck: str = ""

    toCheck += (
        matr[row - 1][colStart - 1]
        + matr[row][colStart - 1]
        + matr[row + 1][colStart - 1]
        + matr[row - 1][colEnd]
        + matr[row][colEnd]
        + matr[row + 1][colEnd]
    )

    for i in range(colStart, colEnd):
        toCheck += matr[row - 1][i] + matr[row + 1][i]

    for ch in toCheck:
        if ch != ".":
            return True

    return False


def getSum2(matr: list[str]) -> int:
    gears: list[tuple] = []
    result = 0

    for i in range(len(matr)):
        for j in range(len(matr[0])):
            if matr[i][j] == "*":
                gears.append((i, j))

    for gear in gears:
        nums = getAdjNumbers(matr, gear[0], gear[1])
        if len(nums) == 2:
            result += nums[0] * nums[1]

    return result


def getAdjNumbers(matr: list[str], row: int, col: int) -> list[int]:
    adjNums: list[str] = []

    topLeft = lTraceNum(matr[row - 1][:col])
    topRight = rTraceNum(matr[row - 1][col + 1 :])
    left = lTraceNum(matr[row][:col])
    right = rTraceNum(matr[row][col + 1 :])
    botLeft = lTraceNum(matr[row + 1][:col])
    botRight = rTraceNum(matr[row + 1][col + 1 :])

    if matr[row - 1][col].isdecimal():
        adjNums.append(topLeft + matr[row - 1][col] + topRight)
    else:
        adjNums.extend([topLeft, topRight])

    adjNums.extend([left, right])

    if matr[row + 1][col].isdecimal():
        adjNums.append(botLeft + matr[row + 1][col] + botRight)
    else:
        adjNums.extend([botLeft, botRight])

    return list(map(lambda x: int(x), filter(lambda x: len(x) > 0, adjNums)))


def lTraceNum(s: str) -> str:
    idx = len(s)
    while idx - 1 > 0 and s[idx - 1].isdecimal():
        idx -= 1

    return s[idx:]


def rTraceNum(s: str) -> str:
    idx = 0
    while idx < len(s) and s[idx].isdecimal():
        idx += 1

    return s[:idx]


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path")
        exit(1)

    f = open(sys.argv[1])
    matr: list[str] = ["." + line.strip() + "." for line in f]
    f.close()

    # Pad matrix with "."
    matr.insert(0, "." * len(matr[0]))
    matr.append("." * len(matr[0]))

    print(f"Sum 1: {getSum1(matr)}\nSum 2: {getSum2(matr)}")
