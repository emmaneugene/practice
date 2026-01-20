# Problem: https://leetcode.com/problems/jump-game
# tags: blind75, medium

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        furthest = 0

        for idx, n in enumerate(nums):
            if idx <= furthest:
                furthest = max(idx + n, furthest)
            else:
                break

        return furthest >= len(nums) - 1


def main():
    s = Solution()

    print(s.canJump([2, 3, 1, 1, 4]))  # Expected: True
    print(s.canJump([3, 2, 1, 0, 4]))  # Expected: False


if __name__ == "__main__":
    main()
