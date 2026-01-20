# Problem: https://leetcode.com/problems/count-number-of-trapezoids-i/
# tags: medium

# Time complexity: O(n)
# Space complexity: O(n)

from typing import Dict, List
import math

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        LIMIT = (10 ** 9 + 7)
        lines: Dict[int, List[int]] = {}
        for x, y in points:
            if y not in lines:
                lines[y] = []
            lines[y].append(x)
        combis = list(math.comb(len(c), 2) for c in lines.values())

        res = 0
        tmp = 0
        for c in combis:
            res += tmp * c
            tmp += c
            res %= LIMIT
            tmp %= LIMIT

        return res


def main():
    s = Solution()

    print(s.countTrapezoids([[1,0],[2,0],[3,0],[2,2],[3,2]])) # Expected: 3
    print(s.countTrapezoids([[0,0],[1,0],[0,1],[2,1]])) # Expected: 1


if __name__ == "__main__":
    main()
