# Problem: https://leetcode.com/problems/counting-bits
# tags: blind75, easy

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)
#
# Alternative solutions:
# 1. Brute force - count bits for each number individually [implemented]
#    Time: O(nlog(n)) | Space: O(n)
# 2. DP with most significant bit - i & (i-1) to clear lowest set bit
#    Time: O(n) | Space: O(n)
# 3. DP with least significant bit - dp[i] = dp[i >> 1] + (i & 1)
#    Time: O(n) | Space: O(n)
# 4. DP with offset - dp[i] = dp[i - offset] + 1, offset is largest power of 2 <= i
#    Time: O(n) | Space: O(n)


class Solution:
    def countBits(self, n: int) -> list[int]:
        return [self.getBitCount(i) for i in range(n + 1)]

    def getBitCount(self, n: int) -> int:
        count = 0
        while n > 0:
            count += n % 2
            n //= 2
        return count


def main():
    s = Solution()

    print(s.countBits(2))  # Expected: [0,1,1]
    print(s.countBits(5))  # Expected: [0,1,1,2,1,2]


if __name__ == "__main__":
    main()
