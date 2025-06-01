# Problem: https://leetcode.com/problems/merge-two-sorted-lists

# Assuming n elemeents in total:
# Time complexity: O(n)
# Space complexity: O(n)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # Corner cases
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1

        t1, t2 = list1, list2
        result: Optional[ListNode]

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


def printList(x: Optional[ListNode]) -> None:
    if not x:
        print("<empty list>")
        return

    print(f"{x.val}", end="")
    x = x.next

    while x:
        print(f", {x.val}", end="")
        x = x.next

    print("")


def main():
    s = Solution()

    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))

    printList(s.mergeTwoLists(l1, l2))  # Expected: 1, 1, 2, 3, 4, 4

    printList(s.mergeTwoLists(None, None))  # Expected: <empty list>

    printList(s.mergeTwoLists(None, ListNode(0)))  # Expected: 0


if __name__ == "__main__":
    main()
