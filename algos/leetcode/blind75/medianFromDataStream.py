# Problem: https://leetcode.com/problems/find-median-from-data-stream

# TODO: How would you optimize the solution if all integers are in the range (0,100)?
# TODO: How would you optimize the solution if 99% of integers are in the range (0,100)?


class MedianFinder:
    def __init__(self):
        # Using an array, could be improved with a heap instead
        self.vals: list[int] = []

    def addNum(self, num: int) -> None:
        if len(self.vals) == 0:
            self.vals.append(num)
            return

        if num <= self.vals[0]:
            self.vals.insert(0, num)
        elif num >= self.vals[-1]:
            self.vals.append(num)
        else:
            for i in range(1, len(self.vals)):
                if num < self.vals[i]:
                    self.vals.insert(i, num)
                    return

    def findMedian(self) -> float:
        count = len(self.vals)

        # Corner case should not occur
        if count == 0:
            return 0
        if count % 2 == 0:
            return (self.vals[count // 2 - 1] + self.vals[count // 2]) / 2

        return self.vals[count // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
def main():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())  # Expects 1.5
    obj.addNum(3)
    print(obj.findMedian())  # Expects 2.0


if __name__ == "__main__":
    main()
