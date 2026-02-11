# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(1)

# Alternative solutions:
# 1. Recursive DFS - recursion [implemented]
#    Time: O(n) | Space: O(h)
# 2. Iterative BFS - queue, level-by-level processing
#    Time: O(n) | Space: O(n)
# 3. Iterative DFS - stack
#    Time: O(n) | Space: O(h)

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def main():
    s = Solution()

    root: TreeNode = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    print(s.maxDepth(root))  # Expected: 3

    root: TreeNode = TreeNode(1, None, TreeNode(2))
    print(s.maxDepth(root))  # Expected: 2


if __name__ == "__main__":
    main()
