class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def deleteNode(self,node):

    while self.next != None:
        if self.val == node:
            self = self.next
            return
        else:
            self = self.next

    return

a = ListNode(4)
b = ListNode(5)
c = ListNode(1)
d = ListNode(9)

a.next = b
b.next = c
c.next = d


