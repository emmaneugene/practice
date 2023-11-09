# Problem:  https://leetcode.com/problems/group-anagrams/description/

# Sorting each word is nlog(n), iterating m words gives overall time complexity
# of O(mnlog(n))

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mappings: dict[str, List[str]] = {}

        for _, s in enumerate(strs):
            sSorted = "".join(sorted(s))
            if sSorted in mappings:
                mappings[sSorted].append(s)
            else:
                mappings[sSorted] = [s]

        return mappings.values()


def main():
    s: Solution = Solution()

    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Expected: [['bat'],['nat','tan'],['ate','eat','tea']]
    print(s.groupAnagrams([""]))  # Expected: [['']]
    print(s.groupAnagrams(["a"]))  # Expected: [['a']]


if __name__ == "__main__":
    main()
