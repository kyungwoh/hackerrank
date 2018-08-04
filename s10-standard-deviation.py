# https://www.hackerrank.com/challenges/s10-standard-deviation/problem
import math
n = int(input())
nums = list(map(int, input().split(' ')))
mean = sum(nums)/n
var = sum([(x - mean)**2 for x in nums])/n
stddev = math.sqrt(var)
print(format(stddev,'.1f'))
