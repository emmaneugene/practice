# Problem: https://leetcode.com/problems/subtree-of-another-tree
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. BFS + BFS comparison - BFS to find candidates, BFS to compare subtrees [implemented]
#    Time: O(m * n) | Space: O(m + n)
# 2. DFS + DFS comparison - recursive DFS traversal, recursive tree matching
#    Time: O(m * n) | Space: O(m + n)
# 3. Tree serialization - serialize both trees (preorder with nulls), substring check
#    Time: O(m + n) | Space: O(m + n)
# 4. Tree hashing - Merkle-style hash each subtree, compare hash values
#    Time: O(m + n) | Space: O(m + n)
# 5. KMP on serialized trees - serialize both, use KMP for substring matching
#    Time: O(m + n) | Space: O(m + n)

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        toVisit = deque([root])

        while any(toVisit):
            n: TreeNode = toVisit.popleft()
            if n.val == subRoot.val and self.isSameTree(n, subRoot):
                return True
            if n.left:
                toVisit.append(n.left)
            if n.right:
                toVisit.append(n.right)

        return False

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        # Perform BFS, return false if a single element doesn't match
        pToVisit = deque([p])
        qToVisit = deque([q])

        while len(pToVisit) > 0 and len(qToVisit) > 0:
            nextP: TreeNode = pToVisit.popleft()
            nextQ: TreeNode = qToVisit.popleft()

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


def main():
    s = Solution()

    t1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    t1s = TreeNode(4, TreeNode(1), TreeNode(2))
    print(s.isSubtree(t1, t1s))  # Expected: True

    t2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    t2s = TreeNode(4, TreeNode(1), TreeNode(2))
    print(s.isSubtree(t2, t2s))  # Expected: False


if __name__ == "__main__":
    main()
