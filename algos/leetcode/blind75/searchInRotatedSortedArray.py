# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array

# Time complexity: O(log(n))
# Space complexity: O(n)


# TODO: Refactor
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """Perform binary search for circular adjacent numbers (a, b) which are
        not in ascending order. Index of b is equivalent to offset k

        Then perform another binary search for the target, taking k into account.
        """
        n = len(nums)
        if n == 1:
            return 0 if target in nums else -1

        # find k
        lo = 0
        hi = n - 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            lo_num = nums[lo]
            hi_num = nums[hi]
            mid_num = nums[mid]
            # a, b is to the left
            if mid_num < lo_num:
                hi = mid
                continue
            # a, b is to the right
            if mid_num > hi_num:
                lo = mid
                continue
            break
        k = n - hi if nums[lo] > nums[hi] else 0

        # find target
        lo = 0
        hi = n - 1
        while lo < hi:
            mid = (lo + hi) // 2
            mid_k = (mid - k) % n
            mid_num = nums[mid_k]
            if target < mid_num:
                hi = mid
                continue
            if target > mid_num:
                lo = mid + 1
                continue
            return mid_k
        if lo == hi and nums[(lo - k) % n] == target:
            return (lo - k) % n
        return -1


def main():
    s: Solution = Solution()

    print(s.search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
    print(s.search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
    print(s.search([1], 0))  # -1


if __name__ == "__main__":
    main()
