# Problem: https://leetcode.com/problems/longest-palindromic-substring

# Time complexity: O(n^2)
# Space complexity: O(n)

# Loop over all chars and look for odd/even length palindromes
# Odd:
# abcba
#   ^
# Even:
# abba
#  ^


class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = s[0]

        for i in range(len(s)):
            result = max(result, self.getSubPalindrome(s, i), key=lambda s: len(s))

        return result

    def getSubPalindrome(self, s: str, i: int) -> str:
        """Returns the longest even or odd palindrome of with s[i] at its centre"""

        oddOffset = 0
        evenOffset = 0

        while (
            i - oddOffset - 1 >= 0
            and i + oddOffset + 1 < len(s)
            and s[i - oddOffset - 1] == s[i + oddOffset + 1]
        ):
            oddOffset += 1

        if i + 1 == len(s) or s[i] != s[i + 1]:
            return s[i - oddOffset : i + oddOffset + 1]

        while (
            i - evenOffset - 1 >= 0
            and i + evenOffset + 2 < len(s)
            and s[i - evenOffset - 1] == s[i + evenOffset + 2]
        ):
            evenOffset += 1

        return max(
            s[i - oddOffset : i + oddOffset + 1],
            s[i - evenOffset : i + evenOffset + 2],
            key=lambda s: len(s),
        )


def main():
    s = Solution()
    print(s.longestPalindrome("babad"))  # "bab" OR "aba"
    print(s.longestPalindrome("cbbd"))  # "bb"


if __name__ == "__main__":
    main()
