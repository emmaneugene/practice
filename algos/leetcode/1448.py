# Problem: https://leetcode.com/problems/count-good-nodes-in-binary-tree/
# tags: medium

# Time complexity: O(n)
# Space complexity: O(n)
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None) -> None:
        self.val: int = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.countNodes(root, root.val)

    def countNodes(self, node: TreeNode, largest: int) -> int:
        count: int = 0
        if node.val >= largest:
            count += 1
            largest = node.val

        if node.left:
            count += self.countNodes(node.left, largest)

        if node.right:
            count += self.countNodes(node.right, largest)

        return count


def main():
    s: Solution = Solution()

    tree1 = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    print(s.goodNodes(tree1))  # 4

    tree2 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))
    print(s.goodNodes(tree2))  # 3

    tree3 = TreeNode(1)
    print(s.goodNodes(tree3))  # 1


if __name__ == "__main__":
    main()
