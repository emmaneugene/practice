# Problem: https://leetcode.com/problems/serialize-and-deserialize-bst

# Time complexity: O(n)
# Space complexity: O(n)
# Serialize to array representation with BFS


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""

        def preorder(node):
            if not node:
                vals.append("null")
                return
            vals.append(str(node.val))
            preorder(node.left)
            preorder(node.right)

        vals = []
        preorder(root)
        return ",".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree."""

        def build():
            val = next(vals)
            if val == "null":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node

        vals = iter(data.split(","))
        return build()


def inorder(node: TreeNode) -> str:
    def inorderV(node: TreeNode, output: list[int]) -> None:
        if not node:
            return

        inorderV(node.left, output)
        output.append(node.val)
        inorderV(node.right, output)

    output: list[int] = []
    inorderV(node, output)
    return output


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
def main():
    ser = Codec()
    deser = Codec()

    print("Test 1:")
    t1 = TreeNode(2, TreeNode(1), TreeNode(3))
    print(inorder(t1))
    print(s := ser.serialize(t1))
    print(inorder(deser.deserialize(s)))

    print("Test 2")
    print(inorder(None))
    print(s := ser.serialize(None))
    print(inorder(deser.deserialize(s)))

    print("Test 3")
    t3: TreeNode = TreeNode(
        200, TreeNode(100, TreeNode(50), TreeNode(150)), TreeNode(300)
    )
    print(inorder(t3))
    print(s := ser.serialize(t3))
    print(inorder(deser.deserialize(s)))

    print("Test 4")
    t4 = TreeNode(200, TreeNode(100), TreeNode(300, TreeNode(250), TreeNode(350)))
    print(inorder(t4))
    print(s := ser.serialize(t4))
    print(inorder(deser.deserialize(s)))


if __name__ == "__main__":
    main()
