# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without repeating characters.

# Sliding window technique
# Complexity O(n)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Corner case
        if len(s) == 0:
            return 0

        longest: int = 0
        start: int = 0
        end: int = 1
        for i in range(1, len(s)):
            if s[i] in s[start:i]:
                # Check length of string
                if i - start > longest:
                    longest = i - start
                # Update window start
                start += s[start:i].find(s[i]) + 1

        if len(s) - start > longest:
            longest = len(s) - start
        return longest


def main():
    s = Solution()
    print('Expected: 3')
    print(f'Output  : {s.lengthOfLongestSubstring("abcabcbb")}')
    print('Expected: 1')
    print(f'Output  : {s.lengthOfLongestSubstring("bbbbb")}')
    print('Expected: 3')
    print(f'Output  : {s.lengthOfLongestSubstring("pwwkew")}')
    print('Expected: 0')
    print(f'Output  : {s.lengthOfLongestSubstring("")}')
    print('Expected: 2')
    print(f'Output  : {s.lengthOfLongestSubstring("abba")}')
    print('Expected: 2')
    print(f'Output  : {s.lengthOfLongestSubstring("aab")}')


if __name__ == '__main__':
    main()
