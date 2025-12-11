# Problem: https://leetcode.com/problems/count-covered-buildings/

# Time complexity: O(n)
# Space complexity: O(n)

from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        xRanges = {}
        yRanges = {}

        for x, y in buildings:
            if y not in xRanges:
                xRanges[y] = (x, x)
            else:
                xMin, xMax = xRanges[y]
                xMin = min(xMin, x)
                xMax = max(xMax, x)
                xRanges[y] = (xMin, xMax)

            if x not in yRanges:
                yRanges[x] = (y, y)
            else:
                yMin, yMax = yRanges[x]
                yMin = min(yMin, y)
                yMax = max(yMax, y)
                yRanges[x] = (yMin, yMax)

        res = 0
        for x, y in buildings:
            xMin, xMax = xRanges[y]
            yMin, yMax = yRanges[x]
            if x > xMin and x < xMax and y > yMin and y < yMax:
                res += 1
        return res


def main():
    s = Solution()
    print(
        s.countCoveredBuildings(5, [[1, 2], [2, 2], [3, 2], [2, 1], [2, 3]])
    )  # Expected: 1
    print(s.countCoveredBuildings(5, [[1, 1], [1, 2], [2, 1], [2, 2]]))  # Expected: 0
    print(
        s.countCoveredBuildings(5, [[1, 3], [3, 2], [3, 3], [3, 5], [5, 3]])
    )  # Expected: 1


if __name__ == "__main__":
    main()
