# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Time complexity: O(n)
# Space complexity: O(n)

from typing import Optional, List


class TreeNode:
    '''Definition for a binary tree node
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output: List[List[int]] = []

        if root is None:
            return output

        currLevel: List[TreeNode] = [root]
        nextLevel: List[TreeNode] = []
        currList: List[int] = []

        while len(currLevel) > 0:
            new: TreeNode = currLevel.pop(0)
            currList.append(new.val)

            if new.left:
                nextLevel.append(new.left)
            if new.right:
                nextLevel.append(new.right)

            if len(currLevel) == 0:
                output.append(currList)
                currList = []
                currLevel = nextLevel
                nextLevel = []

        return output


def main():
    s: Solution = Solution()

    right: TreeNode = TreeNode(20, TreeNode(15), TreeNode(7))
    root: TreeNode = TreeNode(3, TreeNode(9), right)
    print(s.levelOrder(root))  # Expected: [[3],[9,20],[15,7]]

    root: TreeNode = TreeNode(1)
    print(s.levelOrder(root))  # Expected: [[1]]

    root: Optional[TreeNode] = None
    print(s.levelOrder(root))  # Expected: []


if __name__ == '__main__':
    main()
