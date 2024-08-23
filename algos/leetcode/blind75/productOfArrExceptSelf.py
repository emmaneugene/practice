# Problem: https://leetcode.com/problems/product-of-array-except-self

# Constraints: Cannot use division, algo must run in O(n) time

# Time complexity: O(n)
# Space complexity: O(n)


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
    s: Solution = Solution()

    print(s.productExceptSelf([1, 2, 3, 4]))
    print(s.productExceptSelf([-1, 1, 0, -3, 3]))


if __name__ == "__main__":
    main()
