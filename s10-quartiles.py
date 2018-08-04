# https://www.hackerrank.com/challenges/s10-quartiles/problem
def getMedian(nums):
    nLen = len(nums)
    #print(nLen, nums)
    if nLen%2==1: return nums[nLen//2]
    else: return (nums[nLen//2-1] + nums[nLen//2])//2

n = int(input())
nums = list(map(int, input().split(' ')))
nums.sort()


q2 = getMedian(nums)
if n%2==1:
    q1 = getMedian(nums[0:n//2])
    q3 = getMedian(nums[n//2+1:])
else:
    q1 = getMedian(nums[0:n//2])
    q3 = getMedian(nums[n//2:])

print(q1)
print(q2)
print(q3)
