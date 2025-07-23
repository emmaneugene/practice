# Problem: https://leetcode.com/problems/pacific-atlantic-water-flow

# Time complexity: O()
# Space complexity: O(mn)

from typing import List, Set


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        canVisitPac, canVisitAtl = set(), set()

        def dfs(r: int, c: int, visited: Set[int], prevHeight: int):
            if (
                r < 0
                or c < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visited
                or heights[r][c] < prevHeight
            ):
                return

            visited.add((r, c))
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, canVisitPac, heights[r][0])
            dfs(r, COLS - 1, canVisitAtl, heights[r][COLS - 1])

        for c in range(COLS):
            dfs(0, c, canVisitPac, heights[0][c])
            dfs(ROWS - 1, c, canVisitAtl, heights[ROWS - 1][c])

        return list(canVisitPac.intersection(canVisitAtl))


def main():
    s = Solution()

    print(
        s.pacificAtlantic(
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ]
        )
    )
    # Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    print(s.pacificAtlantic([[1]]))
    # Expected: [[0,0]]


if __name__ == "__main__":
    main()
