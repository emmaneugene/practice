# Problem: https://leetcode.com/problems/search-a-2d-matrix/

# Time complexity: O(log(m+n))
# Space complexity: NA

import bisect

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if matrix[0][0] > target or matrix[-1][-1] < target:
            return False

        # Bisect rows to find row such that target > row[0] and target < row[1] 
        rowCount: int = len(matrix)
        colCount: int = len(matrix[0])
        start: int = 0
        end: int = len(matrix)
        rowIdx: int = 0

        while start < end:
            mid = start + (end-start)//2

            if target >= matrix[mid][0]:
                if mid == rowCount-1 or target < matrix[mid+1][0]:
                    rowIdx = mid
                    break
                start = mid+1
            else:
                end = mid

        # Bisect column
        colIdx: int = bisect.bisect_left(matrix[rowIdx], target)

        return colIdx < colCount and matrix[rowIdx][colIdx] == target


def main():
    s: Solution = Solution()

    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3)) # True
    print(s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13)) # False
    print(s.searchMatrix([[1],[3]], 2)) # False
    print(s.searchMatrix([[1],[3]], 3)) # Trus



if __name__ == '__main__':
    main()
