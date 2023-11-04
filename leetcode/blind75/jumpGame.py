# Problem: https://leetcode.com/problems/jump-game/

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        furthest: int = 0

        for idx, n in enumerate(nums):
            if idx <= furthest and idx + n > furthest:
                furthest = idx + n

        return furthest >= len(nums) - 1


def main():
    s: Solution = Solution()

    print(s.canJump([2, 3, 1, 1, 4]))  # True
    print(s.canJump([3, 2, 1, 0, 4]))  # False


if __name__ == "__main__":
    main()
