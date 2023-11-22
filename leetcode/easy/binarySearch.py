# Problem: https://leetcode.com/problems/binary-search/

# Time complexity: O(log(n))
# Space complexity: NA


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start: int = 0
        end: int = len(nums)

        while start < end:
            mid: int = start + (end - start) // 2

            print(f"Lookup {nums[mid]}")

            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                end = mid
            else:
                start = mid + 1

        return -1


def main():
    s: Solution = Solution()

    print(s.search([-1, 0, 3, 4, 9, 12], 9))  # Expected: 4
    print(s.search([-1, 0, 3, 4, 9, 12], 2))  # Expected: -1
    print(s.search([-1, 0, 3], 0))  # Expected: 1
    print(s.search([-1, 0], -1))  # Expected: 0
    print(s.search([-1, 0], 0))  # Expected: 1


if __name__ == "__main__":
    main()
