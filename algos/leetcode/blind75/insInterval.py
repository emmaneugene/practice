# Problem: https://leetcode.com/problems/insert-interval

# Time complexity: O(n)
# Space complexity: O(n)

from bisect import bisect


class Solution:
    def overlap(self, i1: list[int], i2: list[int]) -> bool:
        return (i1[0] <= i2[0] and i1[1] >= i2[0]) or (
            i2[0] <= i1[0] and i2[1] >= i1[0]
        )

    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        if len(intervals) == 0:
            return [newInterval]

        out: list[list[int]] = []
        add: list[int] = newInterval

        for ivl in intervals:
            if self.overlap(ivl, add):
                add = [min(add[0], ivl[0]), max(add[1], ivl[1])]
            else:
                out.append(ivl)

        idx: int = bisect(out, add)
        out.insert(idx, add)

        return out


def main():
    s: Solution = Solution()
    print(s.insert([[1, 3], [6, 9]], [2, 5]))
    print(s.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))


if __name__ == "__main__":
    main()
