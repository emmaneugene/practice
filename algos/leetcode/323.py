# Problem: https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph
# tags: blind75, medium

# Time complexity: O(n)
# Space complexity: O(n)
# Iterate over each edge to create a list of components


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        # Map each node to a connected group
        nodeGrps: dict[int, set[int]] = {}
        toVisit: set[int] = {i for i in range(n)}

        count = 0
        for n1, n2 in edges:
            if n1 not in nodeGrps and n2 not in nodeGrps:
                # New group
                newGrp: list[int] = {n1, n2}
                nodeGrps[n1] = newGrp
                nodeGrps[n2] = newGrp
                count += 1
            elif n1 not in nodeGrps:
                nodeGrps[n1] = nodeGrps[n2]
                nodeGrps[n1].add(n1)
            elif n2 not in nodeGrps:
                nodeGrps[n2] = nodeGrps[n1]
                nodeGrps[n2].add(n2)
            else:
                # Merge 2 groups if no intersection found
                if len(nodeGrps[n1] & nodeGrps[n2]) == 0:
                    count -= 1

                newGrp: set[int] = nodeGrps[n1] | nodeGrps[n2]
                for i in newGrp:
                    nodeGrps[i] = newGrp

            if n1 in toVisit:
                toVisit.remove(n1)
            if n2 in toVisit:
                toVisit.remove(n2)

        return count + len(toVisit)


def main():
    s = Solution()

    print(s.countComponents(5, [[0, 1], [1, 2], [3, 4]]))  # Expected: 2
    print(s.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # Expected: 1
    print(s.countComponents(5, [[0, 1], [1, 2], [0, 2], [3, 4]]))  # Expected: 2


if __name__ == "__main__":
    main()
