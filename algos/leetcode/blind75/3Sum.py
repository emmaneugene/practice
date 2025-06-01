# Problem: https://leetcode.com/problems/3sum


# Time complexity: O(n^2)
# Space complexity: O(n^2)


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        results: list[list[int]] = []

        posCounts: dict[int, int] = {}
        negCounts: dict[int, int] = {}
        zeroCounts = 0

        for n in nums:
            if n > 0:
                if n in posCounts:
                    posCounts[n] += 1
                else:
                    posCounts[n] = 1
            elif n < 0:
                if n in negCounts:
                    negCounts[n] += 1
                else:
                    negCounts[n] = 1
            else:
                zeroCounts += 1

        # -ve, 0, +ve: O(n):
        if zeroCounts > 0:
            # Triple 0s: O(1)
            if zeroCounts >= 3:
                results.append([0, 0, 0])
            for neg in negCounts:
                if -neg in posCounts:
                    results.append([neg, 0, -neg])

        # Pairs: O(n)
        for val, count in posCounts.items():
            if count >= 2 and -(2 * val) in negCounts:
                results.append([val, val, -(2 * val)])

        for val, count in negCounts.items():
            if count >= 2 and -(2 * val) in posCounts:
                results.append([val, val, -(2 * val)])

        # All unique: O(n^2)
        # 2 positive, 1 negative
        positives: list[int] = list(posCounts.keys())
        for i in range(len(positives)):
            for j in range(i + 1, len(positives)):
                toFind: int = -(positives[i] + positives[j])
                if toFind in negCounts:
                    results.append([positives[i], positives[j], toFind])

        # 2 negative, 1 positive
        negatives: list[int] = list(negCounts.keys())
        for i in range(len(negatives)):
            for j in range(i + 1, len(negatives)):
                toFind: int = -(negatives[i] + negatives[j])
                if toFind in posCounts:
                    results.append([negatives[i], negatives[j], toFind])

        return results


def main():
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # Expected: [[-1,-1,2].[-1,0,1]]
    print(s.threeSum([0, 1, 1]))  # Expected: []
    print(s.threeSum([0, 0, 0]))  # Expected: [0,0,0]
    print(s.threeSum(
        [-1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 4, 4]
    ))  # Expected: [0,0,0], [-1,0,1], [-1,-1,2]


if __name__ == "__main__":
    main()
