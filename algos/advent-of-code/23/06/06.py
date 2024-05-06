import sys
import functools

# Formula is (x)(a - x) where a is total time and x is time held
# Find the intersections for where (x)(a - x)


def waysToWin(time: int, dist: int):
    intersect: int = 0

    for i in range(time):
        if i * (time - i) > dist:
            intersect = i
            break

    return time + 1 - (2 * intersect)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a file path")
        exit(1)

    with open(sys.argv[1]) as f:
        lines = f.readlines()

    # Part 1
    times = list(map(lambda x: int(x), lines[0].split()[1:]))
    distances = list(map(lambda x: int(x), lines[1].split()[1:]))
    ways = list(map(waysToWin, times, distances))
    print(functools.reduce(lambda x, y: x * y, ways))

    # Part 2
    time = int("".join(lines[0].split()[1:]))
    distance = int("".join(lines[1].split()[1:]))
    print(waysToWin(time, distance))
