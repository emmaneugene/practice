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
        if not root:
            return True

        return self.checkNode(root)[0]

    def checkNode(self, node: TreeNode) -> tuple[bool, int, int]:
        """Recursively checks whether this node is a valid BST, and returns
        the min and max values of the BST in question
        """
        if not node.left and not node.right:
            return True, node.val, node.val
        elif not node.right:
            lValid, lMin, lMax = self.checkNode(node.left)
            isBST = lValid and lMax < node.val
            return isBST, lMin, node.val
        elif not node.left:
            rValid, rMin, rMax = self.checkNode(node.right)
            isBST = rValid and rMin > node.val
            return isBST, node.val, rMax
        else:
            lValid, lMin, lMax = self.checkNode(node.left)
            rValid, rMin, rMax = self.checkNode(node.right)
            isBST = lValid and lMax < node.val and rValid and rMin > node.val
            return isBST, lMin, rMax


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
