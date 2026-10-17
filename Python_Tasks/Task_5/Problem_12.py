# Question 12: Capitalize!
# Platform: HackerRank
# Link: https://www.hackerrank.com/challenges/capitalize/problem

#!/bin/python3

import math
import os
import random
import re
import sys

def solve(s):
    return s.title()


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)