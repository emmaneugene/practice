# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums)):
            diff = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == diff:
                    return [i,j]