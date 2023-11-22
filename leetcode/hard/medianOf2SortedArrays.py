# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/


# Algorithm should run in O(log(m+n))
# Solution 1: Merging both arrays is O(m+n), which is not optimal
# Solution 2: Divide and conquer - recursively find medians of each array (?)
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Solution 1
        merged: list[int] = []
        idx1: int = 0
        idx2: int = 0

        while idx1 < len(nums1) and idx2 < len(nums2):
            if nums1[idx1] <= nums2[idx2]:
                merged.append(nums1[idx1])
                idx1 += 1
            else:
                merged.append(nums2[idx2])
                idx2 += 1

        while idx1 < len(nums1):
            merged.append(nums1[idx1])
            idx1 += 1

        while idx2 < len(nums2):
            merged.append(nums2[idx2])
            idx2 += 1

        mid: int = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid] + merged[mid - 1]) / 2

        return merged[mid]


def main():
    s: Solution = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))  # Expected: 2
    print(s.findMedianSortedArrays([1, 2], [3, 4]))  # Expected: 2.5


if __name__ == "__main__":
    main()
