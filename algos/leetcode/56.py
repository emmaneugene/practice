# Problem: https://leetcode.com/problems/merge-intervals
# tags: blind75, medium

# Time complexity: O(nlogn)
# Space complexity: O(n)


class Solution:
    def combine(self, i1: list[int], i2: list[int]) -> list[int]:
        return [min(i1[0], i2[0]), max(i1[1], i2[1])]

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort intervals by start time asc
        intervals.sort()
        res: list[list[int]] = []
        curr: list[int] = intervals[0]

        for ivl in intervals[1:]:
            if curr[1] >= ivl[0]:
                curr = self.combine(curr, ivl)
            else:
                res.append(curr)
                curr = ivl

        res.append(curr)
        return res


def main():
    s = Solution()

    print(
        s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    )  # Expected: [[1,6],[8,10],[15,18]]
    print(
        s.merge([[1, 3], [2, 6], [15, 18], [8, 10]])
    )  # Expected: [[1,6],[8,10],[15,18]]
    print(s.merge([[1, 4], [4, 5]]))  # Expected: [[1,5]]


if __name__ == "__main__":
    main()
