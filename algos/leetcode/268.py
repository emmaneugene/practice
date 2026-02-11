# Problem: https://leetcode.com/problems/missing-number
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. Sorting - sort array, find gap
#    Time: O(n log n) | Space: O(1)
# 2. Hash set - store nums in set, check 0..n [implemented]
#    Time: O(n) | Space: O(n)
# 3. Gauss formula - expected sum minus actual sum
#    Time: O(n) | Space: O(1)
# 4. Bit manipulation - XOR all indices and values
#    Time: O(n) | Space: O(1)


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        keys: set[int] = set(nums)

        for i in range(len(nums) + 1):
            if i not in keys:
                return i

        return -1


def main():
    s = Solution()

    print(s.missingNumber([3, 0, 1]))  # 2
    print(s.missingNumber([0, 1]))  # 2
    print(s.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))  # 8


if __name__ == "__main__":
    main()
