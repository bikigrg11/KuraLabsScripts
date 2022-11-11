class BinaryTree(object):

    def __init__(self,keyValue):
        self.root = keyValue
        self.leftNode = None
        self.rightNode = None
    

    def setLeftNode(self,newNode):

        if self.leftNode == None:
            self.leftNode = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftNode = self.leftNode
            self.leftNode = t
    
    def setRightNode(self,newNode):

        if self.rightNode == None:
            self.rightNode = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightNode = self.rightNode
            self.rightNode = t

    def getLeftNode(self):
        return self.leftNode
    
    def getRightNode(self):
        return self.rightNode
    
    def setRootVal(self,newNode):
        self.root = newNode
    
    def getRootVal(self):
        return self.root
    

t1 = BinaryTree('a')
print(t1.getRootVal())

t1.setLeftNode('left1')
t1.setRightNode('right1')

print(t1.getLeftNode())
print(t1.getRightNode())
t1.setLeftNode('left2')
print(t1.getLeftNode().getLeftNode())

