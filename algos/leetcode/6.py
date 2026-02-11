# Problem: https://leetcode.com/problems/zigzag-conversion/
# tags: medium

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. Simulate row-by-row - iterate and assign to rows [implemented]
#    Time: O(n) | Space: O(n)
# 2. Direct index mapping - compute output index per character mathematically
#    Time: O(n) | Space: O(n)

from typing import List


class Solution:
    def convert(self, s: str, nRows: int) -> str:
        strList: List[str] = [""] * nRows
        chunkSize = nRows + max(0, nRows - 2)

        for i in range(0, len(s), chunkSize):
            try:
                for j in range(nRows):
                    strList[j] += s[i + j]
                for k in range(nRows, chunkSize):
                    strList[-2 - (k % nRows)] += s[i + k]
            except IndexError:
                break

        return "".join(strList)


def main():
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))  # Expected: "PAHNAPLSIIGYIR"
    print(s.convert("PAYPALISHIRING", 4))  # Expected: "PINALSIGYAHRPI"
    print(s.convert("A", 1))  # Expected: "A"


if __name__ == "__main__":
    main()
