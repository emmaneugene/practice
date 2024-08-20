# Problem: https://leetcode.com/problems/clone-graph

# Time complexity: O(V+E)
# Space complexity: O(V)
# Clone using BFS

from typing import Optional
import collections


class Node:
    def __init__(self, val=0, neighbors=None) -> None:
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
        pass


class Solution:
    def cloneGraph(self, node: Optional[Node]) -> Node:
        if not node:
            return node

        q = collections.deque([node])
        clones: dict = {node.val: Node(node.val, [])}

        while q:
            cur: Node = q.popleft()
            cur_clone: Node = clones[cur.val]

            for nb in cur.neighbors:
                if nb.val not in clones:
                    clones[nb.val] = Node(nb.val, [])
                    q.append(nb)

                cur_clone.neighbors.append(clones[nb.val])

        return clones[node.val]


def main():
    s: Solution = Solution()


if __name__ == "__main__":
    main()
