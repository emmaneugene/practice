# Problem: https://leetcode.com/problems/climbing-stairs

# Time complexity: O(n)
# Space complexity: O(n)
# Effectively computing fibonacci


class Solution:
    def climbStairs(self, n: int) -> int:
        memo: dict[int, int] = {}
        memo[1] = 1
        memo[2] = 2

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]


def main():
    s: Solution = Solution()

    print(s.climbStairs(2))  # 2
    print(s.climbStairs(3))  # 3


if __name__ == "__main__":
    main()
