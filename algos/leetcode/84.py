# Problem: https://leetcode.com/problems/largest-rectangle-in-histogram/
# tags: hard

# Time complexity: O(n)
# Space complexity: O(n)

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = heights[0]
        stack = []
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)

        while stack:
            height = heights[stack.pop()]
            width = len(heights) if not stack else len(heights) - stack[-1] - 1
            res = max(res, height * width)

        return res


def main():
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))  # Expected: 10
    print(s.largestRectangleArea([2, 4]))  # Expected: 4


if __name__ == "__main__":
    main()
