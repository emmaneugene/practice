# Given a string s, return the longest palindromic substring in s

class Solution:
    # General idea: Loop over all characters in the string

    # That character can either be the middle of an odd-count palindrome, or middle-left of an
    # even palindrome. In both cases, we can write functions that perform an O(n) search for the
    # palindrome

    # Odd:
    # abcba
    #   ^
    # Even:
    # abba
    #  ^

    # Therefore, we should be able to find every single palindrome in the string with just
    # one loop
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        for i in range(len(s)):
            oddPalindrome: str = self.getLongestOddPalindrome(s, i)
            evenPalindrome: str = self.getLongestEvenPalindrome(s, i)

            result = oddPalindrome if len(
                oddPalindrome) > len(result) else result
            result = evenPalindrome if len(
                evenPalindrome) > len(result) else result

        return result

    # Return the longest odd-counted palindrome of <s> with <i> as its centre
    def getLongestOddPalindrome(self, s: str, i: int) -> str:
        result = s[i]
        count: int = 1
        matching: bool = True

        while i - count >= 0 and i + count < len(s) and matching:
            if s[i-count] == s[i+count]:
                result = s[i-count: i+count+1]
            else:
                matching = False
            count += 1

        return result

    # Return the longest even-counted palindrome of <s> with <i> as the centre-left character
    def getLongestEvenPalindrome(self, s: str, i: int) -> str:
        result = s[i]
        count: int = 0
        matching: bool = True

        while i - count >= 0 and i + count + 1 < len(s) and matching:
            if s[i-count] == s[i+count+1]:
                result = s[i-count: i+count+2]
            else:
                matching = False
            count += 1

        return result
