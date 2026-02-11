# Problem: https://leetcode.com/problems/graph-valid-tree
# tags: blind75, medium

import collections

# Time complexity: O(mn) for m nodes, n edges
# Space complexity: O(mn) for m nodes, n edges

# Alternative solutions:
# 1. BFS - build adjacency list, BFS to check connectivity + edge count [implemented]
#    Time: O(V + E) | Space: O(V + E)
# 2. DFS - build adjacency list, DFS to check connectivity + edge count
#    Time: O(V + E) | Space: O(V + E)
# 3. Union-Find - union nodes by edges, check single component + edge count
#    Time: O(E * α(V)) | Space: O(V)


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
