# Problem:  https://leetcode.com/problems/group-anagrams
# tags: blind75, medium

# Time complexity: O(nmlog(m))
# Space complexity: O(n)
# Sorting each word of average length m is mlog(m), iterating n words gives overall time complexity
# of O(nmlog(m))
#
# Alternative solutions:
# 1. Brute force - compare every pair of strings
#    Time: O(n^2 * m) | Space: O(n * m)
# 2. Sorted string as key - hash map, sorting [implemented]
#    Time: O(n * m log m) | Space: O(n * m)
# 3. Character frequency as key - hash map, counting
#    Time: O(n * m) | Space: O(n * m)


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        mappings: dict[str, list[str]] = {}

        for _, s in enumerate(strs):
            sSorted = "".join(sorted(s))
            if sSorted in mappings:
                mappings[sSorted].append(s)
            else:
                mappings[sSorted] = [s]

        return mappings.values()


def main():
    s = Solution()

    print(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # Expected: [['bat'],['nat','tan'],['ate','eat','tea']]
    print(s.groupAnagrams([""]))  # Expected: [['']]
    print(s.groupAnagrams(["a"]))  # Expected: [['a']]


if __name__ == "__main__":
    main()
