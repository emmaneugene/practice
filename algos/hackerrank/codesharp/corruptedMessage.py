# https://www.hackerrank.com/contests/code-23-2/challenges/corruptedmessage

import math
import os
import random
import re
import sys

#
# Complete the 'corrupt' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def corrupt(s: str) -> str:
    out: str = ""

    # Corner cases: * at string start/end
    while s.startswith("*") or s.endswith("*"):
        if s.startswith("*"):
            s = s.lstrip("*")
            if len(s) == 0:
                return ""
            s = s[1:]
        else:
            s = s.rstrip("*")[:-1]
            if len(s) == 0:
                return ""
            s = s[:-1]

    idx: int = 0

    while idx < len(s):
        if idx + 1 < len(s) and s[idx + 1] == "*":
            idx += 3
        else:
            out += s[idx]
            idx += 1

    return out


def main():
    print(corrupt("ab*cd"))  # Expected: 'ad'
    print(corrupt("sta*ying *alive"))  # Expected: 'stinglive


if __name__ == "__main__":
    main()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = corrupt(s)

    # fptr.write(result + '\n')

    # fptr.close()
