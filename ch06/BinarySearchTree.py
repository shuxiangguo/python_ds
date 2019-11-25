# 二叉搜索树
from ch06.TreeNode import TreeNode


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self._put(key, val, self.root)

        else:
            self.root = TreeNode(key, val)
        self.size = self.size + 1

    def _put(self, key, val, currentNode):
        if key < currentNode.key: # key值比当前节点小，则递归往左子树插入
            if currentNode.hasLeftChild(): # 当前节点存在左子树
                self._put(key, val, currentNode.leftChild)
            else: # 当前节点不存在左子树，则将该节点作为左节点
                currentNode.leftChild = TreeNode(key, val, parent=currentNode)
        else: # key值比当前节点值高，则递归往右子树插入
            if currentNode.hasRightChild(): # 当前节点存在右子树
                self._put(key, val, currentNode.rightChild)
            else: # 当前节点不存在子树
                currentNode.rightChild = TreeNode(key, val, parent=currentNode)

    # 重载运算符[]设置值
    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root:
            res = self._get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):
        if not currentNode:
            return None
        elif currentNode.key == key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.leftChild)
        else:
            return self._get(key, currentNode.rightChild)

    # 可以通过[]获取值
    def __getitem__(self, key):
        return self.get(key)

    # 重载in运算符
    def __contains__(self, key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self._get(key, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError('Error, key not in Tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):
        self.delete(key)

    # # 删除一个节点，复杂
    # def remove(self, currentNode):
    #     if currentNode.isLeaf():
    #         if currentNode == currentNode.parent.leftChild:
    #             currentNode.parent.leftChild = None
    #         else:
    #             currentNode.parent.rightChild = None
    #     elif currentNode.hasBothChildren():