# Problem: https://leetcode.com/problems/set-matrix-zeroes
# tags: blind75, medium

# Time complexity: O(n^2)
# Space complexity: O(n)


class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead
        """

        rowsToZero: set[int] = set()
        colsToZero: set[int] = set()

        # Check for zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rowsToZero.add(i)
                    colsToZero.add(j)

        for row in rowsToZero:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0

        for col in colsToZero:
            for i in range(len(matrix)):
                matrix[i][col] = 0


def main():
    s = Solution()

    m1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    s.setZeroes(m1)
    print(m1)  # Expected: [[1,0,1],[0,0,0],[1,0,1]]

    m2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
    s.setZeroes(m2)
    print(m2)  # Expected: [0,0,0,0],[0,4,5,0],[0,3,1,0]


if __name__ == "__main__":
    main()
