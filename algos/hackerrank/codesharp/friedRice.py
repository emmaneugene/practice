# https://www.hackerrank.com/contests/code-23-2/challenges/testfriedrice

import math
import os
import random
import re
import sys

from typing import List

#
# Complete the 'fuiyoh' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY dishes as parameter.
#


def fuiyoh(dishes: List[List[int]]) -> int:
    dishes.sort(key=lambda x: (x[0], x[1]))
    count: int = 0
    lowestMsg: int = dishes[0][0]
    lowestGarlic: int = dishes[0][1]

    for d in dishes[1:]:
        if d[0] > lowestMsg and d[1] > lowestGarlic:
            count += 1

    return count


def main():
    print(fuiyoh([[6, 5], [3, 2]]))  # Expected: 1
    print(fuiyoh([[6, 5], [3, 2], [3, 3]]))  # Expected: 1
    print(fuiyoh([[6, 5]]))  # Expected: 1


if __name__ == "__main__":
    main()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # dishes = []

    # for _ in range(n):
    #     dishes.append(list(map(int, input().rstrip().split())))

    # result = fuiyoh(dishes)

    # fptr.write(str(result) + '\n')

    # fptr.close()
