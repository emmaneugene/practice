# Problem: https://leetcode.com/problems/number-of-1-bits
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(1)

# Alternative solutions:
# 1. Built-in function - bin() and count()
#    Time: O(n) | Space: O(n)
# 2. Bit shift and modulo - check LSB, right shift [implemented]
#    Time: O(n) | Space: O(1)
# 3. Brian Kernighan's algorithm - n & (n-1) clears lowest set bit
#    Time: O(k) where k = number of set bits | Space: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n //= 2

        return count


def main():
    s = Solution()

    print(s.hammingWeight(11))  # Expected: 3
    print(s.hammingWeight(128))  # Expected: 1
    print(s.hammingWeight(4294967293))  # Expected: 31


if __name__ == "__main__":
    main()
