class Queue(object):
    def __init__(self):
        self.item = []

    def isEmpty(self):
        return self.item == []

    def enqueue(self,num):
        self.item.insert(0,num)
    
    def dequeue(self):
        return self.item.pop()
    
    def peek(self):
        return self.item[0]
    
    def size(self):
        return len(self.item)

