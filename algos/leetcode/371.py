# Problem: https://leetcode.com/problems/sum-of-two-integers
# tags: blind75, medium

# Time complexity: O(1) - constant 32-bit operations
# Space complexity: O(1)
# Apply bitwise operations with overflow to do addition


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask to handle negative numbers
        MASK = 0xFFFFFFFF
        # Max integer for 32-bit signed
        MAX = 0x7FFFFFFF

        while b != 0:
            # XOR gives sum without carry
            sum_without_carry = (a ^ b) & MASK
            # AND + left shift gives the carry
            carry = ((a & b) << 1) & MASK
            a = sum_without_carry
            b = carry

        # If a is negative in 32-bit representation, convert to Python negative
        if a > MAX:
            a = ~(a ^ MASK)

        return a


def main():
    s: Solution = Solution()

    print(s.getSum(1, 2))  # Expected: 3
    print(s.getSum(2, 3))  # Expected: 5
    print(s.getSum(-1, 1))  # Expected: 0
    print(s.getSum(-2, 3))  # Expected: 1


if __name__ == "__main__":
    main()
