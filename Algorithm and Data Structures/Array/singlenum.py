import collections

def singleNumber(nums):
    num = collections.defaultdict(int)

    for n in nums:
        if num[n] == 0:
            num[n] = 1
        else:
            num[n] = 0

    for n in num:
        if num[n] == 1:
            return n
    
    return 0

nums = [4,1,2,1,2]
print(singleNumber(nums))