# Problem: https://leetcode.com/problems/valid-palindrome
# tags: blind75, easy

# Time complexity: O(n)
# Space complexity: O(n)

# Alternative solutions:
# 1. Filter + reverse comparison - string filtering, reverse
#    Time: O(n) | Space: O(n)
# 2. Filter + two-pointer comparison - string filtering, iteration [implemented]
#    Time: O(n) | Space: O(n)
# 3. In-place two pointers - two pointers, no extra string
#    Time: O(n) | Space: O(1)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = "".join(c for c in s if c.isalnum()).lower()

        for i in range(len(out) // 2):
            if out[i] != out[-1 - i]:
                return False
        return True


def main():
    s = Solution()

    print(s.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(s.isPalindrome("race a car"))  # False
    print(s.isPalindrome(" "))  # True
    print(s.isPalindrome("0P"))  # False


if __name__ == "__main__":
    main()
