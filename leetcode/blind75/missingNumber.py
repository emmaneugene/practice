# Problem: https://leetcode.com/problems/missing-number/

# Complexity: O(n) time, O(n) space

from typing import Dict, List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        keys: Dict[int, int] = {}

        for n in nums:
            keys[n] = 1

        for i in range(len(nums) + 1):
            if i not in keys:
                return i

        # Should not get here
        return -1
