from tkinter import E


class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextNode = None



a = Node(3)
b = Node(4)
c = Node(5)
d = Node(6)
e = Node(7)


a.nextNode = b
b.nextNode = c
c.nextNode = d
d.nextNode = e


def printNthlist(val,head):
    check = 1
    while check != val:
        head = head.nextNode
        check+=1
    
    return head.value

print(printNthlist(2,a))

