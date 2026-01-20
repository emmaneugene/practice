# Problem: https://leetcode.com/problems/generate-parentheses/
# tags: medium

# Time complexity: O(4^n / sqrt(n)) - generates all Catalan(n) valid combinations
# Space complexity: O(4^n / sqrt(n)) - stores all result strings + O(n) recursion depth
from typing import List


class Solution:
    # Iterative - possibility to store duplicates
    def generateParenthesis(self, n: int) -> List[str]:
        if n < 1:
            return []
        result = ["()"]
        for _ in range(1, n):
            tmp = set()
            for s in result:
                for i in range(len(s)):
                    tmp.add(s[:i] + "()" + s[i:])

            result = list(tmp)

        return result

    # Recursive
    def generateParenthesis2(self, n: int) -> List[str]:
        result = []

        def helper(curr: str, open: int, usable: int) -> None:
            if open == 0 and usable == 0:
                result.append(curr)
                return
            if open > 0:
                helper(curr + ")", open - 1, usable)
            if usable > 0:
                helper(curr + "(", open + 1, usable - 1)

        helper("", 0, n)
        return result


def main():
    s = Solution()

    print(s.generateParenthesis2(1))  # Expected: ["()"]
    print(s.generateParenthesis2(2))  # Expected: ["(())", "()()"]
    print(s.generateParenthesis2(3))
    # Expected: ["((()))", "(()())", "(())()" "()(())", "()()()"]


if __name__ == "__main__":
    main()
