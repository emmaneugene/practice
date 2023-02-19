#  Problem: https://leetcode.com/problems/merge-k-sorted-lists/
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Complexity: O(k * n)
class Solution:
    def getSmallest(self, lists: list[Optional[ListNode]]) -> int:
        '''Returns the smallest element of a list of linked lists
        and advances the corresponding pointer. If the next element is null,
        this function pops the empty linked list
        '''
        idxMin: int = 0

        for i in range(len(lists)):
            if lists[i].val < lists[idxMin].val:
                idxMin = i

        val = lists[idxMin].val
        lists[idxMin] = lists[idxMin].next

        if lists[idxMin] is None:
            lists.pop(idxMin)

        return val
                
    
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        lists = list(filter(lambda x: x is not None, lists))

        if len(lists) == 0:
            return None

        # One iteration to get head
        val = self.getSmallest(lists)

        head: ListNode = ListNode(val)
        current: ListNode = head

        while len(lists) > 0:
            val = self.getSmallest(lists)
            current.next = ListNode(val)
            current = current.next
        
        return head


def main():
    pass


if __name__ == '__main__':
    main()