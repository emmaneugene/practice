# Problem: https://leetcode.com/problems/two-sum

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        tracker: dict[int, int] = {}

        for i, n in enumerate(nums):
            if target - n in tracker:
                return [tracker[target - n], i]
            tracker[n] = i

        return [-1, -1]  # Should not get here


def main():
    s = Solution()

    print(s.twoSum([2, 7, 11, 15], 9))  # Expected: [0,1]
    print(s.twoSum([3, 2, 4], 6))  # Expected: [1,2]
    print(s.twoSum([3, 3], 6))  # Expected: [0,1]


if __name__ == "__main__":
    main()
