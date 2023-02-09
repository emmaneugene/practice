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
        chars: dict = {
            s[0]: 0
        }
        for i in range(1, len(s)):
            if s[i] in chars:
                # Check length of string
                if i - start > longest:
                    print(f'Found string {s[start:i]} with length {i - start}')
                    longest = i - start
                # Update window start
                start = chars.get(s[i]) + 1
                chars = dict(filter(lambda x: x[1] >= start, chars.items()))
            
            chars[s[i]] = i
            
        print("Outside loop")
        if len(s) - start > longest:
            print(f'Found string {s[start:len(s)]} with length {len(s) - start}')
            longest = len(s) - start
        return longest 

def main():
    s = Solution()
    print(f'Actual  : {s.lengthOfLongestSubstring("abcabcbb")}')
    print('Expected: 3')
    print(f'Actual  : {s.lengthOfLongestSubstring("bbbbb")}')
    print('Expected: 1')
    print(f'Actual  : {s.lengthOfLongestSubstring("pwwkew")}')
    print('Expected: 3')
    print(f'Actual  : {s.lengthOfLongestSubstring("")}')
    print('Expected: 0')
    print(f'Actual  : {s.lengthOfLongestSubstring("abba")}')
    print('Expected: 2')

if __name__ == '__main__':
    main()