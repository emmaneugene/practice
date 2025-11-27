# Problem: https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/

# Time complexity: O(n)
# Space complexity: O(n)

from typing import List

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        if not nums or k > len(nums):
            return -1

        curr = sum(nums[:k])
        subSums = [curr]

        for i in range(len(nums)-k):
            curr += nums[i+k] - nums[i]
            subSums.append(curr)

        for i in range(k, len(subSums)):
            if subSums[i-k] > 0:
                subSums[i] += subSums[i-k]

        return max(subSums)
