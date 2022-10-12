import collections;

def intersect(nums1,nums2):
    nums = collections.defaultdict(int)
    output = []
    lenNums1 = len(nums1)
    lenNums2 = len(nums2)
    
    for listNum in nums1:
        if nums[listNum] == None:
            nums[listNum] = 1
        else:
            nums[listNum] += 1
    
    for listNum in nums2:
        if nums[listNum] >= 1:
            output.append(listNum)
            nums[listNum] -= 1
            
    return output

print(intersect([1,2,2,1],[2,2]))