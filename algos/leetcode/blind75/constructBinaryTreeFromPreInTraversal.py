# Problem: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

# Time complexity: O(n^2)
# Space complexity: O(n)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        if not preorder or not any(preorder):
            return None

        rootVal = preorder[0]

        splitIdx = inorder.index(rootVal)

        leftInorder = inorder[:splitIdx]
        rightInorder = inorder[splitIdx+1:]
        leftPreorder = preorder[1:1+len(leftInorder)]
        rightPreorder = preorder[1+len(leftInorder):]

        return TreeNode(
            preorder[0],
            self.buildTree(leftPreorder, leftInorder),
            self.buildTree(rightPreorder, rightInorder),
        )




def main():
    s: Solution = Solution()
    s.buildTree([3,9,20,15,7], [9,3,15,20,7])


if __name__ == "__main__":
    main()
