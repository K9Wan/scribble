class Node(object):
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data


class BinarySearchTree(object):
    def __init__(self, node=None, keyfunc=lambda x: x):
        self.root = node
        self.keyfunc = keyfunc
        if node is not None:
            self.left = __class__(keyfunc=self.keyfunc)
            self.right = __class__(keyfunc=self.keyfunc)

    def add(self, key, data=None):
        node = Node(key, data)
        if self.root is None:
            self.root = node
            self.left = __class__(keyfunc=self.keyfunc)
            self.right = __class__(keyfunc=self.keyfunc)
            return
        parent = self.root.key
        if self.keyfunc(key) < self.keyfunc(parent):
            self.left.add(key, data)
        elif self.keyfunc(key) > self.keyfunc(parent):
            self.right.add(key, data)

    def inorder(self):
        if self.root:
            self.left.inorder()
            print(self.root.key, end=" ")
            self.right.inorder()


if __name__ == "__main__":
    bst1 = BinarySearchTree()
    arr = [2, 6, 4, 3, 2, 7, 8, 1, 9, 5]
    for key in arr:
        bst1.add(key)
    bst1.inorder()
