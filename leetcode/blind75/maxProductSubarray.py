# Problem: https://leetcode.com/problems/maximum-product-subarray/

from typing import List


# Complexity: O(n)
class Solution:
    def getHighestProduct(self, nums: List[int]) -> int:
        """Returns highest product possible from `nums`"""
        if len(nums) == 1:
            return nums[0]

        result: int = nums[0]

        for i in range(1, len(nums)):
            result *= nums[i]

        if result > 0:
            return result

        # Find smallest negative divisor from left/right
        leftNeg: int = nums[0]
        idx: int = 1

        while leftNeg > 0:
            leftNeg *= nums[idx]
            idx += 1

        rightNeg: int = nums[-1]
        idx = len(nums) - 2

        while rightNeg > 0:
            rightNeg *= nums[idx]
            idx -= 1

        divisor = max(leftNeg, rightNeg)
        return int(result / divisor)

    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        result: int = max(nums)

        # Strip leading and trailing 0s
        stripStart: int = 0
        while nums[stripStart] == 0:
            stripStart += 1
        stripEnd: int = len(nums)
        while nums[stripEnd - 1] == 0:
            stripEnd -= 1

        nums = nums[stripStart:stripEnd]

        # Split array where 0s are encountered
        # [2,0,1,4,0,8] becomes [[2], [1,4], [8]]
        subarrs: List[List[int]] = []
        start: int = 0
        reset: bool = nums[0] == 0

        for i in range(1, len(nums)):
            if nums[i] == 0:
                if not reset and i > start:
                    subarrs.append(nums[start:i])
                reset = True
            else:
                if reset:
                    start = i
                    reset = False

        subarrs.append(nums[start:])

        for arr in subarrs:
            temp: int = self.getHighestProduct(arr)
            if result < temp:
                result = temp

        return result


def main():
    s: Solution = Solution()
    print(s.maxProduct([2, 3, -2, 4]))  # Expected: 6
    print(s.maxProduct([-2, 0, -1]))  # Expected: 0
    print(s.maxProduct([-2, -3, 0, -1]))  # Expected: 6
    print(s.maxProduct([0, -2, -3, 0, 0, -1]))  # Expected: 6
    print(s.maxProduct([0, 0, -2, -3, 0, 0, 0, -1, 0]))  # Expected: 6


if __name__ == "__main__":
    main()
