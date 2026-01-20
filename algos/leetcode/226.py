# Problem: https://leetcode.com/problems/invert-binary-tree
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(1)

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        self.swapChildren(root)
        return root

    def swapChildren(self, node: TreeNode) -> None:
        if node.left:
            self.swapChildren(node.left)

        if node.right:
            self.swapChildren(node.right)

        node.left, node.right = node.right, node.left


def main():
    s = Solution()


if __name__ == "__main__":
    main()
