# Problem: https://leetcode.com/problems/word-search/

from copy import deepcopy
from typing import Dict, List, Set, Tuple

# General idea: perform a recursive search, storing coords of previously visited
# locations so we don't revisit


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        tracker: Dict[str, int] = {}
        searchStarts: List[Tuple[int, int]] = []

        rows: int = len(board)
        cols: int = len(board[0])
        startCh: str = word[0]

        for i in range(rows):
            for j in range(cols):
                ch: str = board[i][j]
                if ch in tracker:
                    tracker[ch] += 1
                else:
                    tracker[ch] = 1

                if ch == startCh:
                    searchStarts.append((i,j))

        for ch in word:
            if ch not in tracker:
                return False
            else:
                tracker[ch] -= 1
                if tracker[ch] < 0:
                    return False

        for coord in searchStarts:
            visited: Set[Tuple[int, int]] = {coord}
            if self.search(board, word[1:], coord, visited):
                return True

        return False

    
    def search(self, board: List[List[str]], word: str, curr: Tuple[int, int], visited: Set[Tuple[int, int]]) -> bool:
        '''Recursive function that searches for the next character of a word adjacent to coordinates `curr`
        '''
        if len(word) == 0:
            return True
        
        r: int = curr[0]
        c: int = curr[1]
        toCheck: List[Tuple[int, int]] = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        
        for coord in toCheck:
            if self.isValid(board, coord) and coord not in visited:
                if board[coord[0]][coord[1]] == word[0]:
                    newVisited = deepcopy(visited)
                    newVisited.add(coord)
                    if self.search(board, word[1:], coord, newVisited):
                        return True

        return False


    def isValid(self, board: List[List[str]], coord: Tuple[int, int]) -> bool:
        return not (coord[0] < 0 or coord[0] == len(board) or coord[1] < 0 or coord[1] == len(board[0]))


def main():
    s: Solution = Solution()

    print(s.exist(
        [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ], 'ABCCED'
    )) # Expected: True

    print(s.exist(
        [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ], 'SEE'
    )) # Expected: True

    print(s.exist(
        [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
        ], 'ABCB'
    )) # Expected: False

    print(s.exist(
        [
            ['A','B','C','E'],
            ['S','F','E','S'],
            ['A','D','E','E']
        ], 'ABCESEEEFS'
    )) # Expected: True


if __name__ == '__main__':
    main()
