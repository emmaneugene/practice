#!/bin/python3

import math
import os
import random
import re
import sys

# You are given a playlist of songs with durations in seconds. Return all the song pairs 
# which add up to a multiple of 60 (a minute)
# 
# Complete the 'playlist' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY songs as parameter.
#

def playlist(songs) -> int:
    songs = list(map(lambda x: x % 60, songs))
    
    num_pairs: int = 0
    
    for i in range(len(songs)):
        for j in range(i+1, len(songs)):
            if (songs[i] + songs[j]) % 60 == 0:
                num_pairs += 1

    return num_pairs
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    songs_count = int(input().strip())

    songs = []

    for _ in range(songs_count):
        songs_item = int(input().strip())
        songs.append(songs_item)

    result = playlist(songs)

    fptr.write(str(result) + '\n')

    fptr.close()
