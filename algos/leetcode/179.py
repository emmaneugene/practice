# Problem: https://leetcode.com/problems/largest-number
# tags: medium

# Time complexity: O(knlog(n)), where k is the average length of numbers as strings
# Space complexity: O(n)
# Create a custom comparator

from functools import cmp_to_key


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        numStr = [str(n) for n in nums]

        def compare(s1: str, s2: str) -> int:
            if s1 + s2 > s2 + s1:
                return 1
            elif s1 + s2 < s2 + s1:
                return -1
            else:
                return 0

        numStr.sort(key=cmp_to_key(compare), reverse=True)
        result = "".join(numStr)

        # Edge case: Zero
        return "0" if result[0] == "0" else result


def main():
    s = Solution()

    print(s.largestNumber([10, 2]))  # Expected: 210
    print(s.largestNumber([3, 30, 34, 5, 9]))  # Expected: 9534330
    print(s.largestNumber([543, 54]))  # Expected: 54543
    print(s.largestNumber([545, 54]))  # Expected: 54554


if __name__ == "__main__":
    main()
