# https://www.hackerrank.com/challenges/electronics-shop/problem
# Brute Force
# Time: O(nm), Space: O(1)

#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    keyboards.sort()
    drives.sort()
    ans = -1
    for k in keyboards:
        for d in drives:
            sum = k+d
            if sum<=b:
                if abs(b-sum)<abs(b-ans): ans = sum
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    bnm = input().split()
    b = int(bnm[0])
    n = int(bnm[1])
    m = int(bnm[2])
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #
    moneySpent = getMoneySpent(keyboards, drives, b)
    fptr.write(str(moneySpent) + '\n')
    fptr.close()
