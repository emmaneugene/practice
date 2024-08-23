# Problem: https://leetcode.com/problems/combination-sum

# Time complexity: O(n^2)
# Space complexity: O(n^2)

import copy


class Solution:
    # DP-iterative: Compute all possible sum combinations
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        solns: dict[int, list[list[int]]] = {}
        solns[0] = [[]]

        for c in candidates:
            newSolns = self.getNewSums(solns, target, c)

            for k, v in newSolns.items():
                if k in solns:
                    solns[k] += v
                else:
                    solns[k] = v

        return solns.get(target, [])

    def getNewSums(
        self, prev: dict[int, list[list[int]]], target: int, c: int
    ) -> dict[int, list[list[int]]]:
        newSums: dict[int, list[list[int]]] = {}
        for val, combis in prev.items():
            mult = (target - val) // c
            for m in range(1, mult + 1):
                newVal = val + c * m
                newCombis = [copy.deepcopy(combi) + ([c] * m) for combi in combis]
                if newVal in newSums:
                    newSums[newVal] += newCombis
                else:
                    newSums[newVal] = newCombis

        return newSums


def main():
    s: Solution = Solution()

    print("Expected: [[2, 2, 3], [7]]")
    print(f"Actual  : {s.combinationSum([2, 3, 6, 7], 7)}")

    print("Expected: [[2, 2, 2, 2], [2, 3, 3], [3, 5]]")
    print(f"Actual  : {s.combinationSum([2, 3, 5], 8)}")

    print("Expected: []")
    print(f"Actual  : {s.combinationSum([2], 1)}")


if __name__ == "__main__":
    main()
