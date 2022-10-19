from gettext import find


class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    

def find_sum(root):

    if root == None:
        return 0
    
    return root.data + find_sum(root.left) + find_sum(root.right)


a = Node(1)
b = Node(2)
c = Node(3)
a.left = b
a.right = c
d = Node(4)
b.left = d
e = Node(5)
d.left = e

print(find_sum(a))

