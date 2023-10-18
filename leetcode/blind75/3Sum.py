# Problem: https://leetcode.com/problems/3sum/

from typing import List, Set

# TODO

# Time complexity: O()
# Space complexity: O()
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res: Set = set()
        
        n: List[int]; p: List[int]; z: List[int]
        n, p, z = [], [] , []
         
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        N = set(N)
        P = set(P)

        # Handle corner cases (empty, all +ve, all -ve)
        if ( == 0 or nums[0] > 0 or nums[-1] < 0):
            return []

        # Find "boundary", where array elements go from +ve to -ve
        # The first 0 is treated as the boundary if it exists, otherwise smallest -ve
        boundary: int = -1

        for i in range(size):
            if nums[i] == 0:
                boundary = i
                break
            if nums[i] < 0 and nums[i+1] > 0:
                boundary = i
                break

        # 3 sum is -ve, +ve, and 3rd value that tops up the difference (or it could be 0)
        # -ve will always be <= boundary
        # +ve will always be > boundary
        # if sum -ve, look to boundary right for 3rd value (positive values)
        # if sum +ve, look to boundary left for 3rd value (negative values)

        for pos_idx in range(boundary+1, size):  # >= 0
            for neg_idx in range(boundary+1):  # <= 0
                intermed = nums[pos_idx] + nums[neg_idx]
                if intermed < 0:
                    # Search right
                    for i in range(boundary, pos_idx):
                        if nums[i] + intermed == 0:
                            toAdd = [nums[neg_idx], nums[i], nums[pos_idx]]
                            if toAdd not in output:
                                output.append(toAdd)
                elif intermed > 0:
                    # Search left
                    for i in range(boundary, neg_idx, -1):
                        if nums[i] + intermed == 0:
                            toAdd = [nums[neg_idx], nums[i], nums[pos_idx]]
                            if toAdd not in output:
                                output.append(toAdd)
                else:
                    # Last value must be 0 (but we cannot double count)
                    if pos_idx != boundary and neg_idx != boundary and nums[boundary] == 0:
                        toAdd = [nums[neg_idx], nums[boundary], nums[pos_idx]]
                        if toAdd not in output:
                            output.append(toAdd)

        # Last corner case: look for an occurence of [0,0,0]
        if boundary+3 <= size and nums[boundary] == 0 and sum(nums[boundary: boundary+3]) == 0:
            output.append([0, 0, 0])

        return output


def main():
    s: Solution = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # Expected: [[-1,-1,2].[-1,0,1]]
    print(s.threeSum([0, 1, 1]))  # Expected: []
    print(s.threeSum([0, 0, 0]))  # Expected: [0,0,0]


if __name__ == '__main__':
    main()
