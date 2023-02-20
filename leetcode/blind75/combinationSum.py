# Problem: https://leetcode.com/problems/combination-sum/

# Dynamic programming - start with first candidates, compute and store all
# possible combinations
from copy import deepcopy


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        # Dict of sums to possible combinations
        sumsCombis: dict[int, list[list[int]]] = {}
        sumsCombis[0] = [[]]

        for n in candidates:
            toAdd: dict[int, list[list[int]]] = {}

            for mlti in range(1, (target//n) + 1):
                remainder: int = target - (n * mlti)
                
                for val in range(remainder+1):
                    if val in sumsCombis:
                        prevCombis: list[list[int]] = sumsCombis[val]
                        for combi in prevCombis:
                            newCombi: list[int] = deepcopy(combi)
                            newCombi += [n] * mlti
                            newVal = val + (n * mlti)
                            if newVal in toAdd:
                                toAdd[(n*mlti)+val].append(newCombi)
                            else:
                                toAdd[(n*mlti)+val] = [newCombi]

            for val, combis in toAdd.items():
                if val in sumsCombis:
                    for combi in combis:
                        sumsCombis[val].append(combi)
                else:
                    sumsCombis[val] = combis
                    
            
        return sumsCombis.get(target, [])
                


def main():
    s: Solution = Solution()

    print(s.combinationSum([2,3,6,7], 7)) # Expected: [[2,2,3], [7]]
    
    print(s.combinationSum([2,3,5], 8)) # Expected: [[2,2,2,2],[2,3,3],[3,5]]
    
    print(s.combinationSum([2], 1)) # Expected: []

    


if __name__ == '__main__':
    main()