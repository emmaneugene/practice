# Problem: https://leetcode.com/problems/meeting-rooms-ii

# Time complexity: O(nlog(n))
# Space complexity: O(n)

import heapq


class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        rooms: list[int] = []

        intervals.sort(key=lambda x: x[0])

        heapq.heappush(rooms, intervals[0][1])
        for i in intervals[1:]:
            if rooms[0] <= i[0]:
                # No overlap
                heapq.heappop(rooms)
            heapq.heappush(rooms, i[1])
        return len(rooms)


def main():
    s = Solution()

    print(s.minMeetingRooms([[0, 30], [5, 10], [15, 20]]))  # Expected: 2
    print(s.minMeetingRooms([[7, 10], [2, 4]]))  # Expected: 1


if __name__ == "__main__":
    main()
