'''
    Binary Search will look for the item in the ordered list

    input = [1,2,4,6,7,9,11]
    return output = True

    search_element(input = [1,2,4,6,7,9,11] , num = 7):
        
        middle = len(input) // 2  

        if middle == 0:
            return False

        if input[middle] == num:
            return True
        else: 
            if num > middle 
                 input = input[:middle]
            else
                input = input[middle:]
            return search_element(input,num)


'''

def serach_element_traversal(input,num):

    first = 0
    last = len(input)-1

    while first <= last:

        middle = (first+last) // 2

        if input[middle] == num:
            return True
        
        if input[middle] > num:
            last = middle - 1
        else:
            first = middle + 1

    return False

# this method will 
def search_element_recursion(input, num):

    if len(input) == 0:
        return False

    middle = len(input) // 2  

    if input[middle] == num:
        return True
    if num < input[middle] :
        input = input[:middle]
    else:
        input = input[middle+1:]
    return search_element_recursion(input,num)

testArray = [1,2,4,6,7,9]

print(search_element_recursion(testArray,16))

print(serach_element_traversal(testArray,6))

