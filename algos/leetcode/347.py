# Problem: https://leetcode.com/problems/top-k-frequent-elements
# tags: blind75, medium

# Time complexity: O(nlogn)
# Space complexity: O(n)
#
# Alternative solutions:
# 1. Sorting by frequency - hash map + sort [implemented]
#    Time: O(nlogn) | Space: O(n)
# 2. Min-heap of size k - hash map + heap
#    Time: O(nlogk) | Space: O(n)
# 3. Bucket sort - hash map + frequency buckets
#    Time: O(n) | Space: O(n)
# 4. Quickselect - hash map + randomized partition
#    Time: O(n) avg, O(n²) worst | Space: O(n)


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts: dict[int, int] = {}

        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1

        countsList = sorted(list(counts.items()), reverse=True)
        return [c[0] for c in countsList[:k]]


def main():
    s = Solution()

    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Expected: [1,2]
    print(s.topKFrequent([1], 1))  # Expected: [1]


if __name__ == "__main__":
    main()
