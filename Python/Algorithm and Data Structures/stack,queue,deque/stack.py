
class Stack(object):
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def push(self,num):
        self.item.append(num)
    
    def pop(self):
        return self.item.pop()
    
    def peek(self):
        return self.item[len(self.item)-1]
    
    def size(self):
        return len(self.item)


stack = Stack()

stack.push(5)
stack.push(4)
print(stack.peek())
stack.pop()
print(stack.peek())
stack.pop()
print(stack.isEmpty())

print(stack.size())