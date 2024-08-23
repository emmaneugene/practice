# Problem: https://leetcode.com/problems/word-break

# Time: O(mn) for m words and n chars
# Space: O(n)
# Dynamic programming


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict.sort(key=lambda x: len(x))
        matchTracker: list[bool] = [False] * len(s)

        for word in wordDict:
            if len(word) > len(s):
                break
            if s.startswith(word):
                matchTracker[len(word) - 1] = True

        for i in range(1, len(s)):
            for word in wordDict:
                if len(word) > len(s[i:]):
                    break
                if matchTracker[i - 1] and s[i:].startswith(word):
                    matchTracker[i + len(word) - 1] = True

        return matchTracker[-1]


def main():
    s: Solution = Solution()

    print(s.wordBreak("leetcode", ["leet", "code"]))  # Expected: True
    print(s.wordBreak("applepenapple", ["apple", "pen"]))  # Expected: True
    print(
        s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    )  # Expected: False


if __name__ == "__main__":
    main()
