# Problem: https://leetcode.com/problems/linked-list-cycle
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(1)

# Alternative solutions:
# 1. Hash set - store visited nodes in a set
#    Time: O(n) | Space: O(n)
# 2. Floyd's cycle detection (tortoise and hare) - slow/fast pointers
#    Time: O(n) | Space: O(1)
# 3. Link modification - redirect visited node pointers to head [implemented]
#    Time: O(n) | Space: O(1)

from typing import Optional


class ListNode:
    """Definition for singly-linked list."""

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        curr = head

        while curr.next:
            if curr.next == head:
                return True

            tmp = curr
            curr = curr.next
            tmp.next = head

        return False


def main():
    s = Solution()

    t1N1 = ListNode(3)
    t1N2 = ListNode(2)
    t1N3 = ListNode(0)
    t1N4 = ListNode(4)
    t1N1.next = t1N2
    t1N2.next = t1N3
    t1N3.next = t1N4
    t1N4.next = t1N2
    print(s.hasCycle(t1N1))  # Expected: True

    t2N1 = ListNode(1)
    t2N2 = ListNode(2)
    t2N1.next = t2N2
    t2N2.next = t2N1
    print(s.hasCycle(t2N1))  # Expected: True

    print(s.hasCycle(ListNode(1)))  # Expected: False


if __name__ == "__main__":
    main()
