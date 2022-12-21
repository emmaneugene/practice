import math
import os
import random
import re
import sys

# Consider 2 integer arrays `a` and `b`, each of size `n`
# In one operation, we can swap integers corresponding to the indices of each array
# This operation can be performed at most `k` times
# Find the maximum number of distinct elements that can be achieved in array `a`
# after at most `k` operations

# Example:
# n = 5
# a = [2,3,3,2,2]
# b = [1,3,2,4,1]
# k = 2

# To get the maximum number of distinct elements in array a, we can swap:
# - a[2] and b[0]
# - a[4] and b[3]
# to end up with [2,3,1,2,4] with 4 distinct elements (this is not the only solution) 

# Complete the 'getMaximumDistinctCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#  3. INTEGER k
#

def get_distinct_values_and_duplicates(arr: list[int]) -> tuple[list[int], int]: 
    '''Returns a list of unique values and duplicates in a sorted list
    '''
    unique_vals: list[int] = []
    dupl: int = 0
    
    if len(arr) == 0:
        return unique_vals, dupl
    
    curr: int = arr[0]
    unique_vals.append(curr)
    
    for i in range(1, len(arr)):
        if arr[i] != curr:
            curr = arr[i]
            unique_vals.append(curr)
        else:
            dupl += 1
    
    return unique_vals, dupl

def get_unique_count(src: list[int], dst: list[int]) -> int:
    '''Given sorted lists src and dst, return number of elements in src not present in dst
    '''

    if len(src) == 0 or len(dst) == 0:
        return len(src)
    
    # TODO: Make this code more efficient. Since the lists are sorted, it should
    # be possible to run in O(n) time instead of O(n^2)
    # src_idx: int = 0
    # dst_idx: int = 0

    count: int = 0
    for i in src:
        if i not in dst:
            count += 1

def getMaximumDistinctCount(a: list[int], b: list[int], k: int) -> int:
    # Sort for efficiency: O(n*log(n))
    a.sort()
    b.sort()
    a_unique, a_dupl = get_distinct_values_and_duplicates(a)
    b_unique, b_dupl = get_distinct_values_and_duplicates(b)

    
    # Find out how many unique elements can be swapped in from b
    b_swappable_count: int = get_unique_count(b_unique, a_unique)
    
    # Number of elements we can swap into a to increase the number of distinct elements
    swappable = min(a_dupl, k, b_swappable_count)

    return len(a_unique) + swappable
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = int(input().strip())
        b.append(b_item)

    k = int(input().strip())

    result = getMaximumDistinctCount(a, b, k)

    fptr.write(str(result) + '\n')

    fptr.close()
