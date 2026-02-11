# Problem: https://leetcode.com/problems/task-scheduler/
# tags: medium

# Time complexity: O(m) given m tasks
# - For parsing list of. initial tasks
# Space complexity: O(n)
# - For storing n tasks in waiting queue

# Alternative solutions:
# 1. Simulation with max-heap + cooldown queue - greedily pick most frequent task [implemented]
#    Time: O(m * n) | Space: O(n)
# 2. Sorting each round - sort tasks by frequency each cycle, pick greedily
#    Time: O(m * n * log(n)) | Space: O(n)
# 3. Math/greedy formula - compute (maxFreq - 1) * (n + 1) + countOfMaxFreq, take max with len
#    Time: O(m) | Space: O(1)

import heapq
from collections import deque
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        SKIP = ""

        labels = {}
        for t in tasks:
            if t not in labels:
                labels[t] = 0
            labels[t] += 1

        labeledTasks = []
        for k, v in labels.items():
            heapq.heappush(labeledTasks, [-v, k])

        waiting = deque([SKIP] * n)
        waitingCnt = 0
        ivls = 0

        while labeledTasks or waitingCnt > 0:
            # Process next task
            if labeledTasks:
                task = heapq.heappop(labeledTasks)
                task[0] += 1
                if task[0] < 0:
                    waiting.append(task)
                    waitingCnt += 1
                else:
                    waiting.append(SKIP)
            else:
                waiting.append(SKIP)

            # Pop from waiting tasks
            task = waiting.popleft()
            if task != SKIP:
                heapq.heappush(labeledTasks, task)
                waitingCnt -= 1

            ivls += 1

        return ivls


def main():
    s = Solution()
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 2))  # Expected: 8
    print(s.leastInterval(["A", "C", "A", "B", "D", "B"], 1))  # Expected: 6
    print(s.leastInterval(["A", "A", "A", "B", "B", "B"], 3))  # Expected: 10


if __name__ == "__main__":
    main()
