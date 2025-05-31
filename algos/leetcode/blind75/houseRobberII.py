# Problem: https://leetcode.com/problems/house-robber-ii

# Time complexity: O(n)
# Space complexity: O(1)
# Let s() be the solution to houseRobber.py
# For `nums` of size n: take the max of:
#    - s(nums[:-1])
#    - s(nums[1:])


class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums or len(nums) == 0:
            return 0
        if len(nums) <= 3:
            return max(nums)

        return max(
            self.helper(nums[1:]),
            self.helper(nums[:-1])
        )

    def helper(self, nums: list[int]) -> tuple[int, int]:
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
    print(s.rob([2, 3, 2]))  # Expected: 3
    print(s.rob([1, 2, 3, 1]))  # Expected: 4
    print(s.rob([1, 1, 2, 1]))  # Expected: 3
    print(s.rob([1, 7, 9, 2]))  # Expected: 10


if __name__ == "__main__":
    main()
