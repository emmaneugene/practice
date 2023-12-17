# Problem: https://leetcode.com/problems/alien-dictionary

# Time complexity:
# Space complexity:

# TODO - unimplemented

# General idea: Check from 0th to nth character of each string to create a sorted order of chars
# If a contradiction is encountered, return '' immediately
# Need to maintain a queue of strings to check

from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        currCheck: List[str] = words
        nextCheck: List[str] = []
        while len(currCheck) > 0:
            # Come up with ordering of characters
            prevCh: str = currCheck[0][0]
            order: List[str] = []

            # for w in currCheck[1:]:
            #     if currCh =
            # For consecutive strings w identical characters, append to nextCheck (if there are characters remaining)

            # Try to insert new order into previous order, return "" if contradiction

            # ordering: str = ''
            # for w in words:
            #     ordering += w[i]
            # print(f'depth: {i}, order {ordering}')

        return ""


def main():
    s: Solution = Solution()
    print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))
    print(s.alienOrder(["z", "x"]))
    print(s.alienOrder(["z", "x", "z"]))


if __name__ == "__main__":
    main()
