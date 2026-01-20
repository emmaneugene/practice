# Problem: https://leetcode.com/problems/counting-bits
# tags: blind75, easy

# Time Complexity: O(nlog(n))
# Space Complexity: O(n)


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
