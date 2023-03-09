# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# Recursive bisect with additional conditions
# Time: O(logn)
# Space: O(logn)

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mid: int = len(nums) // 2

        if nums[mid-1] > nums[mid]:
            return nums[mid]

        # Condition to search left
        if nums[mid] <= nums[-1]:
            return self.findMin(nums[:mid])

        return self.findMin(nums[mid+1:])


def main():
    s: Solution = Solution()

    print(s.findMin([3, 4, 5, 1, 2]))  # Expected: 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))  # Expected: 0
    print(s.findMin([11, 13, 15, 17]))  # Expected: 11
    print(s.findMin([5, 1, 2, 3, 4]))  # Expected: 1


if __name__ == '__main__':
    main()
