# https://www.hackerrank.com/contests/code-23-2/challenges/locating-cody

import math
import os
import random
import re
import sys

from typing import List

#
# Complete the 'search_street' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY street as parameter.
#

def search_street(street: List[int]):
    startingPoints: List[int] = []
    for i, n in enumerate(street):
        if n == 1:
            startingPoints.append(i)

    longest: int = 0

    for i in startingPoints:
        # Search behind
        tmpI: int = i 
        backCount: int = 0
        backValid: bool = False
        while tmpI > 0 and street[tmpI-1] == 0:
            backCount += 1
            tmpI -= 1
            if tmpI > 0 and street[tmpI-1] == -1:
                backValid = True
                break

        tmpI = i
        forwardCount: int = 0
        forwardValid: int = False
        while tmpI < len(street)-1 and street[tmpI+1] == 0:
            forwardCount += 1
            tmpI += 1
            if tmpI < len(street)-1 and street[tmpI+1] == -1:
                forwardValid = True
                break
        
        if backValid:
            longest = max(backCount, longest)

        if forwardValid:
            longest = max(forwardCount, longest)

    return longest

def main():
    print(search_street([1,0,0,-1,0,0,0,0,1])) # Expected: 4
    print(search_street([0,0,1,-1])) # Expected: 0

if __name__ == '__main__':
    main()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # num_areas = int(input().strip())

    # street = list(map(int, input().rstrip().split()))

    # result = search_street(street)

    # fptr.write(str(result) + '\n')

    # fptr.close()
