# Problem: https://leetcode.com/problems/top-k-frequent-elements/

# Time complexity: O(nlogn)
# Space complexity: O(n)

from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts: dict[int, int] = {}

        for n in nums:
            if n not in counts:
                counts[n] = 1
            else:
                counts[n] += 1

        countsList: List[tuple[int, int]] = []

        for val, count in counts.items():
            countsList.append((val, count))

        countsList.sort(key=lambda x: x[1], reverse=True)

        result: List[int] = []

        for i in range(k):
            result.append(countsList[i][0])

        return result


def main():
    s: Solution = Solution()

    print(s.topKFrequent([1, 1, 1, 2, 2, 3], 2))  # Expected: [1,2]
    print(s.topKFrequent([1], 1))  # Expected: [1]


if __name__ == '__main__':
    main()
