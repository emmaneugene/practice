# Problem: https://leetcode.com/problems/merge-intervals

# Time complexity: O(nlogn)
# Space complexity: O(n)


class Solution:
    def combine(self, i1: list[int], i2: list[int]) -> list[int]:
        return [min(i1[0], i2[0]), max(i1[1], i2[1])]

    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # Sort intervals by increasing start time
        intervals.sort(key=lambda x: x[0])

        result: list[list[int]] = []
        current: list[int] = intervals[0]
        for i in range(1, len(intervals)):
            if current[1] >= intervals[i][0]:
                current = self.combine(current, intervals[i])
            else:
                result.append(current)
                current = intervals[i]

        result.append(current)
        return result


def main():
    s: Solution = Solution()
    # Expected: [[1,6],[8,10],[15,18]]
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    # Expected: [[1,6],[8,10],[15,18]]
    print(s.merge([[1, 3], [2, 6], [15, 18], [8, 10]]))
    print(s.merge([[1, 4], [4, 5]]))  # Expected: [[1,5]]


if __name__ == "__main__":
    main()
