# Problem: https://leetcode.com/problems/longest-common-subsequence/

# Dynamic programming, starting from first character of first string and iteratively 
# storing the longest subsequences that end with that character

# Somewhat similar to longestIncrSubsequence
from typing import List, Dict

# Complexity: O(n^2)
class Match:
    '''For a reference text (text2), tracks the index of a matched character in the source text (text1) which gives the 
    longest sequence so far. Not necessary for us to track the character itself, but this can be included if we want to
    return the string
    '''

    def __init__(self, matchedAt: int = -1, length: int = 0) -> None:
        self.matchedAt = matchedAt
        self.length = length

    def __str__(self) -> str:
        return f'[{self.matchedAt}, {self.length}]'

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        occurrences: Dict[str, List[int]] = {}

        for i2, ch2 in enumerate(text2):
            if ch2 in occurrences:
                occurrences[ch2].append(i2)
            else:
                occurrences[ch2] = [i2]

        # Stores the best match at each character of text2
        matches: List[Match] = []
            
        for i2 in range(len(text2)):
            matches.append(Match())
            
        for i1, ch1 in enumerate(text1):
            if ch1 in occurrences:

                # Create new set of matches
                newMatches: Dict[int, Match] = {}
                i2s: List[int] = occurrences[ch1]

                for i2 in i2s:
                    newLength = 1
                    for match in matches[:i2]:
                        if match.matchedAt < i1 and match.length >= newLength:
                            newLength = match.length + 1
                    
                    newMatches[i2] = Match(i1, newLength)

                # Update existing matches
                for k, v in newMatches.items():
                    matches[k] = v


        # for match in matches:
        #     print(match)
        return max(matches, key=lambda x: x.length).length

def main():
    s: Solution = Solution()

    print(s.longestCommonSubsequence('abcde', 'ace')) # Expected: 3
    print(s.longestCommonSubsequence('abc', 'abd')) # Expected: 2
    print(s.longestCommonSubsequence('abc', 'def')) # Expected: 0


if __name__ == '__main__':
    main()