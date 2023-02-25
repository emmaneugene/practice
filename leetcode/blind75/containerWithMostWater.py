# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

from typing import List


class Solution:
    # General idea: Start with walls of the containers as max and second max walls, make incremental improvements to find greatest possible volume.

    # Once you have the above arrangement, you can either:
    # 1) Move end pointer forward to increase volume
    # 2) Move start pointer back to increase volume

    def maxArea(self, height: List[int]) -> int:
        # Base case
        start: int = 0
        end: int = 1

        maxArea: int = min(height[start], height[end]) * (end - start)

        return maxArea
