# Problem: https://leetcode.com/problems/alien-dictionary
# tags: blind75, hard

# Time complexity: O(C) - C = total characters across all words
# Space complexity: O(U^2) - U = unique characters, for ordering graph

# 1. Create a dict to track for each character, which characters it is smallr than
#    e.g. {'a': {}, 'b': {'a'}, 'c': {'a', 'b'}} implies the order a -> b -> c
# 2. Check each string in `words` to get ordering information. If a continuous sequence of strings
#    are found which start with the same letter, take [1:] slice of each and put them in a new list
#    to be checked. Do this until there are no more lists to check
# 3. To build the string, grab all the entries and start with the one with the least sets

# - for strings with no comparison information, any arbitrary ordering works?
# - e.g. ['ak', 'bd'] can have an ordering of ['abkd', 'abdk'] and more?

# If a contradiction is encountered, return "" immediately
# Need to maintain a queue of strings to check

# Alternative solutions:
# 1. BFS topological sort (Kahn's algorithm) - graph, BFS, indegree tracking [implemented]
#    Time: O(C) | Space: O(U + min(U^2, N))
# 2. DFS topological sort - graph, DFS, cycle detection via coloring
#    Time: O(C) | Space: O(U + min(U^2, N))

import copy


class Solution:
    def alienOrder(self, words: list[str]) -> str:
        ordering: dict[str, set] = {}
        toCheck = [list(filter(lambda x: x, words))]

        while toCheck:
            toCompare = toCheck.pop(0)
            # print(f"Comparing first characters of: {toCompare}")
            if not any(toCompare):
                continue

            nextWrd = toCompare[0]
            sequence = [nextWrd[0]]
            toAdd = []
            if nextWrd[1:]:
                toAdd.append(nextWrd[1:])

            # Build ordering
            for word in toCompare[1:]:
                if word[0] != sequence[-1]:
                    if any(toAdd):
                        toCheck.append(toAdd)
                    sequence.append(word[0])
                    toAdd = []

                # Contradiction - Empty string cannot be ordered after letters
                if not word[1:] and toAdd:
                    return ""
                if word[1:]:
                    toAdd.append(word[1:])

            if any(toAdd):
                toCheck.append(toAdd)

            # print(f"Got ordering: {sequence}")
            ch = sequence[0]
            if not ordering.get(ch):
                ordering[ch] = set()

            smallerChars = copy.deepcopy(ordering.get(ch))
            smallerChars.add(ch)

            for ch in sequence[1:]:
                # Check for contradictions
                for sm in smallerChars:
                    if ordering.get(sm) and ch in ordering.get(sm):
                        return ""

                # Update for ch
                if ordering.get(ch):
                    ordering[ch] = ordering[ch].union(smallerChars)
                else:
                    ordering[ch] = smallerChars

                smallerChars = copy.deepcopy(ordering.get(ch))
                smallerChars.add(ch)

        items = list(ordering.items())
        items.sort(key=lambda x: len(x[1]))

        # for ch, smaller in items:
        #     print(f"{ch} comes after {smaller if smaller else "nothing (first in sequence)"}")

        return "".join([x[0] for x in items])


def main():
    s = Solution()

    print(s.alienOrder(["wrt", "wrf", "er", "ett", "rftt"]))  # Expected: "wertf"
    print(s.alienOrder(["z", "x"]))  # Expected: "zx"
    print(s.alienOrder(["z", "x", "z"]))  # Expected: ""
    print(s.alienOrder(["abc", "ab"]))  # Expected: ""


if __name__ == "__main__":
    main()
