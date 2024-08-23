# Problem: https://leetcode.com/problems/valid-anagram

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tracker: dict[str, int] = {}

        for ch in s:
            if ch not in tracker:
                tracker[ch] = 1
            else:
                tracker[ch] += 1

        for ch in t:
            if ch not in tracker:
                return False
            tracker[ch] -= 1

        for count in tracker.values():
            if count != 0:
                return False
        return True


def main():
    s: Solution = Solution()

    print(s.isAnagram("anagram", "nagaram"))  # True
    print(s.isAnagram("rat", "car"))  # False


if __name__ == "__main__":
    main()
