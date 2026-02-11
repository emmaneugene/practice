# Problem: https://leetcode.com/problems/maximum-square-area-by-removing-fences-from-a-field/
# tags: medium

# Get a sorted set intersection of all possible horizontal and vertical fence lengths, derived
# From applying sliding windows on the sorted fence lengths

# Given H = len(hFences), V = len(vFences),
# Time complexity: O(H^2 + V^2)
# - Sorting: O(H log H + V log V)
# - Nested loops generate all pairs: O(H²) + O(V²)
# - Intersection check: O(min(H², V²))

# Space complexity: O(H^2 + V^2) in storing all possible lengths

# Alternative solutions:
# 1. Brute force - try all subsets of fences to remove, check each configuration
#    Time: O(2^(H+V) * max(H,V)) | Space: O(H + V)
# 2. Enumerate all pairwise distances, set intersection for common lengths [implemented]
#    Time: O(H^2 + V^2) | Space: O(H^2 + V^2)

from typing import List, Set


class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        def getPossibleLengths(fences: List[int], l: int) -> Set[int]:
            fences = [1] + sorted(fences) + [l]
            lengths = set()
            for i in range(1, len(fences)):
                for j in range(0, len(fences) - i):
                    lengths.add(fences[j + i] - fences[j])

            return lengths

        vLengths = getPossibleLengths(hFences, m)
        hLengths = getPossibleLengths(vFences, n)

        common = vLengths & hLengths
        return -1 if not common else (max(common) ** 2) % (10**9 + 7)


def main():
    s = Solution()
    print(s.maximizeSquareArea(4, 3, [2, 3], [2]))  # Expected: 4
    print(s.maximizeSquareArea(6, 7, [2], [4]))  # Expected: -1


if __name__ == "__main__":
    main()
