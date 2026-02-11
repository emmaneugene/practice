# Problem: https://leetcode.com/problems/reverse-linked-list
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. Iterative with new nodes - build reversed list by copying [implemented]
#    Time: O(n) | Space: O(n)
# 2. Recursive - reverse rest of list, fix pointers
#    Time: O(n) | Space: O(n) recursion stack
# 3. Iterative in-place - three pointers (prev, curr, next), reverse links
#    Time: O(n) | Space: O(1)


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
