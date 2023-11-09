# Problem: https://leetcode.com/problems/subtree-of-another-tree/

# Time complexity: O(n)
# Space complexity: O(n)

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True

        toVisit: list[TreeNode] = [root]

        while len(toVisit) > 0:
            n: TreeNode = toVisit.pop(0)
            if n.val == subRoot.val and self.isSameTree(n, subRoot):
                return True

            if n.left:
                toVisit.append(n.left)

            if n.right:
                toVisit.append(n.right)

        return False

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
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
