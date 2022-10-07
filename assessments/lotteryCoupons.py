#!/bin/python3

import math
import os
import random
import re
import sys


# You are given lottery tickets numbered from 1 ... n.
# We take the sum of digits of each lottery ticket (e.g. "12" -> 3, "3" -> 3) as the actual prize number
# Find the count of prize numbers for which there are the most number of winning tickets
#
# Complete the 'lotteryCoupons' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#
def compute_digit_sum(i: int) -> int:
    total: int = 0
    while i > 0:
        total += i % 10
        i //= 10
    
    return total

def lotteryCoupons(n: int) -> int:
    sum_of_digits = [compute_digit_sum(i) for i in range(1, n+1)]
    # alternatively, use map()
    # sum_of_digits = list(map(compute_digit_sum, sum_of_digits))
    coupon_counts = {}
    
    for i in sum_of_digits:
        if i in coupon_counts:
            coupon_counts[i] += 1
        else:
            coupon_counts[i] = 1

    highest_count: int = 0
    num_values_of_s: int = 0
    
    for coupon, count in coupon_counts.items():
        if count > highest_count:
            highest_count = count
            num_values_of_s = 1
        elif count == highest_count:
            num_values_of_s += 1
    
    return num_values_of_s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = lotteryCoupons(n)

    fptr.write(str(result) + '\n')

    fptr.close()
