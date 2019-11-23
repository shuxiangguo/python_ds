# 构建中序表达式的解析树
from ch06.BinaryTree import BinaryTree


def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = []
    eTree = BinaryTree('')
    pStack.append(eTree)
    currentTree = eTree
    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.append(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-*/)':
            currentTree.setRootVal(eval(i))
            currentTree = pStack.pop()
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.append(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            if not pStack.pop():
                return currentTree
            else:
                currentTree = pStack.pop()
        else:
            raise ValueError("Unknown Operator: " + i)


tree = buildParseTree('(3+(4*5))')