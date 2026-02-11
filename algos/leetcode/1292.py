# Problem: https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
# tags: medium

# Time complexity: O(m * n * min(m,n)^2) - for each square size, iterate all positions, getAdditionalSum is O(size)
# Space complexity: O(m * n) - tracker matrix copy
# Incrementally expands squares, tracking cumulative sums. Breaks early when no valid square of current size exists.

# Alternative solutions:
# 1. Brute force - compute sum for every possible square independently
#    Time: O(m * n * min(m,n)^3) | Space: O(1)
# 2. Incremental square expansion with early termination [implemented]
#    Time: O(m * n * min(m,n)^2) | Space: O(m * n)
# 3. 2D prefix sum + linear scan over side lengths
#    Time: O(m * n * min(m,n)) | Space: O(m * n)
# 4. 2D prefix sum + binary search on side length
#    Time: O(m * n * log(min(m,n))) | Space: O(m * n)

import copy
from typing import List


# Starting from smallest helps with precomputation
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        if not mat:
            return 0

        rows = len(mat)
        cols = len(mat[0])
        maxSqWidth = min(rows, cols)
        tracker: List[List[int]] = [copy.copy(row) for row in mat]

        def getAdditionalSum(mat: List[List[int]], row: int, col: int, size: int):
            """Return the sum that must be added if increasing a square
            starting at (row, col) from {size-1} to {size}
            """
            if size < 2:
                return 0

            res = 0
            # Add new row
            colIdx = col + size - 1
            for i in range(size - 1):
                res += mat[row + i][colIdx]

            # Add new col
            rowIdx = row + size - 1
            for j in range(size - 1):
                res += mat[rowIdx][col + j]

            return res + mat[rowIdx][colIdx]

        res = 0

        for w in range(maxSqWidth):
            for i in range(rows - w):
                for j in range(cols - w):
                    tracker[i][j] += getAdditionalSum(mat, i, j, w + 1)
                    if tracker[i][j] <= threshold:
                        res = max(res, w + 1)

            if res != w + 1:
                break

        return res


def main():
    s = Solution()
    print(
        s.maxSideLength(
            [[1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2], [1, 1, 3, 2, 4, 3, 2]], 4
        )
    )  # Expected: 2
    print(
        s.maxSideLength(
            [
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
            ],
            1,
        )
    )  # Expected: 0
    print(
        s.maxSideLength([[1, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 6)
    )  # Expected: 3


if __name__ == "__main__":
    main()
