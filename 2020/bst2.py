class Node(object):
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data


class BinarySearchTree(object):
    keyfunc = lambda x: x  # Will it be worse when using lambda x: x as default?

    def __init__(self, node=None):
        self.root = node
        if node is not None:
            self.left = __class__()
            self.right = __class__()
        # I don't want default to be NoneType, but don't know how for now.

    def add(self, key, data=None):
        node = Node(key, data)
        if self.root is None:
            self.root = node
            self.left = __class__()
            self.right = __class__()
            return
        parent = self.root.key
        if __class__.keyfunc(key) < __class__.keyfunc(parent):
            self.left.add(key, data)
        elif __class__.keyfunc(key) > __class__.keyfunc(parent):
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
