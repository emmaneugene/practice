# Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(1)
# Dynamic programming with sliding window technique


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        start = 0
        end = 0

        for idx, val in enumerate(prices):
            if val < prices[start]:
                # Reset window
                if prices[end] - prices[start] > profit:
                    profit = prices[end] - prices[start]
                start = idx
                end = idx
            if val > prices[end]:
                end = idx

        if prices[end] - prices[start] > profit:
            profit = prices[end] - prices[start]
        return profit


def main():
    s = Solution()

    print(s.maxProfit([7, 1, 5, 3, 6, 4]))  # Expected: 5
    print(s.maxProfit([7, 6, 4, 3, 1]))  # Expected: 0


if __name__ == "__main__":
    main()
