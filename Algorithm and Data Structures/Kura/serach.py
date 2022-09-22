num = [1,4,9,3,2,6,5,8,7]
num.sort()


def search(numArray,low,high,x):
    if high >= low:
        mid = (low + high) // 2

        if numArray[mid] == x:
            return x

        elif x < numArray[mid]:
           return search(numArray,low,mid-1,x)
        else:
           return search(numArray,mid+1,high,x)

    else:
        print("Number not found")
        return -1

searchNum = 20

result  = search(num,0,len(num)-1,searchNum)

print(result)

