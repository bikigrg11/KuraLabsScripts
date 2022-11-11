class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = None


def deleteNode(head,n):

    counter = 0
    while head.next != None:
        counter += 1

        if counter+1 == n:
            head.value = head.next.value
            head.next = head.next.next
            head.next.next = None
            return head
        head = head.next

    return head


deleteNode(a,3)

head = a
while head.next != None:
        print(head.value)
        head = head.next
