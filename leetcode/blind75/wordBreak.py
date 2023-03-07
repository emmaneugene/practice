# Problem: https://leetcode.com/problems/word-break/

# Dynamic programming
# Time: O(n)
# Space: O(n)

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key=lambda x: len(x))
        matchedToChar: List[bool] = [False] * len(s)

        for word in wordDict:
            if len(word) > len(s):
                break
            if s.startswith(word):
                matchedToChar[len(word)-1] = True

        for i in range(1, len(s)):
            for word in wordDict:
                if len(word) > len(s):
                    break
                if matchedToChar[i-1] and s[i:].startswith(word):
                    matchedToChar[i+len(word)-1] = True

        return matchedToChar[-1]


def main():
    s: Solution = Solution()

    print(s.wordBreak('leetcode', ['leet', 'code']))  # Expected: True
    print(s.wordBreak('applepenapple', ['apple', 'pen']))  # Expected: True
    # Expected: False
    print(s.wordBreak('catsandog', ['cats', 'dog', 'sand', 'and', 'cat']))


if __name__ == '__main__':
    main()
