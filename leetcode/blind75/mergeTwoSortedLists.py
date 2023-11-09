# Problem: https://leetcode.com/problems/merge-two-sorted-lists/

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

        track1 = list1
        track2 = list2

        result = None

        if track1.val < track2.val:
            result = ListNode(track1.val, None)
            track1 = track1.next
        else:
            result = ListNode(track2.val, None)
            track2 = track2.next

        track3 = result

        while track1 is not None and track2 is not None:
            if track1.val < track2.val:
                track3.next = ListNode(track1.val, None)
                track1 = track1.next
            else:
                track3.next = ListNode(track2.val, None)
                track2 = track2.next
            track3 = track3.next

        while track1 is not None:
            track3.next = ListNode(track1.val, None)
            track3 = track3.next
            track1 = track1.next
        while track2 is not None:
            track3.next = ListNode(track2.val, None)
            track3 = track3.next
            track2 = track2.next

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
