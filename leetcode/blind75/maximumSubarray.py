# Problem: https://leetcode.com/problems/maximum-subarray/

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum = nums[0]

        subarraySums = [0] * len(nums)
        subarraySums[0] = nums[0]
        for i in range(1, len(nums)):
            subarraySums[i] = nums[i]
            if subarraySums[i - 1] > 0:
                subarraySums[i] += subarraySums[i - 1]

            if subarraySums[i] > maxSum:
                maxSum = subarraySums[i]

        return maxSum


def main():
    s: Solution = Solution()

    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])) # 6
    print(s.maxSubArray([1])) # 1
    print(s.maxSubArray([5, 4, -1, 7, 8])) # 23


if __name__ == "__main__":
    main()
