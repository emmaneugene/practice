# Problem: https://leetcode.com/problems/subsets/

# Time complexity: O(n^2)
# Space complexity: O(n^2)

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
