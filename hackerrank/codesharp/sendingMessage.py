# https://www.hackerrank.com/contests/code-23-2/challenges/sending-a-message


import math
import os
import random
import re
import sys

from typing import Dict, List

#
# Complete the 'min_stickers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY newspaper_clippings
#  2. STRING send_message
#

def getCounts(s: str) -> Dict[str, int]:
    counts: Dict[str, int] = {}

    for i, ch in enumerate(s):
        if ch in counts:
            counts[ch] += 1
        else:
            counts[ch] = 1

    return counts

def countSubstitutable(clipping: Dict[str, int], message: Dict[str, int]) -> int:
    subCount: int = 0

    for ch, count in message.items():
        if ch in clipping:
            subCount += min(count, clipping[ch])

    return subCount

def removeChars(clipping: Dict[str, int], message: Dict[str, int]) -> None:
    for ch in message.keys():
        if ch in clipping:
            message[ch] -= min(message[ch], clipping[ch])

def charsRemaining(message: Dict[str, int]) -> bool:
    for _, v in message.items():
        if v > 0: return True
    
    return False


def min_stickers(newspaper_clippings: List[str], send_message: str) -> int:
    clips: List[Dict[str, int]] = [getCounts(x) for x in newspaper_clippings]
    msg: Dict[str, int] = getCounts(send_message)

    print(clips)
    print(msg)

    clipCount: int = 0
    
    while charsRemaining(msg):
        foundClip: bool = False
        rmvCount: int = 0
        toRemove: Dict[str, int] = {}
        
        for c in clips:
            tmpCount: int = countSubstitutable(c, msg)
            if tmpCount > 0:
                foundClip = True
                print('Found clip')
                if tmpCount > rmvCount:
                    rmvCount = tmpCount
                    toRemove = c
        
        if not foundClip:
            return -1
     
        removeChars(toRemove, msg)
        clipCount += 1


    return clipCount

def main():
    print(min_stickers(['whale', 'tick', 'bonus'], 'watchout')) # Expected: 3
    print(min_stickers(['extravagant', 'small'], 'biased')) # Expected: -1

if __name__ == '__main__':
    main()
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # num_words = int(input().strip())

    # newspaper_clippings = input().rstrip().split()

    # send_message = input()

    # result = min_stickers(newspaper_clippings, send_message)

    # fptr.write(str(result) + '\n')

    # fptr.close()
