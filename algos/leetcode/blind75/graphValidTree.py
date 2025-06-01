# Problem: https://leetcode.com/problems/graph-valid-tree

import collections

# Time complexity: O(mn) for m nodes, n edges
# Space complexity: O(mn) for m nodes, n edges


class Solution:
    # cycle detection
    # tree: V count == E count + 1
    # cycle: V count !== E count + 1
    # disconnected graph: unvisited Vs
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        adj = {i: [] for i in range(n)}

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        q = collections.deque([])
        q.append(0)
        while q:
            # Visit next node
            cur = q.popleft()

            # Attempt to explore child nodes
            if cur not in adj:
                continue
            for n in adj[cur]:
                q.append(n)
            del adj[cur]

        return len(adj) == 0


def main():
    s = Solution()

    print(s.validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))  # True
    print(s.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))  # False


if __name__ == "__main__":
    main()
