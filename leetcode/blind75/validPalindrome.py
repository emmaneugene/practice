# Problem: https://leetcode.com/problems/valid-palindrome/

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        out = ""
        for i in s:
            if i.isalnum():
                out += i.lower()

        for i in range(len(out) // 2):
            if out[i] != out[-1 - i]:
                return False

        return True


def main():
    s: Solution = Solution()

    print(s.isPalindrome("A man, a plan, a canal: Panama"))  # True
    print(s.isPalindrome("race a car"))  # False
    print(s.isPalindrome(" "))  # False
    print(s.isPalindrome("0P"))  # False


if __name__ == "__main__":
    main()
