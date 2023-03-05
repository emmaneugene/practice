# Problem: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

# Iterate over each edge to create a list of components

from typing import Dict, List, Set

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Maps each node to a group of connected nodes
        nodeConnections: Dict[int, Set[int]] = {}
        unvisited: Set[int] = {i for i in range(n)}
        
        count: int = 0
        for n1, n2 in edges:
            if n1 not in nodeConnections and n2 not in nodeConnections:
                # New connected group
                newGroup: List[int] = {n1, n2}
                nodeConnections[n1] = newGroup
                nodeConnections[n2] = newGroup 
                count += 1
            elif n1 not in nodeConnections:
                # Add to existing group
                nodeConnections[n1] = nodeConnections[n2]
                nodeConnections[n1].add(n1)
            elif n2 not in nodeConnections:
                # Add to existing group
                nodeConnections[n2] = nodeConnections[n1]
                nodeConnections[n2].add(n2)
            else:
                # Merge 2 existing group
                if len(nodeConnections[n1] & nodeConnections[n2]) == 0:
                    count -= 1

                newGroup: Set(int) = nodeConnections[n1] | nodeConnections[n2]
                for i in newGroup:
                    nodeConnections[i] = newGroup

            if n1 in unvisited:
                unvisited.remove(n1)
            if n2 in unvisited:
                unvisited.remove(n2)

        return count + len(unvisited)

def main():
    s: Solution = Solution()

    print(s.countComponents(5, [[0,1],[1,2],[3,4]])) # Expected: 2
    print(s.countComponents(5, [[0,1],[1,2],[2,3],[3,4]])) # Expected: 1
    print(s.countComponents(5, [[0,1],[1,2],[0,2],[3,4]])) # Expected: 2

if __name__ == '__main__':
    main()
