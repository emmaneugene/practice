# Problem: https://leetcode.com/problems/longest-palindromic-substring
# tags: blind75, medium

# Time complexity: O(n^2)
# Space complexity: O(n)

# Decreasing window of size=len(s) to 1

# Alternative solutions:
# 1. Brute force - check all substrings [implemented]
#    Time: O(n^3) | Space: O(n)
# 2. Expand around center - two pointers
#    Time: O(n^2) | Space: O(1)
# 3. Dynamic programming - 2D DP table
#    Time: O(n^2) | Space: O(n^2)
# 4. Manacher's algorithm - linear palindrome detection
#    Time: O(n) | Space: O(n)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(s: str):
            for i in range(len(s) // 2):
                if s[i] != s[-1-i]:
                    return False
            return True

        if not s:
            return ""

        size = len(s)

        while size > 1:
            for i in range(len(s) - size + 1):
                if isPalindrome(s[i: i+size]):
                    return s[i: i+size]
            size -= 1

        return s[0]



def main():
    s = Solution()
    print(s.longestPalindrome(None))  # ""
    print(s.longestPalindrome(""))  # ""
    print(s.longestPalindrome("babad"))  # "bab" OR "aba"
    print(s.longestPalindrome("cbbd"))  # "bb"


if __name__ == "__main__":
    main()
