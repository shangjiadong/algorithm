"""
This function use tree to store the hierarchical structure, math euqation here.
Output it as a tree form, and also use a evaluation function to determine the 
value of the expression.
"""
from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree

def buildParseTree(equation):
    """
    input: a exquation expression, with parenthesis regulated
    output: a tree with postorder traversal
    """
    equationList = equation.split()
    pStack = Stack()
    eTree = BinaryTree('')
    currentTree = eTree
    pStack.push(eTree)
    for i in equationList:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in ['+', '-', '*', '/', ')']:
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise valueError
    return eTree

def evaluate(parseTree):
    """
    input: a parse tree with math equation coded
    output: the value of the equation
    """
    import operator
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

equation = buildParseTree(" ( ( ( 10 + 5 ) * 3 ) + 5 )")
equation.postorder()
print evaluate(equation)