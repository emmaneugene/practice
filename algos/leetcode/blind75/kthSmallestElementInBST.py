# Problem: https://leetcode.com/problems/kth-smallest-element-in-a-bst

# Time complexity: O(n) - but shorter in practice
# Space complexity: O(n) - but shorter in practice
# Perform inorder traversal while appending to an array, but break once array
# length reaches k


from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def inorderTraverseAndFind(self, root: TreeNode, values: list[int], k: int) -> None:
        if root.left:
            self.inorderTraverseAndFind(root.left, values, k)
        if len(values) >= k:
            return

        values.append(root.val)
        if len(values) >= k:
            return

        if root.right:
            self.inorderTraverseAndFind(root.right, values, k)

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return -1

        values: list[int] = []
        self.inorderTraverseAndFind(root, values, k)

        return values[-1]


def main():
    s = Solution()

    tree1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
    print(s.kthSmallest(tree1, 1))  # Expected: 1

    tree2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    print(s.kthSmallest(tree2, 3))  # Expected: 3


if __name__ == "__main__":
    main()
