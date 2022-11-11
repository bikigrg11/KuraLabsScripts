from unicodedata import decimal


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getDecimalValue(head):
    
    lenNodes = 1
    temp = head

    while temp.next != None:
        lenNodes +=1
        temp = temp.next

    decimalVal = 0

    while head.next != None:
        if(head.val == 1):
            decimalVal += pow(2,(lenNodes-1))
        lenNodes -=1
        head = head.next
    
    if head.val == 1:
        decimalVal += 1
    
    print(lenNodes)
    print(decimalVal)


a = ListNode(1)
b = ListNode(0)
c = ListNode(1)
d = ListNode(1)
e = ListNode(0)

a.next = b
b.next = c
c.next = d
d.next = e

getDecimalValue(a)