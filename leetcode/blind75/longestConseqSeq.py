# Problem: https://leetcode.com/problems/longest-consecutive-sequence/

from typing import Dict, List


class Solution:
    def longestConsecutive(self,  nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        toCheck: Dict[int, bool] = {}

        for n in nums:
            toCheck[n] = True

        longest: int = 1

        for n in nums:
            if toCheck.get(n, False):
                curr: int = n
                comp: int = 0
                while toCheck.get(curr, False):
                    comp += 1
                    curr += 1

                longest = max(comp, longest)

        return longest


def main():
    s: Solution = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Expected: 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Expected: 9
    print(s.longestConsecutive(
        [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # Expected: 7


if __name__ == '__main__':
    main()
