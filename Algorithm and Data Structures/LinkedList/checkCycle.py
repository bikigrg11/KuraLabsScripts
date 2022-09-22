from operator import truediv


class Node(object):

    def __init__(self,value):
        self.value = value
        self.nextNode = None

a = Node(1)
b = Node(2)
c = Node(3)

a.nextNode = b
b.nextNode = c
c.nextNode = a

def cycle_check(node):

    marker1 = node
    marker2 = node

    while marker2 !=None and marker2.nextNode != None:
        print("Marker 1",marker1.value)
        marker1 = marker1.nextNode
        print("Marker 1",marker1.value)
        print("Marker 2",marker2.value)
        marker2 = marker2.nextNode.nextNode
        print("Marker 2",marker2.value)

        if marker1 == marker2:
            return True
    
    return False

print(cycle_check(a))