# Problem: https://leetcode.com/problems/make-sum-divisible-by-p/description/
# tags: medium

# Time complexity: O(n^2) - nested loops with sliding window
# Space complexity: O(n) - for modified nums array
# Approach: Brute force sliding window to find smallest subarray with sum % p == target
# NOTE: Can be optimized to O(n) using prefix sum + hashmap (see solution below)

# Alternative solutions:
# 1. Brute force - check all subarrays
#    Time: O(n^3) | Space: O(1)
# 2. Sliding window with modular sum [implemented]
#    Time: O(n^2) | Space: O(n)
# 3. Prefix sum + hashmap - track prefix mod remainders
#    Time: O(n) | Space: O(n)

from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        nums = [n % p for n in nums]
        currSum = sum(nums)
        target = currSum % p

        if target == 0:
            return 0

        for size in range(len(nums) - 1):
            tmp = sum(nums[:size])
            for j in range(len(nums) - size):
                tmp += nums[j + size]
                if tmp % p == target:
                    return size + 1
                tmp -= nums[j]

        return -1


def main():
    s = Solution()

    print(s.minSubarray([3, 1, 4, 2], 6))  # Expected: 1
    print(s.minSubarray([6, 3, 5, 2], 9))  # Expected: 2
    print(s.minSubarray([1, 2, 3], 3))  # Expected: 0


if __name__ == "__main__":
    main()


# IMPROVED O(n) SOLUTION:
# Time complexity: O(n)
# Space complexity: O(n)
#
# class Solution:
#     def minSubarray(self, nums: List[int], p: int) -> int:
#         total = sum(nums) % p
#         if total == 0:
#             return 0
#
#         # We need to find subarray with sum % p == total
#         # Using prefix sum: (prefix[j] - prefix[i]) % p == total
#         # => prefix[i] % p == (prefix[j] - total) % p
#
#         prefix_mod = 0
#         min_len = len(nums)
#         seen = {0: -1}  # prefix_mod -> index
#
#         for i, num in enumerate(nums):
#             prefix_mod = (prefix_mod + num) % p
#             # We need (prefix_mod - total) % p
#             needed = (prefix_mod - total) % p
#             if needed in seen:
#                 min_len = min(min_len, i - seen[needed])
#             seen[prefix_mod] = i
#
#         return min_len if min_len < len(nums) else -1
