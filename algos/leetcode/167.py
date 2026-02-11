# Problem: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
# tags: medium

# Time complexity: O(n)
# Space complexity: O(1)

# Alternative solutions:
# 1. Brute force - check all pairs
#    Time: O(n^2) | Space: O(1)
# 2. Hash map - store complements
#    Time: O(n) | Space: O(n)
# 3. Binary search - for each element, binary search for complement
#    Time: O(n log n) | Space: O(1)
# 4. Two pointers - converge from both ends [implemented]
#    Time: O(n) | Space: O(1)

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i1 = 0
        i2 = len(numbers) - 1
        while i1 < i2:
            if numbers[i1] + numbers[i2] < target:
                i1 += 1
            elif numbers[i1] + numbers[i2] > target:
                i2 -= 1
            else:
                return [i1 + 1, i2 + 1]

        return []  # No solution


def main():
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # Expected: [1,2]
    print(s.twoSum([2, 3, 4], 6))  # Expected: [1,3]
    print(s.twoSum([-1, 0], -1))  # Expected: [1,2]


if __name__ == "__main__":
    main()
