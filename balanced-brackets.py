# https://www.hackerrank.com/challenges/balanced-brackets/problem
# same as https://leetcode.com/problems/valid-parentheses/description/
# Use Stack
# Time: O(n), Space: O(n)

#!/bin/python3

import math
import os
import random
import re
import sys
import collections

# Complete the isBalanced function below.
def isBalanced(s):
    stack = collections.deque()
    for c in s:
        if c in ['{','[','(']: stack.append(c)
        elif c in ['}',']',')']:
            if stack:
                c2 = stack[-1]
                if (c=='}' and c2=='{') or (c==']' and c2=='[') or (c==')' and c2=='('):
                    stack.pop()
                else: return 'NO'
            else: return 'NO'
    return 'YES' if not stack else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input())
    for t_itr in range(t):
        s = input()
        result = isBalanced(s)
        fptr.write(result + '\n')
    fptr.close()
