# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.

# Time complexity: O(n)
# Space complexity: O(n)
# Sliding window technique


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = 0
        longest = 0
        idx = 0
        tracked: set[str] = set()

        for i in range(len(s)):
            if s[i] in tracked:
                longest = max(longest, curr)
                newStart: int = idx + s[idx:i].find(s[i]) + 1

                for j in range(idx, newStart):
                    tracked.remove(s[j])
                    curr -= 1

                idx = newStart

            tracked.add(s[i])
            curr += 1

        return max(longest, curr)


def main():
    s = Solution()
    print("Expected: 3")
    print(f'Output  : {s.lengthOfLongestSubstring("abcabcbb")}')
    print("Expected: 1")
    print(f'Output  : {s.lengthOfLongestSubstring("bbbbb")}')
    print("Expected: 3")
    print(f'Output  : {s.lengthOfLongestSubstring("pwwkew")}')
    print("Expected: 0")
    print(f'Output  : {s.lengthOfLongestSubstring("")}')
    print("Expected: 2")
    print(f'Output  : {s.lengthOfLongestSubstring("abba")}')
    print("Expected: 2")
    print(f'Output  : {s.lengthOfLongestSubstring("aab")}')


if __name__ == "__main__":
    main()
