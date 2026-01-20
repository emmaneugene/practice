# Problem: https://leetcode.com/problems/separate-squares-i/
# tags: medium

# Time complexity: O(n)
# Space complexity: O(nlogn)

from typing import List


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        area = sum([s[2] ** 2 for s in squares])

        changeDict = {}
        for s in squares:
            yStart = s[1]
            yEnd = s[1] + s[2]
            width = s[2]
            if yStart not in changeDict:
                changeDict[yStart] = 0
            changeDict[yStart] += width

            if yEnd not in changeDict:
                changeDict[yEnd] = 0
            changeDict[yEnd] -= width

        changeList = sorted([(k, v) for k, v in changeDict.items()])
        remaining = area / 2
        width = 0

        for i in range(len(changeList) - 1):
            width += changeList[i][1]
            y = changeList[i][0]
            nextY = changeList[i + 1][0]
            length = nextY - y
            nextChunk = width * length

            if nextChunk >= remaining:
                return y + (remaining / nextChunk * length)

            remaining -= nextChunk

        return -1


def main():
    s = Solution()
    print(s.separateSquares([[0, 0, 1], [2, 2, 1]])) # Expected: 1.000
    print(s.separateSquares([[0, 0, 2], [1, 1, 1]])) # Expected: 1.16667


if __name__ == "__main__":
    main()
