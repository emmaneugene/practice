# Problem: https://leetcode.com/problems/reorder-list
# tags: blind75, medium

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. Array of nodes - store all nodes, stitch from both ends [implemented]
#    Time: O(n) | Space: O(n)
# 2. Recursion - use call stack to access nodes from end
#    Time: O(n) | Space: O(n)
# 3. Find middle + reverse second half + merge - slow/fast pointers, in-place reversal
#    Time: O(n) | Space: O(1)

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Do not return anything, modify head in-place instead."""

        if not head:
            return

        nodes: list[ListNode] = []

        tmp = head
        while tmp:
            nodes.append(tmp)
            tmp = tmp.next

        track = head
        sliceEnd = len(nodes) // 2

        # Stitch nodes
        for node in nodes[len(nodes) - 1 : sliceEnd : -1]:
            tmp = track.next
            track.next = node
            node.next = tmp
            track = tmp

        if len(nodes) % 2 == 0:
            track.next.next = None
        else:
            track.next = None


def llToString(head: Optional[ListNode]) -> str:
    out: str = ""

    if head is None:
        return out

    out += str(head.val)

    while head.next is not None:
        head = head.next
        out += f"->{head.val}"

    return out


def main():
    s = Solution()

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    print(f"Original : {llToString(head)}")
    s.reorderList(head)
    print(f"Reordered: {llToString(head)}")

    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(f"Original : {llToString(head)}")
    s.reorderList(head)
    print(f"Reordered: {llToString(head)}")


if __name__ == "__main__":
    main()
