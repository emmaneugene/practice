# Problem: https://leetcode.com/problems/valid-parentheses

# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def matchingBrackets(self, opening: str, closing: str):
        matches = {"{": "}", "[": "]", "(": ")"}

        return matches[opening] == closing

    def isValid(self, s: str) -> bool:
        open_braces = []

        for ch in s:
            if ch in "{([":
                open_braces.append(ch)
            else:
                if not open_braces:
                    return False

                opening = open_braces.pop()
                if not self.matchingBrackets(opening, ch):
                    return False

        return not any(open_braces)


def main():
    s = Solution()

    print(s.isValid("()"))  # True
    print(s.isValid("()[]{}"))  # True
    print(s.isValid("(]"))  # False
    print(s.isValid("([])"))  # False


if __name__ == "__main__":
    main()
