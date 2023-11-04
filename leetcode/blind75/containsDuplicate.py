# Problem: https://leetcode.com/problems/contains-duplicate/

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        unique: set = set()
        for n in nums:
            if n in unique:
                return True
            unique.add(n)

        return False


def main():
    s: Solution = Solution()

    print(s.containsDuplicate([1, 2, 3, 1]))  # True
    print(s.containsDuplicate([1, 2, 3, 4]))  # False
    print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))  # True


if __name__ == "__main__":
    main()
