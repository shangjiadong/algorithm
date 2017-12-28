class BinaryTree():
	def __int__(self, rootid):
		self.root = rootid
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newnode):
		if self.leftChild == None:
			self.leftChild = BinaryTree(self, newnode)
		else:
			t = BinaryTree(newnode)
			t.leftChild = self.leftChild
			self.leftChild = t

	def insertRight(self, newnode):
		if self.rightChild == None:
			self.rightChild = BinaryTree(newnode)
		else:
			t = BinaryTree(newnode)
			t.rightChild = self.rightChild
			self.rightChild = t

	def getLeftChild(self):
		return self.leftChild

	def getRightChild(self):
		return self.rightChild

	def setRootValue(self, rootVal):
		self.root = rootVal

	def getRootValue(self):
		return self.root

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

