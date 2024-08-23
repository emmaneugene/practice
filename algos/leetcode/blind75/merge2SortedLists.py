# Problem: https://leetcode.com/problems/merge-two-sorted-lists

# Time complexity: O(m+n)
# Space complexity: O(m+n)

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Corner case
        if list1 is None and list2 is None:
            return None
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1

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
            curr = curr.next
            t3 = t3.next

        return result


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

    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    printList(s.mergeTwoLists(l1, l2))  # Expected: 1, 1, 2, 3, 4, 4

    printList(s.mergeTwoLists(None, None))  # Expected: <empty list>

    printList(s.mergeTwoLists(None, ListNode(0)))  # Expected: 0


if __name__ == "__main__":
    main()
