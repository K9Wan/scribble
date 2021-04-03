class Node(object):

    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data

class BinarySearchTree(object):
    keyfunc = None  # Will it be worse when using lambda x: x as default?
    
    def __init__(self, node=None):
        self.root = node
        self.left = None
        self.right = None
        # I don't want default to be NoneType, but don't know how for now.

    def add(self, key, data=None):
        node = Node(key, data)
        if self.root is None:
            self.root = node
            return
        parent = self.root.key
        if self.keyfunc is None:
            if key < parent:
                if self.left is None:
                    self.left = __class__(node)
                else:
                    self.left.add(key, data)
                        
            elif key > parent:
                if self.right is None:
                    self.right = __class__(node)
                else:
                    self.right.add(key, data)
        else:
            if keyfunc(key) < keyfunc(parent):
                if self.left is None:
                    self.left = __class__(node)
                else:
                    self.left.add(key, data)
            elif keyfunc(key) > keyfunc(parent):
                if self.right is None:
                    self.right = __class__(node)
                else:
                    self.right.add(key, data)
    def inorder(self):
        if self.root:
            if self.left:
                self.left.inorder()
            print(self.root.key, end=' ')
            if self.right:
                self.right.inorder()

if __name__ == '__main__':
    bst1 = BinarySearchTree()
    arr = [2,6,4,3,2,7,8,1,9,5]
    for key in arr:
        bst1.add(key)
    bst1.inorder()
