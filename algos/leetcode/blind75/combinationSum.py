# Problem: https://leetcode.com/problems/combination-sum/

# Dynamic programming - start with first candidates, compute and store all
# possible combinations

# Time complexity: O(n^2)
# Space complexity: O(n^2)

from copy import deepcopy
from typing import Dict, List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Dict of sums to possible combinations
        sumsCombis: Dict[int, List[List[int]]] = {}
        sumsCombis[0] = [[]]

        for n in candidates:
            toAdd: Dict[int, List[List[int]]] = {}

            for mlti in range(1, (target // n) + 1):
                remainder: int = target - (n * mlti)

                for val in range(remainder + 1):
                    if val in sumsCombis:
                        prevCombis: List[List[int]] = sumsCombis[val]
                        for combi in prevCombis:
                            newCombi: List[int] = deepcopy(combi)
                            newCombi += [n] * mlti
                            newVal = val + (n * mlti)
                            if newVal in toAdd:
                                toAdd[(n * mlti) + val].append(newCombi)
                            else:
                                toAdd[(n * mlti) + val] = [newCombi]

            for val, combis in toAdd.items():
                if val in sumsCombis:
                    for combi in combis:
                        sumsCombis[val].append(combi)
                else:
                    sumsCombis[val] = combis

        return sumsCombis.get(target, [])


def main():
    s: Solution = Solution()

    print("Expected: [[2,2,3], [7]]")
    print(f"Actual  :{s.combinationSum([2, 3, 6, 7], 7)}")

    print("Expected: [[2,2,2,2],[2,3,3],[3,5]]")
    print(f"Actual  : {s.combinationSum([2, 3, 5], 8)}")

    print("Expected: []")
    print(f"Actual  :{s.combinationSum([2], 1)}")


if __name__ == "__main__":
    main()
