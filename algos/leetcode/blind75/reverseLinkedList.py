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
        rvsHead: Optional[ListNode] = None
        if not head:
            return rvsHead

        while head.next:
            rvsHead = ListNode(head.val, rvsHead)
            head = head.next

        return ListNode(head.val, rvsHead)
