# Problem: https://leetcode.com/problems/minimum-window-substring/

from typing import Dict, List

# General idea: Come up with set of char Idxs that minimize window length
# Sliding window technique (again)
# Given I have to start at this idx, what is the smallest idx I can stop at?

# TODO: Complexity analysis
# Time complexity:
# Space complexity:


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Check if characters in t are present and have correct quantities in s
        tChCounts: Dict[str, int] = {}
        sChIdxs: Dict[str, List[int]] = {}

        for i, ch in enumerate(s):
            if ch not in sChIdxs:
                sChIdxs[ch] = [i]
            else:
                sChIdxs[ch].append(i)

        for ch in t:
            if ch not in tChCounts:
                tChCounts[ch] = 1
            else:
                tChCounts[ch] += 1

        for k, v in tChCounts.items():
            if k not in sChIdxs or len(sChIdxs[k]) < v:
                return ""

        # DP: Sliding window
        idxs: List[int] = []

        for ch in tChCounts.keys():
            idxs.extend(sChIdxs[ch])

        idxs.sort()

        currStartIdx: int = 0
        currEndIdx: int = 0
        currWindow: Dict[str, int] = {ch: 0 for ch in tChCounts.keys()}

        self.addCounts(currWindow, s[idxs[currStartIdx] : idxs[currEndIdx] + 1])

        # Find first valid window
        while not self.validWindow(currWindow, tChCounts):
            currEndIdx += 1
            self.addCounts(
                currWindow, s[idxs[currEndIdx - 1] + 1 : idxs[currEndIdx] + 1]
            )

        minStart: int = idxs[currStartIdx]
        minEnd: int = idxs[currEndIdx] + 1

        # Corner case: Smallest window found (1 character)
        if currStartIdx == currEndIdx:
            return s[minStart:minEnd]

        # Continue searching for new valid windows
        while currEndIdx < len(idxs):
            # Update start
            currStartIdx += 1
            self.removeCounts(
                currWindow, s[idxs[currStartIdx - 1] : idxs[currStartIdx]]
            )

            # Update end
            while not self.validWindow(currWindow, tChCounts):
                currEndIdx += 1

                if currEndIdx == len(idxs):
                    break

                self.addCounts(
                    currWindow, s[idxs[currEndIdx - 1] + 1 : idxs[currEndIdx] + 1]
                )

            if (
                self.validWindow(currWindow, tChCounts)
                and (idxs[currEndIdx] + 1) - idxs[currStartIdx] < minEnd - minStart
            ):
                minStart = idxs[currStartIdx]
                minEnd = idxs[currEndIdx] + 1

        return s[minStart:minEnd]

    def validWindow(self, window: Dict[str, int], chCounts: Dict[str, int]) -> bool:
        for k in chCounts.keys():
            if window[k] < chCounts[k]:
                return False

        return True

    def addCounts(self, window: Dict[str, int], s: str) -> None:
        for ch in s:
            if ch in window:
                window[ch] += 1

    def removeCounts(self, window: Dict[str, int], s: str) -> None:
        for ch in s:
            if ch in window:
                window[ch] -= 1


def main():
    s: Solution = Solution()

    print(s.minWindow("ADOBECODEBANC", "ABC"))  # Expected: 'BANC'
    print(s.minWindow("a", "a"))  # Expected: 'a'
    print(s.minWindow("a", "aa"))  # Expected: ''


if __name__ == "__main__":
    main()
