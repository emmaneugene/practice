# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# tags: blind75, medium

# Time complexity: O(log(n))
# Space complexity: O(n) for storing all nodes


class TreeNode:
    def __init__(self, val: int, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        smaller = False
        larger = False
        equal = False

        if p.val < root.val:
            smaller = True
        elif p.val > root.val:
            larger = True
        else:
            equal = True

        if q.val < root.val:
            smaller = True
        elif q.val > root.val:
            larger = True
        else:
            equal = True

        if equal or (smaller and larger):
            return root
        if not smaller:
            return self.lowestCommonAncestor(root.right, p, q)
        return self.lowestCommonAncestor(root.left, p, q)


def main():
    s = Solution()

    t1 = TreeNode(
        6,
        TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5))),
        TreeNode(8, TreeNode(7), TreeNode(9)),
    )
    print(s.lowestCommonAncestor(t1, TreeNode(2), TreeNode(8)).val)  # Expected: 6
    print(s.lowestCommonAncestor(t1, TreeNode(2), TreeNode(4)).val)  # Expected: 2

    t2 = TreeNode(2, TreeNode(1))
    print(s.lowestCommonAncestor(t2, TreeNode(2), TreeNode(1)).val)  # Expected: 2


if __name__ == "__main__":
    main()
