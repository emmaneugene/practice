# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
# tags: blind75, medium

# Time complexity: O(logn)
# Space complexity: O(log n) - recursion stack
# Recursive bisect with additional conditions

# Alternative solutions:
# 1. Linear scan - iterate through array
#    Time: O(n) | Space: O(1)
# 2. Iterative binary search - two pointers narrowing on pivot
#    Time: O(log n) | Space: O(1)
# 3. Recursive binary search - divide and conquer [implemented]
#    Time: O(log n) | Space: O(log n)


class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        mid = len(nums) // 2

        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # Condition to search left
        if nums[mid] <= nums[-1]:
            return self.findMin(nums[:mid])

        return self.findMin(nums[mid + 1 :])


def main():
    s = Solution()

    print(s.findMin([3, 4, 5, 1, 2]))  # Expected: 1
    print(s.findMin([4, 5, 6, 7, 0, 1, 2]))  # Expected: 0
    print(s.findMin([11, 13, 15, 17]))  # Expected: 11
    print(s.findMin([5, 1, 2, 3, 4]))  # Expected: 1


if __name__ == "__main__":
    main()
