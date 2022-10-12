
def addTwoNumbers(l1,l2):

    i = 0
    sum1 = 0
    while l1.next != None:
        sum1 = l1.val + pow(10,i)
        i+=1
        l1 = l1.next

    i = 0
    sum2 = 0
    while l2.next != None:
        sum1 = l2.val + pow(10,i)
        i+=1
        l2 = l2.next

    return (sum1+sum2)





l1 = [2,4,3]
l2 = [5,6,4]

print(addTwoNumbers(l1,l2))

