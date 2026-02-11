# Problem: https://leetcode.com/problems/maximum-product-subarray
# tags: blind75, medium

# Time complexity: O(n)
# Space complexity: O(1)

# Alternative solutions:
# 1. Brute force - check all subarrays
#    Time: O(n^2) | Space: O(1)
# 2. Track min/max product DP - maintain running min and max products [implemented]
#    Time: O(n) | Space: O(1)


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        out = nums[0]
        candidatePos = nums[0]
        candidateNeg = nums[0]

        for n in nums[1:]:
            if n < 0:
                tmp = candidatePos
                candidatePos = candidateNeg * n
                candidateNeg = tmp * n
                candidateNeg = min(candidateNeg, n)
            elif n > 0:
                candidatePos *= n
                candidateNeg *= n
                candidatePos = max(candidatePos, n)
            else:
                candidatePos = candidateNeg = n
            out = max(out, candidatePos)

        return out


def main():
    s = Solution()

    print(s.maxProduct([2, 3, -2, 4]))  # Expected: 6
    print(s.maxProduct([-2, 0, -1]))  # Expected: 0
    print(s.maxProduct([-2, -3, 0, -1]))  # Expected: 6
    print(s.maxProduct([0, -2, -3, 0, 0, -1]))  # Expected: 6
    print(s.maxProduct([0, 0, -2, -3, 0, 0, 0, -1, 0]))  # Expected: 6


if __name__ == "__main__":
    main()
