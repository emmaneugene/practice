#  Problem: https://leetcode.com/problems/merge-k-sorted-lists

# Assumign n total elements, k lists:
# Time complexity: O(nlogk)
# Space complexity: O(n)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: ListNode, list2: ListNode
    ) -> ListNode:

        t1 = list1
        t2 = list2

        result = None

        if t1.val < t2.val:
            result = ListNode(t1.val, None)
            t1 = t1.next
        else:
            result = ListNode(t2.val, None)
            t2 = t2.next
        curr = result

        while t1 is not None and t2 is not None:
            if t1.val < t2.val:
                curr.next = ListNode(t1.val, None)
                t1 = t1.next
            else:
                curr.next = ListNode(t2.val, None)
                t2 = t2.next
            curr = curr.next

        t3 = t1 if t2 is None else t2
        while t3 is not None:
            curr.next = ListNode(t3.val, None)
            t3 = t3.next
            curr = curr.next

        return result

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        lists = list(filter(lambda x: x is not None, lists))

        if len(lists) == 0:
            return None

        while len(lists) > 1:
            tmp: list[ListNode] = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    tmp.append(self.mergeTwoLists(lists[i], lists[i+1]))
                else:
                    tmp.append(lists[i])
            lists = tmp


        return lists[0]

def printList(x: Optional[ListNode]) -> None:
    if x == None:
        print("<empty list>")
        return

    print(f"{x.val}", end="")
    x = x.next

    while x is not None:
        print(f", {x.val}", end="")
        x = x.next

    print("")

def main():
    s: Solution = Solution()

    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    l4 = None

    printList(s.mergeKLists([l1, l2, l3])) # Expected: 1, 1, 2, 3, 4, 4, 5, 6
    printList(s.mergeKLists([])) # Expected: <empty list>
    printList(s.mergeKLists([l4])) # Expected: <empty list>


if __name__ == "__main__":
    main()
