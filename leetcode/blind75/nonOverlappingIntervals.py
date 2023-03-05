# Problem: https://leetcode.com/problems/non-overlapping-intervals/

# Idea: Sort by start time, collect sets of overlapping intervals, find best to remove, recursively iterate

from typing import List

class Grouping:
    '''Class that represents a grouping of intervals, with start time, end time,
    and interval count
    '''
    def __init__(self, end: int, count: int=1) -> None:
        self.end = end
        self.count = count

class Solution:
    def overlap(self, i1: List[int], i2: List[int]) -> bool:
        '''Function that takes in intervals `i1` and `i2`, where `i1[0] <= i2[0]`. `i1` and `i2` are overlapping if 
        `i1[1] > i2[0]` (end time of earlier interval crosses start time of later interval)
        '''
        return i1[1] > i2[0]

    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result: int = 0

        intervals.sort(key=lambda x: (x[0], x[1]))
        
        # Remove intervals with equal start time (greedy)
        processed: List[List[int]] = [intervals[0]]
        prevStart: int = intervals[0][0]

        for i in range(1, len(intervals)):
            if intervals[i][0] == prevStart:
                result += 1
            else:
                processed.append(intervals[i])
                prevStart = intervals[i][0]
            
        intervals = processed

        # Dynamic programming, track most non-overlapping intervals before end times
        # x[0] -> number of intervals, x[1] = end time

        maxIntervals: int = 1
        groupings: List[Grouping] = [Grouping(intervals[0][1], 1)]
        
        for i in range(1, len(intervals)):
            tmp: List[int] = intervals[i]
            count: int = 1
            insIdx: int = 0

            # Find largest new interval grouping
            for j, grp in enumerate(groupings):
                if grp.end > tmp[0]:
                    insIdx = j
                    break

                if count <= grp.count:
                    count = grp.count + 1

            # Insert new interval according to end time
            toAdd: Grouping = Grouping(tmp[1], count)
            
            while insIdx < len(groupings) and groupings[insIdx].end < toAdd.end:
                insIdx += 1

            if insIdx < len(groupings) and groupings[insIdx].end == toAdd.end:
                groupings[insIdx].count = max(groupings[insIdx].count, toAdd.count)
            else:
                groupings.insert(insIdx, toAdd)

            # Update maxIntervals
            if maxIntervals < toAdd.count: maxIntervals = toAdd.count
            

        result += len(intervals) - maxIntervals
        return result


def main():
    s: Solution = Solution()

    print(s.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]])) # Expected: 1
    print(s.eraseOverlapIntervals([[1,2],[1,2],[1,2]])) # Expected: 2
    print(s.eraseOverlapIntervals([[1,2],[2,3]])) # Expected: 0
    print(s.eraseOverlapIntervals([[1,9],[1,6],[1,3],[2,7],[3,5]])) # Expected: 3
    print(s.eraseOverlapIntervals([[1,9],[1,6],[1,3],[3,9]])) # Expected: 2

if __name__ == '__main__':
    main()