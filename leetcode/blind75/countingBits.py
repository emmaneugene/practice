# Problem: https://leetcode.com/problems/counting-bits/

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        out: List[int] = [self.getBitCount(i) for i in range(n+1)]

        return out

    def getBitCount(self, n: int) -> int:
        count: int = 0
        while (n > 0):
            count += n % 2
            n //= 2
        return count

def main():
    s: Solution = Solution()

    print(s.countBits(2)) # Expected: [0,1,1]
    print(s.countBits(5)) # Expected: [0,1,1,2,1,2]

if __name__ == '__main__':
    main()