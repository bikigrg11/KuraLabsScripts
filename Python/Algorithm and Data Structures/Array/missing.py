'''
Find the missing num from the array
'''
import collections

def missingNum(array1, array2):

    if len(array1) == len(array2):
        print("array is same")
        return -1

    if len(array1) < len(array2):
        arr1 = array1
        arr2 = array2
    else:
        arr1 = array2
        arr2 = array1


    check = collections.defaultdict(int) 


    for num in arr1:
        check[num] += 1
    
    for num in arr2:
        if check[num] == 0:
            print(num, "is the missing num")
            return num


    # for num in arr1:
    #     if num not in arr2:
    #         print(num," is the missing Num")
    #         return num

    

arr1 = [1,2,4,3,5]
arr2 = [1,2,4,5]
missingNum(arr1,arr2)