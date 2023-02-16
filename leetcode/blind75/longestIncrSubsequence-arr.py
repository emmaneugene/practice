# Problem: https://leetcode.com/problems/longest-increasing-subsequence/

# Can you come up with a solution that runs in O(nlogn)?

# Dynamic programming with 2D array (list of possible solutions, pruning)
# Complexity: O(n^3) (very inefficient)
class Solution:
    def updateSubseqs(self, subseqs: list[list[int]],  n: int) -> None:
        # Find the longest new sequence that can be generated 
        toAdd: list[int] = [n]
        for subseq in subseqs:
            for i in range(len(subseq)-1, -1, -1):
                if n > subseq[i]:
                    new: list[int] = subseq[:i+1] + [n]
                    if len(new) > len(toAdd):
                        toAdd = new

        subseqs.append(toAdd)


    def lengthOfLIS(self, nums: list[int]) -> int:
        subseqs: list[list[int]] = [[nums[0]]]
        
        for i in range(1, len(nums)):
            self.updateSubseqs(subseqs, nums[i])

        longestSubseq: list[int] = subseqs[0]
        
        for subseq in subseqs:
            if len(subseq) > len(longestSubseq):
                longestSubseq = subseq
        
        print(f'Longest subsequence: {longestSubseq}')
        return len(longestSubseq)

        

def main():
    s = Solution()

    print(s.lengthOfLIS([10,9,2,5,3,7,101,18])) # [2,3,7,101]
    print(s.lengthOfLIS([0,1,0,3,2,3])) # [0,1,2,3] error
    print(s.lengthOfLIS([7,7,7,7,7,7,7]))  # [7]
    print(s.lengthOfLIS([4,10,4,3,8,9])) # [3,8,9]
    print(s.lengthOfLIS([1,3,6,7,9,4,10,5,6])) # [1,3,6,7,9,10]
    

if __name__ == "__main__":
    main()