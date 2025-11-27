# Problem: https://leetcode.com/problems/container-with-most-water

# Time complexity: O(n)
# Space complexity: O(1)
# Double pointers


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # Base case
        left = 0
        right = len(height) - 1
        maxArea = (right - left) * min(height[left], height[right])

        while left < right:
            # Collapse smaller of left/right inwards
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

            maxArea = max(maxArea, (right - left) * min(height[left], height[right]))

        return maxArea


def main():
    s = Solution()

    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # Expected: 49
    print(s.maxArea([1, 1]))  # Expected: 1


if __name__ == "__main__":
    main()
