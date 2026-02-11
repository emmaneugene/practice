# Problem: https://leetcode.com/problems/word-break
# tags: blind75, medium

# Time complexity: O(mn) for m words and n chars
# Space complexity: O(n)
# Dynamic programming

# Alternative solutions:
# 1. Brute force recursion - try every partition, backtracking
#    Time: O(2^n) | Space: O(n)
# 2. Recursion with memoization - top-down DP, hash map
#    Time: O(n^2 * m) | Space: O(n)
# 3. Bottom-up DP - boolean DP array, word matching [implemented]
#    Time: O(n^2 * m) | Space: O(n)
# 4. BFS - treat indices as graph nodes, BFS over reachable positions
#    Time: O(n^2 * m) | Space: O(n)
# 5. Trie + DP - trie for dictionary, DP for segmentation
#    Time: O(n^2 + m * k) | Space: O(n + m * k)


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
