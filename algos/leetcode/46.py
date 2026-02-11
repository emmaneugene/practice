# Problem: https://leetcode.com/problems/permutations/
# tags: medium

# Time complexity: O(n!)
# Space complexity: O(n!)
#
# Alternative solutions:
# 1. Backtracking - recursion, visited set
#    Time: O(n * n!) | Space: O(n * n!)
# 2. Heap's algorithm - recursion, swaps
#    Time: O(n * n!) | Space: O(n * n!)
# 3. Iterative insertion - insert element at each position [implemented]
#    Time: O(n * n!) | Space: O(n * n!)

import copy


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results: list[list[int]] = []

        if len(nums) > 0:
            results.append([nums[0]])

        for i in range(1, len(nums)):
            prevCount: int = len(results)

            for j in range(prevCount):
                result: list[int] = results[j]
                for k in range(len(result)):
                    newResult: list[int] = copy.deepcopy(result)
                    newResult.insert(k, nums[i])
                    results.append(newResult)

            for j in range(prevCount):
                results[j].append(nums[i])

        return results


def main():
    s: Solution = Solution()

    print(s.permute([1, 2, 3]))
    print(s.permute([1, 2, 3, 4]))


if __name__ == "__main__":
    main()
