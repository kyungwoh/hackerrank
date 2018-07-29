# https://www.hackerrank.com/challenges/non-divisible-subset/problem
# 1. count mods
# 2. sum possible cases
# Time: O(n), Space: O(k)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    mods = [0]*k
    for i in S: mods[i%k] += 1
    
    cnt = min(mods[0], 1)
    for i in range(1, k//2+1):
        if i==(k-i): cnt += min(mods[i], 1)
        else: cnt += max(mods[i], mods[k-i])
    return cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    S = list(map(int, input().rstrip().split()))
    result = nonDivisibleSubset(k, S)
    fptr.write(str(result) + '\n')
    fptr.close()
