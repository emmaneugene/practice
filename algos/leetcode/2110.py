# Problem: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
# tags: medium

# Time complexity: O(n)
# Space complexity: O(1)

from typing import List

class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0
        currVal = prices[0]
        currLen = 1

        for p in prices[1:]:
            if p == currVal - 1:
                currLen += 1
            else:
                res += int((1 + currLen) * currLen / 2)
                currLen = 1
            currVal = p

        res += int((1 + currLen) * currLen / 2)
        return res


def main():
    s = Solution()
    print(s.getDescentPeriods([3,2,1,4])) # Expected: 7
    print(s.getDescentPeriods([8,6,7,7])) # Expected: 4
    print(s.getDescentPeriods([1])) # Expected: 1


if __name__ == "__main__":
    main()
