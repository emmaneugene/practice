# Problem: https://leetcode.com/problems/missing-number

# Time complexity: O(n)
# Space complexity: O(n)


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
