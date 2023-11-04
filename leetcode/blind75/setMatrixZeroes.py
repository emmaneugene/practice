# Problem: https://leetcode.com/problems/set-matrix-zeroes/

# Time complexity: O(n^2)
# Space complexity: O(n)

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        markedRows: set[int] = set()
        markedCols: set[int] = set()

        # Check for zeros
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    markedRows.add(i)
                    markedCols.add(j)
        
        for row in markedRows:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        
        for col in markedCols:
            for i in range(len(matrix)):
                matrix[i][col] = 0


def main():
    s: Solution = Solution()


if __name__ == '__main__':
    main()
