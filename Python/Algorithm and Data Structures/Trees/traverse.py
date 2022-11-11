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
    

t1 = BinaryTree(25)
t1.setLeftNode(4)
t1.setRightNode(12)
t1.setLeftNode(10)


def preOrder(tree):
    if tree != None:
        print(tree.getRootVal())
        preOrder(tree.getLeftNode())
        preOrder(tree.getRightNode())

preOrder(t1)

def inOrder(tree):
    if tree != None:
        inOrder(tree.getLeftNode())
        print(tree.getRootVal())
        inOrder(tree.getRightNode())

inOrder(t1)

def postOrder(tree):
    if tree != None:
        postOrder(tree.getLeftNode())
        postOrder(tree.getRightNode())
        print(tree.getRootVal())

postOrder(t1)



