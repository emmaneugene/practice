# Problem: https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/
# tags: medium

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. Brute force - check all subarrays with length divisible by k
#    Time: O(n^2) | Space: O(1)
# 2. Prefix sums with min tracking by index mod k
#    Time: O(n) | Space: O(k)
# 3. Sliding window of size k with Kadane-style DP [implemented]
#    Time: O(n) | Space: O(n)

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
