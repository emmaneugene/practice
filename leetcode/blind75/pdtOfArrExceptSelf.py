# Problem: https://leetcode.com/problems/product-of-array-except-self/

# Constraints: Cannot use division, algo must run in O(n) time

# Solution: Cached computations from left and right

# Time complexity: O(n)
# Space complexity: O(1) (excludes output array)

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out: List[int] = [1] * len(nums)

        # Multiply from left
        pdt: int = 1
        for i in range(len(nums)-1):
            pdt *= nums[i]
            out[i+1] *= pdt 

        # Multiply from right
        pdt = 1
        for i in range(len(nums)-1, 0, -1):
            pdt *= nums[i]
            out[i-1] *= pdt

        return out


def main():
    s: Solution = Solution()

    print(s.productExceptSelf([1, 2, 3, 4]))
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))


if __name__ == '__main__':
    main()
