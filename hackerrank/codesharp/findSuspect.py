# https://www.hackerrank.com/contests/code-23-2/challenges/find-the-suspect

import math
import os
import random
import re
import sys

from typing import Dict, List

#
# Complete the 'suspect' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER num_accusations
#  3. 2D_INTEGER_ARRAY accusations
#


def suspect(n: int, num_accusations: int, accusations: List[List[int]]):
    # person:
    accGiven: Dict[int, int] = {}
    accRcvd: Dict[int, int] = {}

    for a in accusations:
        sender: int = a[0]
        receiver: int = a[1]

        if sender in accGiven:
            accGiven[sender] += 1
        else:
            accGiven[sender] = 1

        if receiver in accRcvd:
            accRcvd[receiver] += 1
        else:
            accRcvd[receiver] = 1

    for k, v in accGiven.items():
        if v > n / 2:
            return k

    majorityAccusedFound: bool = False
    majorityAccused: int = 0

    for k, v in accRcvd.items():
        if v > n / 2:
            if majorityAccusedFound:
                return 0
            else:
                majorityAccused = k
                majorityAccusedFound = True

    return majorityAccused


def main():
    print(suspect(4, 5, [[1, 2], [2, 3], [3, 2], [3, 4], [4, 2]]))  # Expected: 2
    print(
        suspect(6, 8, [[1, 2], [2, 1], [3, 1], [4, 2], [5, 1], [5, 2], [6, 1], [6, 2]])
    )  # Expected: 0
    print(suspect(3, 4, [[1, 2], [1, 3], [2, 3], [3, 2]]))  # Expected: 1


if __name__ == "__main__":
    main()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # n = int(input().strip())

    # num_accusations = int(input().strip())

    # accusations = []

    # for _ in range(num_accusations):
    #     accusations.append(list(map(int, input().rstrip().split())))

    # result = suspect(n, num_accusations, accusations)

    # fptr.write(str(result) + '\n')

    # fptr.close()
