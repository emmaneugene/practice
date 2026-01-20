# Problem: https://leetcode.com/problems/reverse-nodes-in-k-group/description/
# tags: hard
# Time complexity: O(n)
# Space complexity: O(n)

from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k < 2:
            return head

        # First iteration
        track = head
        for _ in range(k):
            track = track.next

        curr = head
        newHead = track
        while curr != track:
            tmp = curr
            curr = curr.next
            tmp.next = newHead
            newHead = tmp

        newTail = newHead
        for _ in range(k - 1):
            newTail = newTail.next

        while track:
            do = True
            for _ in range(k):
                if not track:
                    do = False
                    break
                track = track.next
            if not do:
                break

            curr = newTail.next
            newHead2 = track
            while curr != track:
                tmp = curr
                curr = curr.next
                tmp.next = newHead2
                newHead2 = tmp

            newTail.next = newHead2
            for _ in range(k):
                newTail = newTail.next

        return newHead


def printList(n: Optional[ListNode]) -> None:
    while n:
        print(f"{n.val}->", end="")
        n = n.next
    print("")


def parseToList(vals: List[int]):
    if not vals or len(vals) == 0:
        return None

    head = ListNode(vals[0])
    tmp = head
    for v in vals[1:]:
        tmp.next = ListNode(v)
        tmp = tmp.next

    return head


def main():
    s = Solution()

    printList(s.reverseKGroup(parseToList([1, 2, 3, 4, 5]), 2))
    printList(s.reverseKGroup(parseToList([1, 2, 3, 4, 5]), 3))
    printList(s.reverseKGroup(parseToList([1, 2, 3, 4]), 2))


if __name__ == "__main__":
    main()
