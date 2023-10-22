# Problem: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Time complexity: O(n)
# Space complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# One-pass solution using 2 pointers
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        forward = head
        for i in range(n):
            forward = forward.next
        
        # Corner case - n is length of linked list
        if forward == None:
            return head.next
        
        forward = forward.next
        track = head

        while forward != None:
            forward = forward.next
            track = track.next
        
        track.next = track.next.next
        
        return head


def printList(x: Optional[ListNode]) -> None:
    if x == None: 
        print("<empty list>")
        return
    
    print(f"{x.val}", end='')
    x = x.next

    while x is not None:
        print(f", {x.val}", end='')
        x = x.next

    print("")


def main():
    s: Solution = Solution()

    l1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    l1 = s.removeNthFromEnd(l1, 2)
    printList(l1) # Expected: 1, 2, 3, 5

    l2 = ListNode(1)
    l2 = s.removeNthFromEnd(l2, 1)
    printList(l2) # Expected: <empty list>
    
    l3 = ListNode(1, ListNode(2))
    l3 = s.removeNthFromEnd(l3, 1)
    printList(l3) # Expected: 1



if __name__ == '__main__':
    main()
