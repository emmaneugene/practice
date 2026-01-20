# Problem: https://leetcode.com/problems/valid-sudoku/
# tags: medium

# Time complexity: O(1)
# Space complexity: O(1)

from typing import Dict, List, Set


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                occurrences: set = set()
                for row in range(i, i + 3):
                    for col in range(j, j + 3):
                        if board[row][col] != "." and board[row][col] in occurrences:
                            return False
                        occurrences.add(board[row][col])

        # Check rows
        for i in range(9):
            rowOccurrences: set = set()
            colOccurrences: set = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in rowOccurrences:
                    return False
                rowOccurrences.add(board[i][j])

                if board[j][i] != "." and board[j][i] in colOccurrences:
                    return False
                colOccurrences.add(board[j][i])

        return True


def main():
    s: Solution = Solution()

    board1: list[list[str]] = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    print(s.isValidSudoku(board1))  # Expected: True

    board2: list[list[str]] = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    print(s.isValidSudoku(board2))  # Expected: False


if __name__ == "__main__":
    main()
