# Problem: https://leetcode.com/problems/bus-routes
# tags: hard
# Basically Dijkstra's algo

# Time complexity: O(N * S) - N = number of routes, S = total stops across all routes
# Space complexity: O(N * S) - for stopToRoutes map and visited sets

# Alternative solutions:
# 1. BFS on stops - treat each stop as a node, expand via routes [implemented]
#    Time: O(N * S) | Space: O(N * S)
# 2. BFS on routes - build route-to-route graph via shared stops
#    Time: O(N^2 * S) build + O(N) BFS | Space: O(N^2 + N * S)

from typing import Dict, List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        busCount = 0
        if source == target:
            return busCount

        stopToRoutes: Dict[int, List[int]] = {}
        for route, stops in enumerate(routes):
            for stop in stops:
                if stop not in stopToRoutes:
                    stopToRoutes[stop] = []
                stopToRoutes[stop].append(route)

        if source not in stopToRoutes or target not in stopToRoutes:
            return -1

        explore = set([source])
        visitedRoutes = set()
        visitedStops = set([source])

        while explore:
            tmp = set()
            for e in explore:
                for route in stopToRoutes[e]:
                    if route not in visitedRoutes:
                        for stop in routes[route]:
                            # Add to tmp if not visited
                            if stop not in visitedStops:
                                visitedStops.add(stop)
                                tmp.add(stop)
                        visitedRoutes.add(route)

            busCount += 1
            if target in visitedStops:
                return busCount
            explore = tmp

        return -1


def main():
    s = Solution()

    print(s.numBusesToDestination([[1, 2, 7], [3, 6, 7]], 1, 6))  # Expected: 2
    print(
        s.numBusesToDestination(
            [[7, 12], [4, 5, 15], [6], [15, 19], [9, 12, 13]], 15, 12
        )
    )  # Expected: -1


if __name__ == "__main__":
    main()
