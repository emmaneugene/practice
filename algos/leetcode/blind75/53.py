# Problem: https://leetcode.com/problems/maximum-subarray

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]
        subarrSums = [0] * len(nums)
        subarrSums[0] = nums[0]

        for i in range(1, len(nums)):
            subarrSums[i] = nums[i]
            if subarrSums[i - 1] > 0:
                subarrSums[i] += subarrSums[i - 1]

            if subarrSums[i] > maxSum:
                maxSum = subarrSums[i]

        return maxSum


def main():
    s = Solution()

    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # Expected: 6
    print(s.maxSubArray([1]))  # Expected: 1
    print(s.maxSubArray([5, 4, -1, 7, 8]))  # Expected: 23


if __name__ == "__main__":
    main()
