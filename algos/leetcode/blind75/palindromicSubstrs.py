# Problem: https://leetcode.com/problems/palindromic-substrings

# Time complexity: O(n^2)
# Space complexity: O(1)


class Solution:
    def countSubstrings(self, s: str):
        count = len(s)

        for i in range(len(s)):
            oddLimit = min(i, len(s) - 1 - i)
            evenLimit = min(i + 1, len(s) - 1 - i)

            # Odd-length palindromes
            for j in range(1, oddLimit + 1):
                if s[i - j] != s[i + j]:
                    break
                count += 1

            # Even-length palindromes
            for j in range(evenLimit):
                if s[i - j] != s[i + 1 + j]:
                    break
                count += 1

        return count


def main():
    s = Solution()

    print(s.countSubstrings("abc"))  # Expected: 3
    print(s.countSubstrings("aaa"))  # Expected: 6


if __name__ == "__main__":
    main()
