# Problem: https://leetcode.com/problems/binary-tree-maximum-path-sum

# Time complexity: O(n)
# Space complexity: O(n)

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        maxExt, maxCompl = self.helper(root)
        return maxExt if maxCompl is None else max(maxExt, maxCompl)

    def helper(self, root: TreeNode) -> tuple[int, Optional[int]]:
        """Needs to return extendable path, and completed path"""
        if not root.left and not root.right:
            return (root.val, None)

        if not root.right or not root.left:
            child = root.right if root.right else root.left
            extendable, complete = self.helper(child)
            maxCompl = extendable if not complete else max(extendable, complete)
            return (max(root.val, root.val + extendable), maxCompl)

        leftExt, leftCompl = self.helper(root.left)
        rightExt, rightCompl = self.helper(root.right)

        compls = [root.val + leftExt + rightExt, leftExt, rightExt]
        if leftCompl:
            compls.append(leftCompl)
        if rightCompl:
            compls.append(rightCompl)

        return (
            max(root.val, root.val + leftExt, root.val + rightExt),
            max(compls),
        )


def main():
    s: Solution = Solution()

    print(s.maxPathSum(TreeNode(2, TreeNode(1), TreeNode(3))))  # Expected: 6
    print(s.maxPathSum(TreeNode(-1, TreeNode(0), TreeNode(1))))  # Expected: 1
    print(s.maxPathSum(
            TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        )
    )  # Expected: 42


if __name__ == "__main__":
    main()
