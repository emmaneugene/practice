# Problem: https://leetcode.com/problems/same-tree/
from typing import Optional

# Time complexity - O(n)
# Space complexity - O(n)


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        # Perform BFS, return false if a single element doesn't match
        pToVisit: list[TreeNode] = [p]
        qToVisit: list[TreeNode] = [q]

        while len(pToVisit) > 0 and len(qToVisit) > 0:
            nextP: TreeNode = pToVisit.pop(0)
            nextQ: TreeNode = qToVisit.pop(0)

            if nextP.val != nextQ.val:
                return False

            if nextP.left is not None or nextQ.left is not None:
                if nextP.left is None or nextQ.left is None:
                    return False
                pToVisit.append(nextP.left)
                qToVisit.append(nextQ.left)

            if nextP.right is not None or nextQ.right is not None:
                if nextP.right is None or nextQ.right is None:
                    return False
                pToVisit.append(nextP.right)
                qToVisit.append(nextQ.right)

        return len(pToVisit) == len(qToVisit)
