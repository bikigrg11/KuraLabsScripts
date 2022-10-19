
def merge_sort(arr):

    if len(arr) > 1:

        mid = len(arr) //2 
        leftHalf = arr[:mid]
        rightHalf = arr[mid:]

        merge_sort(leftHalf)
        merge_sort(rightHalf)

        i=0
        j=0
        k=0

        while i < len(leftHalf) and j < len(rightHalf):

            if leftHalf[i] < rightHalf[j]:
                arr[k] = leftHalf[i]

                i +=1 
            else:
                arr[k] = rightHalf[j]
                j += 1

            k += 1

        while i < len(leftHalf):
            arr[k] = leftHalf[i]
            i +=1
            k +=1
        while j < len(rightHalf):
            arr[k] = rightHalf[j]
            j += 1
            k += 1
    
    return

arr = [1,4,6,2,3,9,7,8]

merge_sort(arr)
print(arr)