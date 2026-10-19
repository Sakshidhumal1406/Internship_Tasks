# Question 19: Weighted Uniform Strings
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/weighted-uniform-string/problem


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'weightedUniformStrings' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER_ARRAY queries
#

def weightedUniformStrings(s, queries):
    # Write your code here
    weights = set()
    current_weight = 0
    previous = ""

    for char in s:
        weight = ord(char) - ord('a') + 1

        if char == previous:
            current_weight += weight
        else:
            current_weight = weight
            previous = char

        weights.add(current_weight)

    return ["Yes" if q in weights else "No" for q in queries]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = weightedUniformStrings(s, queries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
