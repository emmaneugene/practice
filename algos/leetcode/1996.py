# Problem: https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
# tags: medium

# Time complexity: O(n log n) - sorting
# Space complexity: O(n) - for characters list and track dictionary
# Approach: Sort by attack (desc), track higher atk chars per char,
#           then sort by defense and find intersection with higher def chars

# Alternative solutions:
# 1. Brute force - compare every pair of characters
#    Time: O(n^2) | Space: O(1)
# 2. Sort + set intersection - dual sort with set tracking [implemented]
#    Time: O(n log n) | Space: O(n)
# 3. Sort by attack desc, defense asc + greedy max defense tracking
#    Time: O(n log n) | Space: O(1)
# 4. Monotonic stack - sort by attack asc, defense desc, track max defense
#    Time: O(n log n) | Space: O(n)

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
        strongerSet = set()
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


# IMPROVEMENTS:
# The current solution is correct but can be optimized:
#
# 1. Space: Use O(1) extra space by sorting once and tracking max defense
#    - Sort by attack DESC, then defense ASC (so same attack chars have lower defense first)
#    - Track max defense seen so far
#    - Any char with defense < max_defense is weak
#
# 2. Time: Still O(n log n) but with simpler logic:
#
# class Solution:
#     def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
#         # Sort by attack DESC, defense ASC
#         # This ensures when attack ties, lower defense comes first
#         properties.sort(key=lambda x: (-x[0], x[1]))
#
#         max_defense = 0
#         weak_count = 0
#
#         for atk, dfs in properties:
#             if dfs < max_defense:
#                 weak_count += 1
#             else:
#                 max_defense = dfs
#
#         return weak_count
