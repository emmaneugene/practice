# Problem: https://leetcode.com/problems/coin-change

# Dynamic programming, find optimal selection of m possible coins for amounts (1...n)
# Time complexity: O(m*n)
# Space complexity: O(m+n)

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        optimalCounts: List[int] = [-1] * (amount + 1)
        optimalCounts[0] = 0

        for i in range(1, amount + 1):
            foundValid: bool = False
            toAdd: int = -1
            for c in coins:
                if c <= i and optimalCounts[i - c] != -1:
                    temp = optimalCounts[i - c] + 1
                    if not foundValid:
                        toAdd = temp
                        foundValid = True
                    else:
                        if temp < toAdd:
                            toAdd = temp

            optimalCounts[i] = toAdd

        return optimalCounts[amount]


def main():
    s: Solution = Solution()

    print(s.coinChange([1, 2, 5], 11))  # Expected: 3
    print(s.coinChange([2], 3))  # Expected: -1
    print(s.coinChange([1], 0))  # Expected: 0


if __name__ == "__main__":
    main()
