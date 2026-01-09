# Problem: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

# Time complexity: O(n)
# Space complexity: O(n)
# Recursive function call to find max left and right depth of each node, build a lookup dictionary,
# then search from root, navigating to deeper child, until left and right depths match

from typing import Dict, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: Optional["TreeNode"]=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        def getMaxDepth(node: "TreeNode", tracker: Dict) -> int:
            if not node.left and not node.right:
                tracker[node.val] = (0, 0)
                return 1

            if not node.left:
                res = getMaxDepth(node.right, tracker)
                tracker[node.val] = (0, res)
                return res + 1

            if not node.right:
                res = getMaxDepth(node.left, tracker)
                tracker[node.val] = (res, 0)
                return res + 1

            lDepth = getMaxDepth(node.left, tracker)
            rDepth = getMaxDepth(node.right, tracker)


            tracker[node.val] = (lDepth, rDepth)
            return max(lDepth, rDepth) + 1

        tracker = {}
        getMaxDepth(root, tracker)

        curr = root
        lrDepths = tracker[curr.val]
        while lrDepths[0] != lrDepths[1]:
            if lrDepths[0] > lrDepths[1]:
                curr = curr.left
            else:
                curr = curr.right
            lrDepths = tracker[curr.val]

        return curr

def main():
    s = Solution()

    # Test 1: [3,5,1,6,2,0,8,null,null,7,4] -> node 2 (deepest nodes are 7,4)
    #         3
    #        / \
    #       5   1
    #      / \ / \
    #     6  2 0  8
    #       / \
    #      7   4
    n7 = TreeNode(7)
    n4 = TreeNode(4)
    n2 = TreeNode(2, n7, n4)
    n6 = TreeNode(6)
    n5 = TreeNode(5, n6, n2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n1 = TreeNode(1, n0, n8)
    n3 = TreeNode(3, n5, n1)
    assert s.subtreeWithAllDeepest(n3).val == 2, "Test 1 failed"

    # Test 2: Single node [1] -> node 1
    single = TreeNode(1)
    assert s.subtreeWithAllDeepest(single).val == 1, "Test 2 failed"

    # Test 3: [0,1,3,null,2] -> node 2 (only deepest node)
    #       0
    #      / \
    #     1   3
    #      \
    #       2
    t3_n2 = TreeNode(2)
    t3_n1 = TreeNode(1, None, t3_n2)
    t3_n3 = TreeNode(3)
    t3_n0 = TreeNode(0, t3_n1, t3_n3)
    assert s.subtreeWithAllDeepest(t3_n0).val == 2, "Test 3 failed"

    # Test 4: None -> None
    assert s.subtreeWithAllDeepest(None) is None, "Test 4 failed"

    # Test 5: Equal depth on both sides -> root
    #       1
    #      / \
    #     2   3
    t5_n2 = TreeNode(2)
    t5_n3 = TreeNode(3)
    t5_n1 = TreeNode(1, t5_n2, t5_n3)
    assert s.subtreeWithAllDeepest(t5_n1).val == 1, "Test 5 failed"

    print("All tests passed!")


if __name__ == "__main__":
    main()
