# Problem: https://leetcode.com/problems/house-robber
# tags: blind75, medium

# Time complexity: O(n)
# Space complexity: O(1)
# DP with memoization (only last 2 results needed)

# Alternative solutions:
# 1. Brute force recursion - try all rob/skip combinations
#    Time: O(2^n) | Space: O(n)
# 2. Recursion with memoization - top-down DP, hashmap/array cache
#    Time: O(n) | Space: O(n)
# 3. Bottom-up DP with array - tabulation
#    Time: O(n) | Space: O(n)
# 4. Bottom-up DP with two variables - space-optimized tabulation [implemented]
#    Time: O(n) | Space: O(1)


class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums or len(nums) == 0:
            return 0

        prev, curr = 0, 0
        for num in nums:
            new = max(prev + num, curr)
            prev = curr
            curr = new

        return curr


def main():
    s = Solution()

    print(s.rob([1, 2, 3, 1]))  # 4
    print(s.rob([2, 7, 9, 3, 1]))  # 12


if __name__ == "__main__":
    main()
