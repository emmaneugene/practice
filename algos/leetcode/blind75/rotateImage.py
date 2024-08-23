# Problem: https://leetcode.com/problems/rotate-image

# Time complexity: O(n^2)
# Space complexity: O(n^2)


class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """Rotate a n*n matrix 90 degrees clockwise in-place"""

        n = len(matrix)

        for i in range(n // 2):
            for j in range(i, n - i - 1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n - j - 1][i]
                matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
                matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
                matrix[j][n - i - 1] = tmp


def main():
    s = Solution()
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    s.rotate(arr)
    print("Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]")
    print("Output  :", arr)

    arr = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(arr)
    print("Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]")
    print("Output  :", arr)


if __name__ == "__main__":
    main()
