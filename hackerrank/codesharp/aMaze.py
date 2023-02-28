# https://www.hackerrank.com/contests/code-23-2/challenges/amaze

import math
import os
import random
import re
import sys

from typing import List, Dict

#
# Complete the 'solve_maze' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts 2D_STRING_ARRAY maze as parameter.
#
class Coords():
    def __init__(self, y: int, x: int) -> None:
        self.y = y
        self.x = x

    def up(self):
       return Coords(self.y+1, self.x)

    def down(self):
       return Coords(self.y-1, self.x)

    def left(self):
       return Coords(self.y, self.x-1)

    def right(self):
       return Coords(self.y, self.x+1)


def solve_maze(maze: List[List[str]]) -> List[str]:
    moves: List[str] = []
    nRows: int = len(maze)
    nCols: int = len(maze[0])

    start: Coords = Coords(-1,-1)
    end: Coords = Coords(-1,-1)

    # Find start and end
    for i in range(nRows):
        for j in range(nCols):
            if maze[i][j] == 'S':
                start.y = i
                start.x = j
            
            if maze[i][j] == 'E':
                end.y = i
                end.x = j
            
    

    return moves

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    height = int(first_multiple_input[0])

    width = int(first_multiple_input[1])

    maze = []

    for _ in range(height):
        maze.append(input().rstrip().split())

    directions = solve_maze(maze)

    fptr.write(' '.join(directions))
    fptr.write('\n')

    fptr.close()
