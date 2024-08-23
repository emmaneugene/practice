# Problem: https://leetcode.com/problems/word-search

# Time complexity: O(m^2n^2)
# Space complexity: O(mn)
# Create a hashmap of character-coordinates, BFS/DFS to find sequence

from copy import deepcopy


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        tracker: dict[str, list[tuple[int, int]]] = {}

        rows = len(board)
        cols = len(board[0])

        # Create hashmap O(mn)
        for i in range(rows):
            for j in range(cols):
                ch = board[i][j]
                if ch in tracker:
                    tracker[ch].append((i, j))
                else:
                    tracker[ch] = [(i, j)]

        for ch in word:
            if ch not in tracker:
                return False

        toSearch: list[tuple[int, int]] = tracker[word[0]]

        # Search
        for coord in toSearch:
            visited: set = {coord}
            if self.DFS(tracker, visited, word[1:], coord):
                return True

        return False

    def DFS(
        self,
        tracker: dict[str, list],
        visited: set[tuple],
        word: str,
        prev: tuple[int, int],
    ) -> bool:
        """Recursively search for next character in word, and add it to a set of visited coordinates"""
        if len(word) == 0:
            return True

        nextCh: str = word[0]
        if nextCh not in tracker:
            return False

        toSearch: list[tuple(int, int)] = list(
            filter(
                lambda x: x not in visited and self.isAdjacent(prev, x), tracker[nextCh]
            )
        )

        for coord in toSearch:
            newVisited = deepcopy(visited)
            newVisited.add(coord)
            if self.DFS(tracker, newVisited, word[1:], coord):
                return True

        return False

    def isAdjacent(self, coord1: tuple[int, int], coord2: tuple[int, int]) -> bool:
        return (
            coord1[0] == coord2[0]
            and abs(coord1[1] - coord2[1]) == 1
            or coord1[1] == coord2[1]
            and abs(coord1[0] - coord2[0]) == 1
        )


def main():
    s = Solution()

    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"
        )
    )  # Expected: True

    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"
        )
    )  # Expected: True

    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCS"
        )
    )  # Expected: False

    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"
        )
    )  # Expected: False

    print(
        s.exist(
            [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]],
            "ABCESEEEFS",
        )
    )  # Expected: True

    print(
        s.exist([["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], "Z")
    )  # Expected: False


if __name__ == "__main__":
    main()
