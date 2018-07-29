# https://www.hackerrank.com/challenges/cut-the-sticks/problem
# 1. get minVal
# 2. if minVal, flag false
#    otherwise, -= minVal
# Time: O(n^2), Space: O(n)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    length = len(arr)
    used = [True]*length
    
    curLen = length
    ans = []
    while curLen>0:
        ans.append(curLen)
        minVal = sys.maxsize
        for i in range(length):
            if used[i] and minVal>arr[i]: minVal = arr[i]
        #print('min',minVal)
        for i in range(length):
            if used[i]:
                if arr[i]==minVal:
                    used[i] = False
                    curLen -= 1
                else:
                    arr[i] -= minVal
        #print('cur',curLen)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = cutTheSticks(arr)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
