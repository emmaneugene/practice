# Problem: https://leetcode.com/problems/top-k-frequent-elements

# Time complexity: O(nlogn)
# Space complexity: O(n)


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
