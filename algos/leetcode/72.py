# Problem: https://leetcode.com/problems/edit-distance
# tags: medium

# Dynamic programming

# Time complexity: O(m * n) - m = len(word1), n = len(word2), each subproblem computed once
# Space complexity: O(m * n) - memoization cache + O(m + n) recursion call stack

# Alternative solutions:
# 1. Brute force recursion - recursion, three-way branching
#    Time: O(3^(m+n)) | Space: O(m + n)
# 2. Top-down DP (memoized recursion) - recursion, hash map [implemented]
#    Time: O(m * n) | Space: O(m * n)
# 3. Bottom-up DP (2D table) - tabulation
#    Time: O(m * n) | Space: O(m * n)
# 4. Bottom-up DP (space-optimized, two rows) - tabulation, rolling array
#    Time: O(m * n) | Space: O(min(m, n))


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}

        def helper(w1, w2, idx1, idx2):
            if idx1 == 0:
                return idx2

            if idx2 == 0:
                return idx1

            if (idx1, idx2) in memo:
                return memo[(idx1, idx2)]

            if w1[idx1 - 1] == w2[idx2 - 1]:
                memo[(idx1, idx2)] = helper(w1, w2, idx1 - 1, idx2 - 1)
            else:
                replace = helper(w1, w2, idx1 - 1, idx2 - 1)
                insert = helper(w1, w2, idx1, idx2 - 1)
                delete = helper(w1, w2, idx1 - 1, idx2)
                memo[(idx1, idx2)] = min([replace, insert, delete]) + 1

            return memo[(idx1, idx2)]

        return helper(word1, word2, len(word1), len(word2))


def main():
    s = Solution()
    print(s.minDistance("horse", "ros"))  # Expected: 3
    print(s.minDistance("intention", "execution"))  # Expected: 5


if __name__ == "__main__":
    main()
