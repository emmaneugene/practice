# Problem: https://leetcode.com/problems/house-robber/

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        prev2Opt = nums[0]
        prev1Opt = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            newOpt = max(prev2Opt + nums[i], prev1Opt)
            prev2Opt = prev1Opt
            prev1Opt = newOpt

        return prev1Opt


def main():
    s: Solution = Solution()

    print(s.rob([1, 2, 3, 1]))  # 4
    print(s.rob([2, 7, 9, 3, 1]))  # 12


if __name__ == "__main__":
    main()
