# Problem: https://leetcode.com/problems/construct-the-minimum-bitwise-array-i
# tags: easy

# Time complexity: O(n) (integer size is bounded)
# Space complexity: O(n)
# For a result value n, find the right most 0-bit, and you can convert the bit to the right to
# 0 as well. Even numbers will never work, and for values with all bits set to 1, you can drop
# the MSB

from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def getMinAns(n: int) -> int:
            if n % 2 == 0:
                return -1
            binaryRepr: str = bin(n)[2:]
            idx = binaryRepr.rfind("0")

            return int(binaryRepr[: idx + 1] + "0" + binaryRepr[idx + 2 :], 2)

        return [getMinAns(n) for n in nums]


def main():
    s = Solution()
    print(s.minBitwiseArray([1])) # Expected:  [0]
    print(s.minBitwiseArray([2, 3, 5, 7])) # Expected:  [-1, 1, 4, 3]
    print(s.minBitwiseArray([11, 13, 31])) # Expected:  [9, 12, 15]


if __name__ == "__main__":
    main()
