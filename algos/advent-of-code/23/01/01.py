import sys


def getSum1(s: str) -> int:
    left, right = 0, 0

    for ch in s:
        if ch in "123456789":
            left = int(ch)
            break

    for ch in s[::-1]:
        if ch in "123456789":
            right = int(ch)
            break

    return left * 10 + right


def getSum2(s: str) -> int:
    left, right = 0, 0
    numStrs: dict[str, int] = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    leftFound, rightFound = False, False
    for i in range(len(s)):
        if s[i] in "123456789":
            left = int(s[i])
            leftFound = True

        for k, v in numStrs.items():
            if i + len(k) <= len(s) and s[i : i + len(k)] == k:
                left = v
                leftFound = True
                break

        if leftFound:
            break

    for i in range(len(s) - 1, -1, -1):
        if s[i] in "123456789":
            right = int(s[i])
            rightFound = True

        for k, v in numStrs.items():
            if i + len(k) <= len(s) and s[i : i + len(k)] == k:
                right = v
                rightFound = True
                break

        if rightFound:
            break

    return left * 10 + right


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path")
        exit(1)

    sum1, sum2 = 0, 0

    f1 = open("01_1_py.txt", "w")
    f2 = open("01_2_py.txt", "w")

    with open(sys.argv[1]) as f:
        for line in f:
            val1 = getSum1(line)
            val2 = getSum2(line)

            f1.write(str(val1) + "\n")
            f2.write(str(val2) + "\n")

            sum1 += val1
            sum2 += val2

    f1.close()
    f2.close()

    print(f"Sum1: {sum1}\nSum2: {sum2}")
