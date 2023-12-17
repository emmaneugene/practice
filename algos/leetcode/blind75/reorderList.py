# Problem: https://leetcode.com/problems/reorder-list

# Constraints: Do not modify node values, only nodes themselves

# Time complexity: O(n)
# Space complexity: O(n)

from typing import List, Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Do not return anything, modify head in-place instead."""

        if head is None:
            return

        nodes: List[ListNode] = []

        tmp: ListNode = head
        while tmp is not None:
            nodes.append(tmp)
            tmp = tmp.next

        # Insert (n, n-1, n-2, n // 2 + 1) nodes after (1, 2, 3, ... n // 2)
        curr: ListNode = head

        sliceEnd: int = len(nodes) // 2

        for node in nodes[len(nodes) - 1 : sliceEnd : -1]:
            tmp = curr.next
            curr.next = node
            node.next = tmp
            curr = tmp

        if len(nodes) % 2 == 0:
            curr.next.next = None
        else:
            curr.next = None


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
    s: Solution = Solution()

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
