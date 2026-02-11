# Problem: https://leetcode.com/problems/subsets/
# tags: medium

# Time complexity: O(n^2)
# Space complexity: O(n^2)
#
# Alternative solutions:
# 1. Cascading (iterative) - iterate nums, copy & extend existing subsets [implemented]
#    Time: O(n * 2^n) | Space: O(n * 2^n)
# 2. Backtracking/DFS - recursively include or exclude each element
#    Time: O(n * 2^n) | Space: O(n * 2^n)
# 3. Bit manipulation - use bitmask from 0 to 2^n-1 to represent inclusion
#    Time: O(n * 2^n) | Space: O(n * 2^n)

import copy


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result: list[list[int]] = [[]]

        for n in nums:
            prevCount: int = len(result)

            for i in range(prevCount):
                newCombi: list[int] = copy.deepcopy(result[i])
                newCombi.append(n)
                result.append(newCombi)

        return result


def main():
    s: Solution = Solution()
    print(s.subsets([1, 2, 3]))


if __name__ == "__main__":
    main()
