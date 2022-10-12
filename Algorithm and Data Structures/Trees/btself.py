class BinaryTree(object):

    def __init__(self,root):
        self.keyVal = root
        self.rightNode = None
        self.leftNode = None
    

    def insertLeft(self,newNode):

        if self.leftNode == None:
            self.leftNode = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftNode = self.leftNode
            self.leftNode = t
    
    def insertRight(self,newNode):

        if self.rightNode == None:
            self.rightNode = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightNode = self.rightNode
            self.rightNode = t
    
    def insertRoot(self,obj):
        self.keyVal = obj
        