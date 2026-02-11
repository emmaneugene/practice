# Problem: https://leetcode.com/problems/product-of-array-except-self
# tags: blind75, medium

# Constraints: Cannot use division, algo must run in O(n) time

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. Brute force - nested loops, multiply all except self
#    Time: O(n^2) | Space: O(1)
# 2. Division - total product / each element (fails with zeros)
#    Time: O(n) | Space: O(1)
# 3. Prefix and suffix product arrays - two extra arrays
#    Time: O(n) | Space: O(n)
# 4. Left-right running product in single output array - two passes [implemented]
#    Time: O(n) | Space: O(1) excluding output


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        out: list[int] = [1] * len(nums)

        # Multiply from left
        pdt = 1
        for i in range(len(nums) - 1):
            pdt *= nums[i]
            out[i + 1] *= pdt

        # Multiply from right
        pdt = 1
        for i in range(len(nums) - 1, 0, -1):
            pdt *= nums[i]
            out[i - 1] *= pdt

        return out


def main():
    s = Solution()

    print(s.productExceptSelf([1, 2, 3, 4]))  # Expected: [24, 12, 8, 6]
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))  # Expected: [0, 0, 9, 0, 0]


if __name__ == "__main__":
    main()
