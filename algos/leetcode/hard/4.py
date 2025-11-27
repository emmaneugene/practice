# Problem: https://leetcode.com/problems/median-of-two-sorted-arrays/

# Time complexity: O(log(min(m,n)))
# Space complexity: O(m+n)

from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Binary search on partition positions to find median in O(log(min(m,n)))"""
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # Ensure A is the smaller array for optimization
        if len(B) < len(A):
            A, B = B, A

        left, right = 0, len(A) - 1

        while True:
            # Partition A
            i = (left + right) // 2
            # Partition B based on A's partition to ensure left side has half elements
            j = half - i - 2

            # Get boundary values (use infinity for out-of-bounds)
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")

            # Check if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd
                if total % 2:
                    return min(Aright, Bright)
                # Even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                # A's left partition is too big, move left
                right = i - 1
            else:
                # A's left partition is too small, move right
                left = i + 1


def main():
    s = Solution()
    print(s.findMedianSortedArrays([1, 3], [2]))  # Expected: 2
    print(s.findMedianSortedArrays([1, 2], [3, 4]))  # Expected: 2.5
    print(s.findMedianSortedArrays([1, 2, 3, 4, 5], [6, 7]))  # Expected: 4
    print(s.findMedianSortedArrays([1, 1, 1, 1, 1], [1, 1]))  # Expected: 1


if __name__ == "__main__":
    main()
