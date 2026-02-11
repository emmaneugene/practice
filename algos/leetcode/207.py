# Problem: https://leetcode.com/problems/course-schedule
# tags: blind75, medium

# Time complexity: O(n^2)
# Space complexity: O(n^3)
# Use a 2D array(adjacency matrix) to store courses and their dependencies/dependents

# Alternative solutions:
# 1. Eager prerequisite propagation - adjacency matrix with transitive closure [implemented]
#    Time: O(n^2) per edge, O(n^2 * E) total | Space: O(n^3)
# 2. DFS cycle detection - adjacency list, 3-color marking (white/gray/black)
#    Time: O(V + E) | Space: O(V + E)
# 3. BFS topological sort (Kahn's algorithm) - in-degree tracking, queue
#    Time: O(V + E) | Space: O(V + E)


class Solution:
    def canFinish(self, numCourses: int, prereqs: list[list[int]]) -> bool:
        # j in courseMatrix[i] means course j is a prereq for i
        courseDict: dict[int, set[int]] = {}
        for i in range(numCourses):
            courseDict[i] = set()

        for pair in prereqs:
            cur: int = pair[0]
            req: int = pair[1]

            if cur in courseDict[req]:
                return False
            courseDict[cur].add(req)

            # Retrieve all prereqs of `req`
            prereqs: set[int] = courseDict[req]

            for prereq in prereqs:
                if cur in courseDict[prereq]:
                    return False

                courseDict[cur].add(prereq)

            # Add prerequisites for all courses that `aft` is a prerequisite for
            for code, courses in courseDict.items():
                if cur in courses:
                    if code in courseDict[req]:
                        return False
                    courses.add(req)

                    for prereq in prereqs:
                        if code in courseDict[prereq]:
                            return False
                        courses.add(prereq)

        return True


def main():
    s = Solution()

    print(s.canFinish(2, [[1, 0]]))  # True
    print(s.canFinish(2, [[1, 0], [0, 1]]))  # False
    print(
        s.canFinish(
            20, [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]
        )
    )  # False
    print(s.canFinish(5, [[1, 4], [2, 4], [3, 1], [3, 2]]))  # True
    print(s.canFinish(3, [[2, 1], [1, 0]]))  # True


if __name__ == "__main__":
    main()
