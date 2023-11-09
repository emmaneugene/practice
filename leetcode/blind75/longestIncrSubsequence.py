# Problem: https://leetcode.com/problems/longest-increasing-subsequence/

# Time complexity: O(nlogn)
# Space complexity: O(n)

from bisect import bisect_left
from typing import List, Tuple


class Tracker:
    """Tracks last element of a subsequence and its length"""

    def __init__(self, val: int, length: int) -> None:
        self.val = val
        self.length = length

    def __str__(self) -> str:
        return f"[{self.val}, {self.length}]"


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        longest: int = 1

        trackers: List[Tracker] = [Tracker(nums[0], 1)]

        for i in range(1, len(nums)):
            idx: int = bisect_left(trackers, nums[i], key=lambda x: x.val)

            if idx == 0:
                if trackers[0].length == 1:
                    trackers.pop(0)

                trackers.insert(0, Tracker(nums[i], 1))

            else:
                smaller: Tracker = trackers[idx - 1]
                new: Tracker = Tracker(nums[i], smaller.length + 1)

                # Replace next tracker entry if length is not greater
                if idx < len(trackers) and trackers[idx].length <= new.length:
                    trackers.pop(idx)

                trackers.insert(idx, new)

                if new.length > longest:
                    longest = new.length

        for tracker in trackers:
            print(tracker, end=" ")
        print("")
        return longest


def main():
    s = Solution()

    print(s.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # [2,3,7,101]
    print(s.lengthOfLIS([0, 1, 0, 3, 2, 3]))  # [0,1,2,3]
    print(s.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]))  # [7]
    print(s.lengthOfLIS([4, 10, 4, 3, 8, 9]))  # [3,8,9]
    print(s.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]))  # [1,3,6,7,9,10]


if __name__ == "__main__":
    main()
