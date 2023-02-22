# Problem: https://leetcode.com/problems/spiral-matrix/

from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows: int = len(matrix)
        cols: int = len(matrix[0])

        # Edge cases:
        if rows == 1:
            return matrix[0]
        if cols == 1:
            return [matrix[i][0] for i in range(rows)]

        numIters = min(rows//2, cols//2)

        output: List[int] = []
        for i in range(numIters):

            # Top (left-right)
            for k in range(i, cols-i):
                output.append(matrix[i][k])

            # Right (up-down)
            for k in range(i+1, rows-i-1):
                output.append(matrix[k][cols-1-i])

            # Bottom(right-left)
            for k in range(cols-1-i, -1+i, -1):
                output.append(matrix[rows-1-i][k])

            # Left (down-up)
            for k in range(rows-2-i, i, -1):
                output.append(matrix[k][i])

        # Handle remainder (middle row/column)
        for row in range(numIters, rows-numIters):
            for col in range(numIters, cols-numIters):
                output.append(matrix[row][col])

        
        return output


def main():
    s: Solution = Solution()

    print(s.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8]]))
    print(s.spiralOrder([[7],[9],[6]]))
    print(s.spiralOrder([[1,2,3]]))
    print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]))

if __name__ == '__main__':
    main()