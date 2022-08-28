# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Corner case
        if len(s) == 0:
            return 0

        result = 1

        for i in range(len(s)):
            idx = i

            characters = {}
            substring_length = 0
            repeat_found = False

            while not repeat_found and idx < len(s):
                if characters.get(s[idx]):
                    repeat_found = True
                else:
                    characters[s[idx]] = 1
                    substring_length += 1
                idx += 1

            if substring_length > result:
                result = substring_length

        return result
