# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Time complexity: O(log(n))
# Space complexity: O(1)


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """
        We need to find the two elements a,b that are not in ascending order, as the
        right element will be at index n - k. We can then derive k trivially.

        The index of target in nums_o will simply be its index in (nums + k) % n.

        This would be easy with O(n), but we need O(logn).

        We could do a binary search for the two elements a,b.

        Once we have k, we can do another binary search for the element, with the
        indices circularly offset by k before lookup.
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
    s: Solution = Solution


if __name__ == "__main__":
    main()
