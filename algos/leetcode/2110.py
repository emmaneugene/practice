# Problem: https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/
# tags: medium

# Time complexity: O(n)
# Space complexity: O(1)

# Alternative solutions:
# 1. Brute force - enumerate all subarrays, check each for smooth descent
#    Time: O(n^2) | Space: O(1)
# 2. Dynamic programming - DP array tracking descent length at each index
#    Time: O(n) | Space: O(n)
# 3. Greedy with math - track consecutive descent length, sum contributions [implemented]
#    Time: O(n) | Space: O(1)

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
