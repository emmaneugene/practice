# Problem: https://leetcode.com/problems/reverse-bits
# tags: blind75, easy

# Time complexity: O(1)
# Space complexity: O(1)

# Alternative solutions:
# 1. String reversal - convert to binary string, reverse, convert back
#    Time: O(1) | Space: O(1)
# 2. Bit-by-bit with multiply/divide [implemented]
#    Time: O(1) | Space: O(1)
# 3. Bit-by-bit with bitwise shift and mask
#    Time: O(1) | Space: O(1)
# 4. Divide and conquer - swap halves recursively (16, 8, 4, 2, 1 bits)
#    Time: O(1) | Space: O(1)


class Solution:
    def reverseBits(self, n: int) -> int:
        reversed = 0

        isPositive = n >= 0

        for _ in range(32):
            reversed *= 2
            if n % 2 == 1:
                reversed += 1
            n //= 2
        return reversed if isPositive else -reversed


def main():
    s = Solution()
    print("Expected: 964176192")
    print(f"Output  : {s.reverseBits(43261596)}")

    print("Expected: 3221225471")
    print(f"Output  : {s.reverseBits(4294967293)}")


if __name__ == "__main__":
    main()
