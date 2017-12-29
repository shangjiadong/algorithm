class BinaryTree():
    def __int__(self, rootid):
        self.root = rootid
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newnode):
        if isinstance (newnode, BinaryTree):
            t = newnode
        else:
            t = BinaryTree(newnode)
        if self.leftChild is not None:
            t.leftChild == self.leftChild
        
        self.leftChild = t

    def insertRight(self, newnode):
        if isinstance (newnode, BinaryTree):
            t = newnode
        else:
            t = BinaryTree(newnode)
        if self.rightChild is not None:
            t.rightChild == self.rightChild
        
        self.rightChild = t

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def setRootVal(self, rootVal):
        self.root = rootVal

    def getRootVal(self):
        return self.root

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.root)
        if self.rightChild:
            self.rightChild.inorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.root)

    def preorder(self):
        print(self.root)
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

def buildTree():
    r = BinaryTree('a')		
    r.insertLeft('b')
    r.insertRight('c')
    r.getLeftChild().insertRight('d')
    r.getRightChild().insertLeft('e')
    r.getRightChild().insertRight('f')
    return r
ttree = buildTree()
testEqual(ttree.getRightChild().getRootVal(),'c')
testEqual(ttree.getLeftChild().getRightChild().getRootVal(),'d')
testEqual(ttree.getRightChild().getLeftChild().getRootVal(),'e')

