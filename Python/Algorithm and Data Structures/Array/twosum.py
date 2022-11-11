'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''

import collections

def twoSum(nums,target):

    arr = collections.defaultdict(int)

    index = 0
    for index, num in enumerate(nums):
        arr[num] = index


    print(arr)
    output = []
    counter = 0
    temp = []
    for i,num in enumerate(nums):
        val = target - num
        
        if target == 2 * num:
            temp += [i]
            counter +=1

        if arr.get(val) != None and arr.get(val) != arr.get(num):
            output = [arr[num],arr[val]]
            return output
        else:
            if counter == 2:
                return temp
    return 0

nums = [3,3]
target = 6

print(twoSum(nums,target))