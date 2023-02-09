from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversedHead: Optional[ListNode] = None
        if head is None:
            return reversedHead

        while head.next is not None:
            temp = ListNode(head.val, reversedHead)
            reversedHead = temp
            head = head.next

        return ListNode(head.val, reversedHead)
 

def main():
    s = Solution()

    print("Expected: [1,2,3,4,5]")
    print("Output  : ")

if __name__=="__main__":
    main()