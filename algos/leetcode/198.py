# Problem: https://leetcode.com/problems/house-robber
# tags: blind75, medium

# Time complexity: O(n)
# Space complexity: O(1)
# DP with memoization (only last 2 results needed)


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
