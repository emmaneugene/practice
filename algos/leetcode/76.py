# Problem: https://leetcode.com/problems/minimum-window-substring
# tags: blind75, hard

# Time complexity: O(n)
# Space complexity: O(n)

from typing import Dict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        track: Dict[str, int] = {}

        for tmp in t:
            if tmp in track:
                track[tmp] += 1
            else:
                track[tmp] = 1

        toFind = set(track.keys())
        start = -1
        end = -1

        for i, tmp in enumerate(s):
            if tmp in track:
                start = i
                break

        if start == -1:
            return ""

        for i, tmp in enumerate(s[start:], start):
            if not any(toFind):
                end = i
                break
            if tmp in track:
                track[tmp] -= 1
                if track[tmp] == 0:
                    toFind.remove(tmp)

        if end == -1:
            if not any(toFind):
                end = len(s)
            else:
                return ""

        res = s[start:end]

        while end < len(s):
            tmp = s[start]
            start += 1

            if tmp in track:
                track[tmp] += 1
                if track[tmp] > 0:
                    toFind.add(tmp)

                while any(toFind) and end < len(s):
                    if s[end] in track:
                        track[s[end]] -= 1
                    if s[end] in toFind and track[s[end]] == 0:
                        toFind.remove(s[end])
                    end += 1

            if not any(toFind) and len(s[start:end]) < len(res):
                res = s[start:end]

        while start < len(s):
            if s[start] in track:
                track[s[start]] += 1
                if track[s[start]] > 0:
                    break
            start += 1

        if not any(toFind) and len(s[start:]) < len(res):
            res = s[start:]

        return res


def main():
    s = Solution()

    print(s.minWindow("ADOBECODEBANC", "ABC"))  # Expected: 'BANC'
    print(s.minWindow("a", "a"))  # Expected: 'a'
    print(s.minWindow("a", "aa"))  # Expected: ''


if __name__ == "__main__":
    main()
