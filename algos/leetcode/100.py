# Problem: https://leetcode.com/problems/same-tree
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. Recursive DFS - recursion
#    Time: O(n) | Space: O(n)
# 2. Iterative BFS - queue [implemented]
#    Time: O(n) | Space: O(n)
# 3. Iterative DFS - stack
#    Time: O(n) | Space: O(n)

from collections import deque
from typing import Optional


class TreeNode:
    """Definition for a binary tree node"""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False

        # Perform BFS, return false if a single element doesn't match
        pToVisit = deque([p])
        qToVisit = deque([q])

        while any(pToVisit) and any(qToVisit):
            nextP = pToVisit.popleft()
            nextQ = qToVisit.popleft()

            if nextP.val != nextQ.val:
                return False

            if nextP.left or nextQ.left:
                if not nextP.left or not nextQ.left:
                    return False
                pToVisit.append(nextP.left)
                qToVisit.append(nextQ.left)

            if nextP.right or nextQ.right:
                if not nextP.right or not nextQ.right:
                    return False
                pToVisit.append(nextP.right)
                qToVisit.append(nextQ.right)

        return len(pToVisit) == len(qToVisit)


def main():
    s = Solution()

    print(
        s.isSameTree(
            TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))
        )
    )  # Expected: True
    print(
        s.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)))
    )  # Expected: False
    print(
        s.isSameTree(
            TreeNode(1, TreeNode(2), TreeNode(1)), TreeNode(1, TreeNode(1), TreeNode(2))
        )
    )  # Expected: False


if __name__ == "__main__":
    main()
