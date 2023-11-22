# https://www.hackerrank.com/contests/code-23-2/challenges/straight-line-check

import math
import os
import random
import re
import sys

from typing import List

#
# Complete the 'straight_line_check' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY coordinates as parameter.
#


def straight_line_check(coordinates: List[List[int]]):
    # Corner cases (should not be encountered)
    if len(coordinates) < 2:
        return 0

    run: int = coordinates[1][0] - coordinates[0][0]
    rise: int = coordinates[1][1] - coordinates[0][1]

    for i in range(1, len(coordinates) - 1):
        if (
            coordinates[i + 1][0] - coordinates[i][0] != run
            or coordinates[i + 1][1] - coordinates[i][1] != rise
        ):
            return 0

    return 1


def main():
    coords = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(straight_line_check(coords))  # Expected: 1
    coords = [[1, 1], [2, 2], [3, 4], [4, 5], [5, 6], [7, 7]]
    print(straight_line_check(coords))  # Expected: 0


if __name__ == "__main__":
    main()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # num_coordinates = int(input().strip())

    # coordinates = []

    # for _ in range(num_coordinates):
    #     coordinates.append(list(map(int, input().rstrip().split())))

    # result = straight_line_check(coordinates)

    # fptr.write(str(result) + '\n')

    # fptr.close()
