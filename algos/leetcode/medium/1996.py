# Problem: https://leetcode.com/problems/generate-parentheses/

# Time complexity: O(nlog(n))
# Space complexity: O(n^2)

from copy import copy
from dataclasses import dataclass
from typing import List


@dataclass
class Character:
    idx: int
    atk: int
    df: int


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        characters = [Character(i, p[0], p[1]) for i, p in enumerate(properties)]
        track = {}

        # Compute set of characters with higher atk
        characters.sort(key=lambda x: x.atk, reverse=True)
        strongerSet = set()
        currSet = set()
        currAtk = characters[0].atk
        for c in characters:
            if c.atk < currAtk:
                strongerSet = currSet
                currSet = copy(strongerSet)
                currAtk = c.atk
            track[c.idx] = strongerSet
            currSet.add(c.idx)

        # Compute set of characters with higher def
        characters.sort(key=lambda x: x.df, reverse=True)
        strongerSet.clear()
        currSet = set()
        currDf = characters[0].df
        for c in characters:
            if c.df < currDf:
                strongerSet = currSet
                currSet = copy(strongerSet)
                currDf = c.df
            track[c.idx] = track[c.idx].intersection(strongerSet)
            currSet.add(c.idx)

        return sum(1 for _ in filter(lambda x: len(x) > 0, track.values()))


def main():
    s = Solution()

    print(s.numberOfWeakCharacters([[5, 5], [6, 3], [3, 6]]))  # Expected: 0
    print(s.numberOfWeakCharacters([[2, 2], [3, 3]]))  # Expected: 1
    print(s.numberOfWeakCharacters([[1, 5], [10, 4], [4, 3]]))  # Expected: 1

    print(
        s.numberOfWeakCharacters(
            [
                [7, 7],
                [1, 2],
                [9, 7],
                [7, 3],
                [3, 10],
                [9, 8],
                [8, 10],
                [4, 3],
                [1, 5],
                [1, 5],
            ]
        )
    )  # Expected: 6


if __name__ == "__main__":
    main()
