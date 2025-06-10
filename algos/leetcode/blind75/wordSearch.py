# Problem: https://leetcode.com/problems/word-search

# Time complexity: O(m^2n^2)
# Space complexity: O(mn)

# Approach 1: DFS + Backtracking (Most Common)
# Time: O(N * 4^L) where N = cells in board, L = length of word
# Space: O(L) for recursion stack
class Solution:

    def exist(self, board, word):
        if not board or not board[0] or not word:
            return False

        rows, cols = len(board), len(board[0])

        def dfs(row, col, idx):
            # Base case: found the complete word
            if idx == len(word):
                return True

            # Check bounds and character match
            if (row < 0 or row >= rows or
                col < 0 or col >= cols or
                board[row][col] != word[idx]):
                return False

            # Mark current cell as visited
            temp = board[row][col]
            board[row][col] = '#'  # or any marker that's not in the word

            # Explore all 4 directions
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            found = False
            for dr, dc in directions:
                if dfs(row + dr, col + dc, idx + 1):
                    found = True
                    break

            # Backtrack: restore the original character
            board[row][col] = temp
            return found

        # Try starting from each cell
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False

def main():
    s = Solution()

    print(
        s.exist(
            [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
            ], "ABCCED"
        )
    )  # Expected: True

    print(
        s.exist(
            [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
            ], "SEE"
        )
    )  # Expected: True

    print(
        s.exist(
            [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
            ], "ABCS"
        )
    )  # Expected: False

    print(
        s.exist(
            [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
            ], "ABCB"
        )
    )  # Expected: False

    print(
        s.exist(
            [
            ["A", "B", "C", "E"],
            ["S", "F", "E", "S"],
            ["A", "D", "E", "E"]
            ],"ABCESEEEFS",
        )
    )  # Expected: True

    print(
        s.exist(
            [
            ["A", "B", "C", "E"],
            ["S", "F", "E", "S"],
            ["A", "D", "E", "E"]
            ], "Z")
    )  # Expected: False


if __name__ == "__main__":
    main()
