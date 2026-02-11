# Problem: https://leetcode.com/problems/binary-search/
# tags: easy

# Time complexity: O(log(n))
# Space complexity: NA

# Alternative solutions:
# 1. Linear scan - iterate through array
#    Time: O(n) | Space: O(1)
# 2. Binary search - iterative divide and conquer [implemented]
#    Time: O(log(n)) | Space: O(1)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start: int = 0
        end: int = len(nums)

        while start < end:
            mid: int = start + (end - start) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid + 1

        return -1

    # Alternate implementation, with inclusive end
    def search2(self, nums: list[int], target: int) -> int:
        lo: int = 0
        hi: int = len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1


def main():
    s: Solution = Solution()

    print("Half open search")
    print(s.search([-1, 0, 3, 4, 9, 12], 9))  # Expected: 4
    print(s.search([-1, 0, 3, 4, 9, 12], 2))  # Expected: -1
    print(s.search([-1, 0, 3], 0))  # Expected: 1
    print(s.search([-1, 0], -1))  # Expected: 0
    print(s.search([-1, 0], 0))  # Expected: 1

    print("Inclusive search")
    print(s.search2([-1, 0, 3, 4, 9, 12], 9))  # Expected: 4
    print(s.search2([-1, 0, 3, 4, 9, 12], 2))  # Expected: -1
    print(s.search2([-1, 0, 3], 0))  # Expected: 1
    print(s.search2([-1, 0], -1))  # Expected: 0
    print(s.search2([-1, 0], 0))  # Expected: 1


if __name__ == "__main__":
    main()
