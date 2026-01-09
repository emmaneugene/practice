# Problem: https://leetcode.com/problems/max-dot-product-of-two-subsequences/

# Time complexity: O(m * n)
# Space complexity: O(n)
#  dp[i][j] = max(
#      dp[i-1][j],           # skip nums1[i]
#      dp[i][j-1],           # skip nums2[j]
#      nums1[i] * nums2[j],  # start fresh with this pair
#      dp[i-1][j-1] + nums1[i] * nums2[j]  # extend previous
#  )
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        dp = [float("-inf")] * n

        for i in range(m):
            prev_diag = float("-inf")
            for j in range(n):
                temp = dp[j]  # dp[i-1][j] before overwrite
                curr = nums1[i] * nums2[j]

                dp[j] = curr  # start fresh with this pair
                if i > 0 and j > 0:
                    dp[j] = max(dp[j], prev_diag + curr)  # extend previous
                if i > 0:
                    dp[j] = max(dp[j], temp)  # skip nums1[i]
                if j > 0:
                    dp[j] = max(dp[j], dp[j - 1])  # skip nums2[j]

                prev_diag = temp

        return int(dp[n - 1])


def main():
    s = Solution()
    print(s.maxDotProduct([2, 1, -2, 5], [3, 0, -6]))  # Expected: 18
    print(s.maxDotProduct([3, -2], [2, -6, 7]))  # Expected: 21
    print(s.maxDotProduct([-5, -1, -2], [3, 3, 5, 5]))  # Expected: -3


if __name__ == "__main__":
    main()
