# Problem: https://leetcode.com/problems/number-of-islands
# tags: blind75, medium

# Time complexity: O(mn)
# Space complexity: O(mn)


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    self.explore(grid, i, j)
                    count += 1
        return count

    def explore(self, grid, i, j):
        """Explore with DFS"""
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.explore(grid, i + 1, j)
        self.explore(grid, i - 1, j)
        self.explore(grid, i, j + 1)
        self.explore(grid, i, j - 1)


def main():
    s = Solution()

    grid: list[list[int]] = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    print(s.numIslands(grid))  # Expected: 1

    grid: list[list[int]] = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    print(s.numIslands(grid))  # Expected: 3


if __name__ == "__main__":
    main()
