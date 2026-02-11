# Problem: https://leetcode.com/problems/unique-paths
# tags: blind75, medium

# Time complexity: O(1)
# Space complexity: O(1)

# Alternative solutions:
# 1. Brute force (recursion) - explore all right/down paths
#    Time: O(2^(m+n)) | Space: O(m+n)
# 2. Top-down DP (memoization) - cache subproblem results
#    Time: O(mn) | Space: O(mn)
# 3. Bottom-up DP (2D table) - fill grid from bottom-right
#    Time: O(mn) | Space: O(mn)
# 4. Bottom-up DP (1D rolling array) - single row, update in place
#    Time: O(mn) | Space: O(n)
# 5. Combinatorics - C(m+n-2, m-1) [implemented]
#    Time: O(m+n) | Space: O(1)

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
