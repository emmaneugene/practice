# Problem: https://leetcode.com/problems/longest-repeating-character-replacement


# Time complexity: O(n^2)
# Space complexity: O(n^2)
# Sliding window technique


class Tracker:
    """Convenience class that tracks the first character of a repeating sequence, its length, and number of replacements left"""

    # TODO: Some way of dealing with wildcard
    def __init__(self, char: str, length: int, replacements: int) -> None:
        self.char: str = char
        self.length: int = length
        self.replacements: int = replacements


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest: int = 1

        currCh: str = s[0]
        currTrackers: list[Tracker] = []
        currTrackers.append(Tracker(currCh, 1, k))

        for i in range(1, len(s)):
            newTrackers: list[Tracker] = []
            for t in currTrackers:
                if t.char != s[i]:
                    if t.replacements > 0:
                        t.length += 1
                        t.replacements -= 1
                        newTrackers.append(t)
                    else:
                        longest = max(longest, t.length)
                else:
                    t.length += 1
                    newTrackers.append(t)

            if currCh != s:
                currCh = s[i]
                newTrackers.append(Tracker(currCh, 1, k))

            currTrackers = newTrackers

        for t in currTrackers:
            longest = max(longest, t.length)

        return longest


def main():
    s: Solution = Solution()

    print(s.characterReplacement("ABAB", 2))  # Expected: 1
    print(s.characterReplacement("AABABBA", 1))  # Expected: 4


if __name__ == "__main__":
    main()
