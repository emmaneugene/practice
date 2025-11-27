# Problem: https://leetcode.com/problems/find-median-from-data-stream

# Time complexity: O(nlogn)
# Space complexity: O(n)
# Use heaps to keep track of larger/smaller values, and consistently rebalance
# OR use a red-black tree
# EXTRA: How would you optimize the solution if all integers are in the range (0,100)? -> Use a count
# EXTRA: How would you optimize the solution if 99% of integers are in the range (0,100)? -> Still use a count

import heapq


class MedianFinder:
    def __init__(self):
        self.larger: list[int] = []
        self.smaller: list[int] = []

    def addNum(self, val: int) -> None:
        val = heapq.heappushpop(self.larger, val)
        val = -heapq.heappushpop(self.smaller, -val)
        heapq.heappush(self.larger, val)
        while len(self.larger) - len(self.smaller) > 1:
            heapq.heappush(self.smaller, -heapq.heappop(self.larger))

    def findMedian(self) -> float:
        if len(self.larger) > len(self.smaller):
            return self.larger[0]
        return (self.larger[0] - self.smaller[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
def main():
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())  # Expects 1.5
    medianFinder.addNum(3)
    print(medianFinder.findMedian())  # Expects 2.0


if __name__ == "__main__":
    main()
