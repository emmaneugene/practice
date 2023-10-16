# Problem: https://leetcode.com/problems/number-of-islands/

from typing import List

# TODO: Unimpl


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows: int = len(grid)
        cols: int = len(grid[0])

        visited: List[List[bool]] = [[False] * cols for i in range(rows)]
        print(visited)

        return 0
        
def main():
    s: Solution = Solution()

    grid: List[List[int]] = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(s.numIslands(grid)) # Expected: 1

    grid: List[List[int]] = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(s.numIslands(grid)) # Expected: 3

if __name__ == '__main__':
    main()