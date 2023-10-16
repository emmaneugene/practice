# Problem: https://leetcode.com/problems/non-overlapping-intervals/

# Dynamic programming, sort and binary search

from typing import List

class Grouping:
    '''Class that represents a grouping of intervals, with end time
    and interval count
    '''
    def __init__(self, end: int, count: int=1) -> None:
        self.end = end
        self.count = count

class Solution:
    def lookup(self, groupings: List[Grouping], startTime: int) -> int:
        '''Uses binary search to look for the index `i` such that `grouping[:i].end <= startTime` and
        `grouping[i:].end > startTime`
        '''

        lo: int = 0
        hi: int = len(groupings)-1

        while lo < hi:
            mid: int = lo + (hi - lo) // 2
            if groupings[mid].end <= startTime:
                if mid == 0 or mid == len(groupings):
                    return mid+1
                if groupings[mid+1].end > startTime:
                    return mid+1
                
                lo = mid+1
            else:
                if mid == 0:
                    return 0
                if groupings[mid-1].end <= startTime:
                    return mid

                hi = mid-1
       
        return lo if groupings[lo].end > startTime else lo+1
         
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result: int = 0

        # O(nlogn)
        intervals.sort(key=lambda x: (x[0], x[1]))
        
        # Remove intervals with equal start time (greedy)
        # O(n)
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
            # Lookup instead of linear search
            toAdd: Grouping = Grouping(tmp[1], count)

            insIdx: int = self.lookup(groupings, tmp[0])

            if insIdx > 0:
                toAdd.count = max(toAdd.count, groupings[insIdx-1].count+1)
            
            # for j, grp in enumerate(groupings):
            #     if grp.end > tmp[0]:
            #         insIdx = j
            #         break

            #     if count <= grp.count:
            #         count = grp.count + 1

            # Insert new interval according to end time
            # while insIdx < len(groupings) and groupings[insIdx].end < toAdd.end:
            #     insIdx += 1

            if insIdx < len(groupings) and groupings[insIdx].end == toAdd.end:
                groupings[insIdx].count = max(groupings[insIdx].count, toAdd.count)
            else:
                groupings.insert(insIdx, toAdd)
            

            filtered: List[Grouping] = []
            for g in groupings:
                if g.end < toAdd.end or g.count >= toAdd.count:
                    filtered.append(g)
            
            groupings = filtered

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