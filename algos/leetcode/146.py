# Problem: https://leetcode.com/problems/lru-cache
# tags: medium

# Time complexity: O(1) for every operation
# Space complexity: O(n)

# Alternative solutions:
# 1. OrderedDict - Python's built-in ordered dictionary
#    Time: O(1) | Space: O(n)
# 2. Hashmap + doubly-linked list - manual DLL for ordering [implemented]
#    Time: O(1) | Space: O(n)

# Use a doubly-linked list to keep track of most recent units
from typing import Optional


class ListNode:
    def __init__(self, key: int, val: int, prev=None, next=None) -> None:
        self.key: int = key
        self.val: int = val
        self.prev = prev
        self.next = next


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.items: dict[int, ListNode] = {}
        self.capacity: int = capacity
        self.length: int = 0
        self.head: ListNode = None
        self.tail: ListNode = None

    def get(self, key: int) -> int:
        if key not in self.items:
            return -1

        node: ListNode = self.items[key]

        if node is self.head:
            return node.val

        # Move item to most recently used
        if node is self.tail:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

        return node.val

    def put(self, key: int, value: int) -> None:
        # Coener case - empty cache
        if self.length == 0:
            self.head = ListNode(key, value)
            self.tail = self.head
            self.length += 1
            self.items[key] = self.head
            return

        # Corner case - single entry update
        if self.length == 1 and key in self.items:
            self.head.val = value
            return

        # Remove entry if it exists
        if key in self.items:
            node: ListNode = self.items.pop(key)

            if self.head is node:
                self.head = self.head.next
                self.head.prev = None
            elif self.tail is node:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                node.prev.next = node.next
                node.next.prev = node.prev

            del node
            self.length -= 1

        newNode = ListNode(key, value, None, self.head)
        self.items[key] = newNode
        self.head.prev = newNode
        self.head = newNode
        self.length += 1

        # Evict LRU if capacity exceeded
        if self.length > self.capacity:
            toRemove: ListNode = self.tail
            self.tail = self.tail.prev
            toRemove.prev = None
            self.tail.next = None
            self.length -= 1
            self.items.pop(toRemove.key)

    def __repr__(self) -> str:
        if not self.head:
            return "<empty cache>"

        track: ListNode = self.head
        out: str = ""
        while track:
            out += f"{track.key}:{track.val} <-> "
            track = track.next

        return out


def main():
    # Test case 1
    print("\n --------------- Test 1 ---------------")
    c: LRUCache = LRUCache(2)
    print(f"Init cache: {c}")

    c.put(1, 1)
    print(f"put(1,1): {c}")

    c.put(2, 2)
    print(f"put(2,2): {c}")

    print(f"get(1): {c.get(1)}")  # 1
    print(f"cache: {c}")

    c.put(3, 3)
    print(f"put(3,3): {c}")

    print(f"get(2): {c.get(2)}")  # -1
    print(f"cache: {c}")

    c.put(4, 4)
    print(f"put(4,4): {c}")

    print(f"get(1): {c.get(1)}")  # -1
    print(f"cache: {c}")

    print(f"get(3): {c.get(3)}")  # 3
    print(f"cache: {c}")

    print(f"get(4): {c.get(4)}")  # 4
    print(f"cache: {c}")


if __name__ == "__main__":
    main()
