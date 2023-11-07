# Problem: https://leetcode.com/problems/daily-temperatures/

# Time complexity: O(nlog(n))
# Space complexity: O(n)

import heapq


class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        result: list[int] = [0] * len(temperatures)
        tempsToCheck: list[tuple[int,int]] = []


        for idx, temp in enumerate(temperatures):
            heapq.heappush(tempsToCheck, (temp, idx))

            while len(tempsToCheck) > 0 and temp > tempsToCheck[0][0]:
                _, oldIdx = heapq.heappop(tempsToCheck)
                result[oldIdx] = idx - oldIdx

        return result


def main():
    s: Solution = Solution()

    print(s.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
    print(s.dailyTemperatures([30,40,50,60])) # [1,1,1,0]
    print(s.dailyTemperatures([30,60,90])) # [1,1,0]


if __name__ == '__main__':
    main()
