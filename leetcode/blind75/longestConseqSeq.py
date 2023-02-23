# Problem: https://leetcode.com/problems/longest-consecutive-sequence/

from typing import Dict, List

class Solution:
    def longestConsecutive(self,  nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        minN: int = nums[0]
        maxN: int = nums[0]
        vals: Dict[int, bool] = {}

        for n in nums:
            if n < minN:
                minN = n
            elif n > maxN:
                maxN = n

            vals[n] = True
        
        longest: int = 1
        comp: int = 1
        tracking: bool = False
        count: int = 0

        for i in range(minN, maxN+1):
            if vals.get(i, False):
                count += 1
                if not tracking:
                    tracking = True
                    comp = 1
                else:
                    comp += 1
            else:
                if tracking:
                    longest = max(comp, longest)
                    tracking = False

            # Early stopping condition  
            if longest > (len(nums) // 2):
                break 

        return max(longest, comp)

def main():
    s: Solution = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))
    print(s.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
    print(s.longestConsecutive([9,1,4,7,3,-1,0,5,8,-1,6]))


if __name__=='__main__':
    main()