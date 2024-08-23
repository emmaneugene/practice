# Problem: https://leetcode.com/problems/reverse-linked-list

# Time complexity: O(n)
# Space complexity: O(n)


from typing import Optional


class ListNode:
    """Definition for a singly-linked list"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead: Optional[ListNode] = None
        if head is None:
            return reversedHead

        while head.next is not None:
            reversedHead = ListNode(head.val, reversedHead)
            head = head.next

        return ListNode(head.val, reversedHead)
