# Problem: https://leetcode.com/problems/clone-graph
# tags: blind75, medium

# Time complexity: O(V+E)
# Space complexity: O(V)
# Clone using BFS

from typing import Optional
import collections


class Node:
    def __init__(self, val: int = 0, neighbors: list["Node"] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Optional[Node]:
        if not node:
            return node

        copies: dict[int, Node] = {node.val: Node(node.val)}
        q = collections.deque([node])

        while q:
            n = q.popleft()
            nCopy = copies.get(n.val, Node(n.val))

            for nb in n.neighbors:
                if nb.val not in copies:
                    copies[nb.val] = Node(nb.val)
                    q.append(nb)

                nCopy.neighbors.append(copies[nb.val])

        return copies[node.val]


def printAdjList(node: Optional[Node]) -> None:
    if not node:
        print([])
        return

    tracker: dict[int, list[int]] = {}
    q = collections.deque([node])

    while q:
        tmp = q.popleft()
        if tmp.val not in tracker:
            tracker[tmp.val] = [n.val for n in tmp.neighbors]
            q.extend([n for n in tmp.neighbors])

    print([x[1] for x in sorted(list(tracker.items()))])


def main():
    s = Solution()

    n1 = Node(1)
    n3 = Node(3)
    n2 = Node(2, [n1, n3])
    n4 = Node(4, [n1, n3])
    n1.neighbors = [n2, n4]
    n3.neighbors = [n2, n4]

    printAdjList(s.cloneGraph(n1))
    printAdjList(s.cloneGraph(Node(1)))
    printAdjList(s.cloneGraph(None))


if __name__ == "__main__":
    main()
