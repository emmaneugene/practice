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

        countsList: list[tuple[int, int]] = [
            (val, count) for val, count in counts.items()
        ]

        countsList.sort(key=lambda x: x[1], reverse=True)

        return [countsList[i][0] for i in range(k)]


def main():
    s: Solution = Solution()

    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Expected: [1,2]
    print(s.topKFrequent([1], 1))  # Expected: [1]


if __name__ == "__main__":
    main()
