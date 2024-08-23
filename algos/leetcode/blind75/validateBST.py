# Problem: https://leetcode.com/problems/validate-binary-search-tree

from typing import Optional


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity: O(n)
# Space complexity: O(n) due to recursive stack frames
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True

        return self.checkNode(root)[0]

    def checkNode(self, node: TreeNode) -> tuple[bool, int, int]:
        """Recursively checks whether this node is a valid BST, and returns
        the min and max values of the BST in question
        """
        if node.left is None and node.right is None:
            return True, node.val, node.val
        elif node.right is None:
            leftIsBST, leftMin, leftMax = self.checkNode(node.left)
            isBST = leftIsBST and leftMax < node.val
            return isBST, leftMin, node.val
        elif node.left is None:
            rightIsBST, rightMin, rightMax = self.checkNode(node.right)
            isBST = rightIsBST and rightMin > node.val
            return isBST, node.val, rightMax
        else:
            leftIsBST, leftMin, leftMax = self.checkNode(node.left)
            rightIsBST, rightMin, rightMax = self.checkNode(node.right)
            isBST = (
                leftIsBST and leftMax < node.val and rightIsBST and rightMin > node.val
            )
            return isBST, leftMin, rightMax


def main():
    s = Solution()

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    print(s.isValidBST(root))  # Expected: True

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    print(s.isValidBST(root))  # Expected: False

    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    print(s.isValidBST(root))  # Expected: False


if __name__ == "__main__":
    main()
