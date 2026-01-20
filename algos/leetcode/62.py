# Problem: https://leetcode.com/problems/unique-paths
# tags: blind75, medium

# Time complexity: O(1)
# Space complexity: O(1)

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Combinatorial logic
        # How many unique permutations of m-1 (down) and n-1 right moves?
        return (int)(
            math.factorial(m + n - 2) / (math.factorial(m - 1) * math.factorial(n - 1))
        )


def main():
    s = Solution()

    print(s.uniquePaths(3, 7))  # 28
    print(s.uniquePaths(3, 2))  # 3


if __name__ == "__main__":
    main()
