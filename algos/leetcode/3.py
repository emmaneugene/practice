# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters
# tags: blind75, medium

# Time complexity: O(n)
# Space complexity: O(n)
# Sliding window technique


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = 0
        longest = 0
        idx = 0
        tracked: set[str] = set()

        for i in range(len(s)):
            if s[i] in tracked:
                longest = max(longest, curr)
                newStart: int = idx + s[idx:i].find(s[i]) + 1

                for j in range(idx, newStart):
                    tracked.remove(s[j])
                    curr -= 1

                idx = newStart

            tracked.add(s[i])
            curr += 1

        return max(longest, curr)


def main():
    s = Solution()

    print(s.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
    print(s.lengthOfLongestSubstring("bbbbb"))  # Expected: 1
    print(s.lengthOfLongestSubstring("pwwkew"))  # Expected: 3
    print(s.lengthOfLongestSubstring(""))  # Expected: 0
    print(s.lengthOfLongestSubstring("abba"))  # Expected: 2
    print(s.lengthOfLongestSubstring("aab"))  # Expected: 2


if __name__ == "__main__":
    main()
