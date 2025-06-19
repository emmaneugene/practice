# Problem: https://leetcode.com/problems/longest-repeating-character-replacement


# Time complexity: O(n)
# Space complexity: O(n^2)
# Single loop to find sequences of identical characters, then explore all possible character
# substitutions


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = min(len(s), k + 1)
        if len(s) <= 1 + k:
            return longest

        tracker: dict[str, list] = {}
        start = 0
        currCh = s[0]
        for i in range(1, len(s)):
            if s[i] != currCh:
                seq = (start, i)
                if currCh not in tracker:
                    tracker[currCh] = [seq]
                else:
                    tracker[currCh].append(seq)
                start = i
                currCh = s[i]

        if currCh not in tracker:
            tracker[currCh] = [(start, len(s))]
        else:
            tracker[currCh].append((start, len(s)))

        for ch, locs in tracker.items():
            longest = max(longest, self.helper(s, locs, k))

        return longest

    def helper(self, s: str, chunks: list[int], k: int) -> int:
        res = k + 1

        for i, chunk in enumerate(chunks):
            idx = i
            start = chunk[0]
            end = chunk[1]
            replace = k

            while replace > 0:
                idx += 1
                if idx == len(chunks):
                    canSub = min((len(s) - end) + (start), replace)
                    res = max(res, end - start + canSub)
                    break

                diff = chunks[idx][0] - end
                if diff > replace:
                    end += replace
                    replace = 0
                else:
                    end = chunks[idx][1]
                    replace -= diff

            res = max(res, end - start)

        return res

    # TODO: Use greedy algo in helper instead?
    # def helper(self, s: str, chunks: list[int], k: int) -> int:
    #     start = 0
    #     end = len(chunks) - 1
    #     replaced = 0

    #     for i in range(1, len(chunks)):
    #         replaced += chunks[i][0] - chunks[i - 1][1]

    #     remaining = chunks[start][0] + (len(s) - chunks[end][1])

    #     if replaced < k:
    #         remaining = min(k - replaced, remaining)
    #         return (chunks[end][1] - chunks[start][0]) + remaining

    #     remaining = 0
    #     while replaced > k:
    #         if (chunks[start][1] - chunks[start][0]) < (
    #             chunks[end][1] - chunks[end][0]
    #         ):
    #             start += 1
    #             remaining = chunks[start][0] - chunks[start - 1][1]
    #         else:
    #             end -= 1
    #             remaining = chunks[end + 1][0] - chunks[end][1]

    #         toRemove = min(remaining, replaced - k)
    #         remaining -= toRemove
    #         replaced -= toRemove

    #     return (chunks[end][1] - chunks[start][0]) + remaining


def main():
    s = Solution()

    print(s.characterReplacement("A", 0))  # Expected: 1
    print(s.characterReplacement("ABAB", 2))  # Expected: 4
    print(s.characterReplacement("AABABBA", 1))  # Expected: 4
    print(s.characterReplacement("ABBB", 2))  # Expected: 4
    print(s.characterReplacement("BAAAB", 2))  # Expected: 5


if __name__ == "__main__":
    main()
