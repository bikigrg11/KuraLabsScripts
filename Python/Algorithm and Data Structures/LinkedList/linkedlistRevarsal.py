from email import header


class Node(object):
    def __init__(self,value):
        self.value = value
        self.nextNode = None


a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c
c.nextNode = None

def reverse(head):
    current = head
    prevNode = None
    nextNode = None

    while current:
        nextNode = current.nextNode
        current.nextNode = prevNode
        prevNode = current
        current = nextNode
        
reverse(a)