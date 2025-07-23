# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree

# Have to perform a search across all nodes in the worst case
# Time complexity: O(n)
# Space complexity: O(n)

from typing import Optional, Set


class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        return self.helper(root, set([p.val, q.val]))[0]

    def helper(self, node: TreeNode, vals: Set[int]) -> tuple[Optional[TreeNode], Set]:
        if node is None:
            return None, set()

        lNode, lVals = self.helper(node.left, vals)
        lVals.add(node.val)
        if lNode:
            return lNode, lVals
        if vals.issubset(lVals):
            return node, lVals

        rNode, rVals = self.helper(node.right, vals)
        rVals.update(lVals)
        if rNode:
            return rNode, rVals
        if vals.issubset(rVals):
            return node, rVals

        return None, rVals


def main():
    s = Solution()

    t1 = TreeNode(
        3,
        TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
        TreeNode(1, TreeNode(0), TreeNode(8)),
    )
    print(s.lowestCommonAncestor(t1, TreeNode(5), TreeNode(1)).val)  # Expected: 3
    print(s.lowestCommonAncestor(t1, TreeNode(5), TreeNode(4)).val)  # Expected: 5

    t2 = TreeNode(1, TreeNode(2))
    print(s.lowestCommonAncestor(t2, TreeNode(1), TreeNode(2)).val)  # Expected: 1


if __name__ == "__main__":
    main()
