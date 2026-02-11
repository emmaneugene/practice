# Problem: https://leetcode.com/problems/climbing-stairs
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(n)
# Effectively computing fibonacci

# Alternative solutions:
# 1. Brute force recursion - recursion tree
#    Time: O(2^n) | Space: O(n)
# 2. Memoized recursion (top-down DP) - recursion, hash map
#    Time: O(n) | Space: O(n)
# 3. Bottom-up DP with array - tabulation [implemented]
#    Time: O(n) | Space: O(n)
# 4. Bottom-up DP with two variables - iterative fibonacci
#    Time: O(n) | Space: O(1)
# 5. Matrix exponentiation - linear algebra
#    Time: O(log n) | Space: O(1)
# 6. Binet's formula (closed-form) - math
#    Time: O(1) | Space: O(1)


class Solution:
    def climbStairs(self, n: int) -> int:
        memo: dict[int, int] = {}
        memo[1] = 1
        memo[2] = 2

        for i in range(3, n + 1):
            memo[i] = memo[i - 1] + memo[i - 2]

        return memo[n]


def main():
    s = Solution()

    print(s.climbStairs(2))  # 2
    print(s.climbStairs(3))  # 3


if __name__ == "__main__":
    main()
