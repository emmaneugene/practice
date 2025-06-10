# Problem: https://leetcode.com/problems/non-overlapping-intervals

# Time complexity: O(nlogn)
# Space complexity: O(n)

class Solution:

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        res = 0
        if not any(intervals):
            return res

        intervals.sort(key=lambda x: (x[1], x[0]))
        prev = intervals[0]

        for ivl in intervals[1:]:
            if ivl[0] < prev[1]:
                res += 1
            else:
                prev = ivl

        return res


def main():
    s = Solution()

    print(s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))  # Expected: 1
    print(s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))  # Expected: 2
    print(s.eraseOverlapIntervals([[1, 2], [2, 3]]))  # Expected: 0
    print(
        s.eraseOverlapIntervals([[1, 9], [1, 6], [1, 3], [2, 7], [3, 5]])
    )  # Expected: 3
    print(s.eraseOverlapIntervals([[1, 9], [1, 6], [1, 3], [3, 9]]))  # Expected: 2
    print(s.eraseOverlapIntervals([[-52,31],[-73,-26],[82,97],[-65,-11],[-62,-49],[95,99],[58,95],[-31,49],[66,98],[-63,2],[30,47],[-40,-26]]))  # Expected: 7


if __name__ == "__main__":
    main()
