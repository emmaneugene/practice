# Problem: https://leetcode.com/problems/two-sum
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. Brute force - nested loops
#    Time: O(n^2) | Space: O(1)
# 2. Sort + two pointers - sorting, two pointers
#    Time: O(n log n) | Space: O(n)
# 3. Hash map - single pass hash map [implemented]
#    Time: O(n) | Space: O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tracker: dict[int, int] = {}

        for i, n in enumerate(nums):
            if target - n in tracker:
                return [tracker[target - n], i]
            tracker[n] = i

        return [-1, -1]  # Should not get here


def main():
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))  # Expected: [0,1]
    print(s.twoSum([3, 2, 4], 6))  # Expected: [1,2]
    print(s.twoSum([3, 3], 6))  # Expected: [0,1]


if __name__ == "__main__":
    main()
