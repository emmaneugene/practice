# Problem: https://leetcode.com/problems/longest-consecutive-sequence

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nSet = set(nums)
        longest = 0

        for n in nums:
            if n - 1 not in nSet:
                length = 1
                while n + length in nSet:
                    length += 1
                longest = max(length, longest)

        return longest


def main():
    s = Solution()

    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # Expected: 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # Expected: 9
    print(s.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))  # Expected: 7


if __name__ == "__main__":
    main()
