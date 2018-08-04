# https://www.hackerrank.com/challenges/s10-weighted-mean/problem
n = int(input())
nums = list(map(int, input().split(' ')))
weights = list(map(int, input().split(' ')))
sum, sumW = 0, 0
for i in range(n):
    sum += nums[i]*weights[i]
    sumW += weights[i]
print(format(sum/sumW,'.1f'))
