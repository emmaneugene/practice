# Problem: https://leetcode.com/problems/number-of-1-bits

# Time complexity: O(n)
# Space complexity: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n //= 2

        return count


def main():
    s: Solution = Solution()

    print(s.hammingWeight(11))  # Expected: 3
    print(s.hammingWeight(128))  # Expected: 1
    print(s.hammingWeight(4294967293))  # Expected: 31


if __name__ == "__main__":
    main()
