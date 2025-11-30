from typing import List

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        nums = [n % p for n in nums]
        currSum = sum(nums)
        target = currSum % p

        if target == 0:
            return 0

        for size in range(len(nums) - 1):
            tmp = sum(nums[:size])
            for j in range(len(nums) - size):
                tmp += nums[j+size]
                if tmp % p == target:
                    return size + 1
                tmp -= nums[j]

        return -1


def main():
    s = Solution()

    print(s.minSubarray([3,1,4,2], 6)) # Expected: 1
    print(s.minSubarray([6,3,5,2], 9)) # Expected: 2
    print(s.minSubarray([1,2,3], 3)) # Expected: 0


if __name__ == "__main__":
    main()
