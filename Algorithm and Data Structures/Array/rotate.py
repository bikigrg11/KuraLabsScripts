


def rotate(nums,k):
    
    arr = []
    i = 0
    while i < k :
        n = nums.pop()
        arr.insert(0,n)
        i +=1
    
    arr += nums
    return arr
  

nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums,k))