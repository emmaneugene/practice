# Problem: https://leetcode.com/problems/linked-list-cycle

# Time complexity: O(n)
# Space complexity: O(1)

from typing import Optional, Set

class ListNode:
    '''Definition for singly-linked list.
    '''
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        curr: ListNode = head

        while curr.next is not None:
            if curr.next == head:
                return True
            
            tmp: ListNode = curr
            curr = curr.next
            tmp.next = head
            
        return False