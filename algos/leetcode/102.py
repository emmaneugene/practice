# Problem: https://leetcode.com/problems/binary-tree-level-order-traversal
# tags: blind75, medium

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. BFS with queue - deque, level-by-level processing [implemented]
#    Time: O(n) | Space: O(n)
# 2. DFS with recursion - recursion, depth tracking
#    Time: O(n) | Space: O(n)

from typing import Optional, List


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res: List[List[int]] = []

        if not root:
            return res

        currLvl: List[TreeNode] = [root]
        nextLvl: List[TreeNode] = []
        currVals: List[int] = []

        while len(currLvl) > 0:
            new = currLvl.pop(0)
            currVals.append(new.val)

            if new.left:
                nextLvl.append(new.left)
            if new.right:
                nextLvl.append(new.right)

            if len(currLvl) == 0:
                res.append(currVals)
                currVals = []
                currLvl = nextLvl
                nextLvl = []

        return res


def main():
    s = Solution()

    right = TreeNode(20, TreeNode(15), TreeNode(7))
    root = TreeNode(3, TreeNode(9), right)
    print(s.levelOrder(root))  # Expected: [[3],[9,20],[15,7]]

    root = TreeNode(1)
    print(s.levelOrder(root))  # Expected: [[1]]

    root = None
    print(s.levelOrder(root))  # Expected: []


if __name__ == "__main__":
    main()
