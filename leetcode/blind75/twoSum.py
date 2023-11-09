# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Time complexity: O(n)
# Space complexity: O(n)

from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker: Dict[int, int] = {}

        for i, n in enumerate(nums):
            if target - n in tracker:
                return [tracker[target - n], i]
            tracker[n] = i

        return [-1, -1]  # Should not get here


def main():
    s: Solution = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))  # Expected: [0,1]
    print(s.twoSum([3, 2, 4], 6))  # Expected: [1,2]
    print(s.twoSum([3, 3], 6))  # Expected: [0,1]


if __name__ == "__main__":
    main()
