# https://www.hackerrank.com/contests/code-23-2/challenges/locating-cody

import math
import os
import random
import re
import sys

from typing import Dict

#
# Complete the 'encrypt' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def encrypt(s: str) -> str:
    out: str = ""

    charToInt: Dict[str, int] = {}
    intToChar: Dict[int, str] = {}

    for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz"):
        charToInt[ch] = i
        intToChar[i] = ch

    for i, ch in enumerate(s):
        if ch.isalpha():
            shift: int = (charToInt[ch.lower()] + i + 1) % 26
            encrypted: str = intToChar[shift]

            if ch.isupper():
                encrypted = encrypted.upper()

            out += encrypted
        else:
            out += ch

    return out


def main():
    print(encrypt("ABC DE"))  # Expected: BDF IK
    print(encrypt("abcDE"))  # Expected: bdfHJ


if __name__ == "__main__":
    main()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()

    # result = encrypt(s)

    # fptr.write(result + '\n')

    # fptr.close()
