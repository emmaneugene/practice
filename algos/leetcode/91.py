# Problem: https://leetcode.com/problems/decode-ways
# tags: blind75, medium

# Time complexity: O(n)
# Space complexity: O(n) (can be made smaller by throwing away old values)
# General approach: Iteratively process string from right to left
#
# Alternative solutions:
# 1. Recursion with memoization - top-down, try decoding 1 or 2 chars at each position
#    Time: O(n) | Space: O(n)
# 2. DP array (bottom-up) - iterate right to left, store counts in array [implemented]
#    Time: O(n) | Space: O(n)
# 3. DP with constant space - only keep two previous values instead of full array
#    Time: O(n) | Space: O(1)


class Solution:
    def numDecodings(self, s: str) -> int:
        sLen = len(s)
        # Corner cases
        if sLen == 0 or s.startswith("0"):
            return 0
        if sLen == 1:
            return 1

        charEncodings: set[str] = {
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "10",
            "11",
            "12",
            "13",
            "14",
            "15",
            "16",
            "17",
            "18",
            "19",
            "20",
            "21",
            "22",
            "23",
            "24",
            "25",
            "26",
        }

        tracker: list[int] = [0] * sLen

        # Process counts for last and second last character substrings
        if s[sLen - 1] in charEncodings:
            tracker[sLen - 1] = 1
        if s[sLen - 2] in charEncodings:
            tracker[sLen - 2] += tracker[sLen - 1]
        if s[sLen - 2 :] in charEncodings:
            tracker[sLen - 2] += 1

        for i in range(sLen - 3, -1, -1):
            count: int = 0
            if s[i] in charEncodings:
                count += tracker[i + 1]
            if s[i : i + 2] in charEncodings:
                count += tracker[i + 2]

            tracker[i] = count

        return tracker[0]


def main():
    s = Solution()

    print(s.numDecodings("12"))  # Expected: 2
    print(s.numDecodings("226"))  # Expected: 3
    print(s.numDecodings("06"))  # Expected: 0


if __name__ == "__main__":
    main()
