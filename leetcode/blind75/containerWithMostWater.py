# Problem: https://leetcode.com/problems/container-with-most-water
# Double pointers

from typing import List

# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Base case
        left: int = 0
        right: int = len(height) - 1

        maxArea: int = (right-left) * min(height[left], height[right])

        while (left < right):
            # Collapse smaller of left/right inwards
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            
            maxArea = max(maxArea, (right-left) * min(height[left], height[right]))

        return maxArea

def main():
    s: Solution = Solution()

    print('Expected: 49')
    print(f'Actual  : {s.maxArea([1,8,6,2,5,4,8,3,7])}')

    print('Expected: 1')
    print(f'Actual  : {s.maxArea([1,1])}')

if __name__ == '__main__':
    main()