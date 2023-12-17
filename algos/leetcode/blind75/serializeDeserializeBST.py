# Problem: https://leetcode.com/problems/serialize-and-deserialize-bst/

# Breadth-first search solution
# Time complexity: O(n)
# Space complexity: O(depth)
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a string"""
        if root is None or root.val is None:
            return ""
        # Parse to array
        treeArr: List[int] = []
        toExplore: List[TreeNode] = [root]

        while len(toExplore) > 0:
            node: TreeNode = toExplore.pop(0)
            treeArr.append(node.val)

            if node.val == -1:
                continue

            if node.left is None:
                toExplore.append(TreeNode(-1))
            else:
                toExplore.append(node.left)

            if node.right is None:
                toExplore.append(TreeNode(-1))
            else:
                toExplore.append(node.right)

        serialized: str = str(treeArr)
        return serialized.replace(" ", "")

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if len(data) == 0:
            return None

        arr: list[int] = [int(i) for i in data[1:-1].split(",")]

        rootVal = arr.pop(0)
        return self.constructNode(arr, rootVal)

    def constructNode(self, arr: list[int], val: int) -> Optional[TreeNode]:
        """Recursive function that constructs a TreeNode given an input array
        `arr` and node value `val`
        """
        node: TreeNode = TreeNode(val)

        leftVal: int = arr.pop(0)
        rightVal: int = arr.pop(0)

        if leftVal != -1:
            node.left = self.constructNode(arr, leftVal)

        if rightVal != -1:
            node.right = self.constructNode(arr, rightVal)

        return node


def inorderTraverse(node: TreeNode) -> str:
    output: list[int] = []

    inOrderVisit(node, output)

    return output


def inOrderVisit(node: TreeNode, output: list[int]) -> None:
    if node is None:
        return

    inOrderVisit(node.left, output)
    output.append(node.val)
    inOrderVisit(node.right, output)


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
def main():
    ser = Codec()
    deser = Codec()

    root: TreeNode = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print("Test 1:")
    # Before serialization
    print(inorderTraverse(root))
    # Serialization
    print(s := ser.serialize(root))
    # Deserialization
    print(inorderTraverse(deser.deserialize(s)))

    print("Test 2")
    print(s := ser.serialize(None))
    print(inorderTraverse(deser.deserialize(s)))

    print("Test 3")

    left: TreeNode = TreeNode(100)
    left.left = TreeNode(50)
    left.right = TreeNode(150)

    right: TreeNode = TreeNode(300)

    root: TreeNode = TreeNode(200)
    root.left = left
    root.right = right

    print(s := ser.serialize(root))
    print(inorderTraverse(deser.deserialize(s)))

    print("Test 4")

    left: TreeNode = TreeNode(100)

    right: TreeNode = TreeNode(300)
    right.left = TreeNode(250)
    right.right = TreeNode(350)

    root: TreeNode = TreeNode(200)
    root.left = left
    root.right = right

    print(s := ser.serialize(root))
    print(inorderTraverse(deser.deserialize(s)))


if __name__ == "__main__":
    main()
