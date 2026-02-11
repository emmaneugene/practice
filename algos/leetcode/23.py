#  Problem: https://leetcode.com/problems/merge-k-sorted-lists
# tags: blind75, hard

# Assumign n total elements, k lists:
# Time complexity: O(nlogk)
# Space complexity: O(n)
#
# Alternative solutions:
# 1. Brute force - collect all values, sort, build new list
#    Time: O(n log n) | Space: O(n)
# 2. Sequential merging - merge lists one by one
#    Time: O(nk) | Space: O(n)
# 3. Min-heap (all elements) - push all elements, pop to build result [implemented]
#    Time: O(n log n) | Space: O(n)
# 4. Min-heap (k elements) - maintain heap of k list heads
#    Time: O(n log k) | Space: O(k)
# 5. Divide and conquer - pairwise merge lists like merge sort [implemented]
#    Time: O(n log k) | Space: O(n)

import heapq
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge2Lists(self, list1: ListNode, list2: ListNode) -> ListNode:
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

        while t1 and t2:
            if t1.val < t2.val:
                curr.next = ListNode(t1.val, None)
                t1 = t1.next
            else:
                curr.next = ListNode(t2.val, None)
                t2 = t2.next
            curr = curr.next

        t3 = t1 if not t2 else t2
        while t3:
            curr.next = ListNode(t3.val, None)
            t3 = t3.next
            curr = curr.next

        return result

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        lists = list(filter(lambda x: x is not None, lists))

        if not lists:
            return None

        while len(lists) > 1:
            tmp: list[ListNode] = []
            for i in range(0, len(lists), 2):
                if i + 1 < len(lists):
                    tmp.append(self.merge2Lists(lists[i], lists[i + 1]))
                else:
                    tmp.append(lists[i])
            lists = tmp

        return lists[0]

    def mergeKLists2(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        """min-heap, add all, then pop all"""
        lists = list(filter(lambda x: x is not None, lists))

        if not lists:
            return None

        minHeap = []
        result = ListNode()
        curr = result

        for lst in lists:
            while lst:
                heapq.heappush(minHeap, lst.val)
                lst = lst.next

        while minHeap:
            val = heapq.heappop(minHeap)
            curr.next = ListNode(val)
            curr = curr.next

        return result.next


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

    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    l4 = None

    printList(s.mergeKLists([l1, l2, l3]))  # Expected: 1, 1, 2, 3, 4, 4, 5, 6
    printList(s.mergeKLists([]))  # Expected: <empty list>
    printList(s.mergeKLists([l4]))  # Expected: <empty list>

    printList(s.mergeKLists2([l1, l2, l3]))  # Expected: 1, 1, 2, 3, 4, 4, 5, 6
    printList(s.mergeKLists2([]))  # Expected: <empty list>
    printList(s.mergeKLists2([l4]))  # Expected: <empty list>


if __name__ == "__main__":
    main()
