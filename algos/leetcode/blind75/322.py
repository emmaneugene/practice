# Problem: https://leetcode.com/problems/coin-change

# Time complexity: O(m*n)
# Space complexity: O(m+n)
# Dynamic programming, find optimal selection of m possible coins for amounts (1...n)


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        amtCounts: list[int] = [-1] * (amount + 1)
        amtCounts[0] = 0

        for amt in range(1, amount + 1):
            found = False
            amtCount = -1
            for c in coins:
                if c <= amt and amtCounts[amt - c] != -1:
                    tmp = amtCounts[amt - c] + 1
                    if not found:
                        amtCount = tmp
                        found = True
                    else:
                        if tmp < amtCount:
                            amtCount = tmp

            amtCounts[amt] = amtCount

        return amtCounts[amount]


def main():
    s = Solution()

    print(s.coinChange([1, 2, 5], 11))  # Expected: 3
    print(s.coinChange([2], 3))  # Expected: -1
    print(s.coinChange([1], 0))  # Expected: 0


if __name__ == "__main__":
    main()
