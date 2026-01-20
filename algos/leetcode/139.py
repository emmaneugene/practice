# Problem: https://leetcode.com/problems/word-break
# tags: blind75, medium

# Time: O(mn) for m words and n chars
# Space: O(n)
# Dynamic programming


class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordDict.sort(key=lambda x: len(x))
        tracker: list[bool] = [False] * len(s)

        for word in wordDict:
            if len(word) > len(s):
                break
            if s.startswith(word):
                tracker[len(word) - 1] = True

        for i in range(1, len(s)):
            for word in wordDict:
                if len(word) > len(s[i:]):
                    break
                if tracker[i - 1] and s[i:].startswith(word):
                    tracker[i + len(word) - 1] = True

        return tracker[-1]


def main():
    s = Solution()

    print(s.wordBreak("leetcode", ["leet", "code"]))  # Expected: True
    print(s.wordBreak("applepenapple", ["apple", "pen"]))  # Expected: True
    print(
        s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"])
    )  # Expected: False


if __name__ == "__main__":
    main()
