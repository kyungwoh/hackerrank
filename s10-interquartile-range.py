# https://www.hackerrank.com/challenges/s10-interquartile-range/problem
def getMedian(nums):
    nLen = len(nums)
    #print(nLen, nums)
    if nLen%2==1: return nums[nLen//2]
    else: return (nums[nLen//2-1] + nums[nLen//2])/2

n = int(input())
nums = list(map(int, input().split(' ')))
freqs = list(map(int, input().split(' ')))
nums2 = []
for i in range(n):
    for j in range(freqs[i]):
        nums2.append(nums[i])
nums2.sort()
nLen = len(nums2)
#print(nLen, nums2)
q1 = getMedian(nums2[0:nLen//2])
q3 = getMedian(nums2[nLen//2+1:]) if nLen%2==1 else getMedian(nums2[nLen//2:])
    
print(format(q3-q1,'.1f'))
