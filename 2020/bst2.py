from collections import deque

class Node(object):
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data

    def noname1(self):
        '''
        can't find appropriate name:
        get derive gain take generate yield obtain take return ...
        retrieve release discharge bring fetch pick invoke pull ...
        extract enumerate collect attain inspect view look obtain ...
        value data pair content element ...
        adaptable flexible custom casual normal relaxed informal ...
        '''
        if self.data is None:
            return self.key
        return (self.key, self.data)

    def _noname2(self):
        yield self.key
        if self.data is not None:
            yield self.data

    def noname2(self):
        return tuple(self._noname2())

    

class BinarySearchTree(object):
    def __init__(self, keyfunc=lambda x: x, *, node=None):
        self.root = node
        self.keyfunc = keyfunc
        if node is not None:
            self.left = self.new_empty()
            self.right = self.new_empty()

    def _kf(self, key):
        try:
            dummy = self.keyfunc(key) > self.keyfunc(key)
            dummy = self.keyfunc(key) < self.keyfunc(key)
            return self.keyfunc(key)
        except Exception as e:
            raise KeyError(key) from e

    def _lt(self, key, target):
        try:
            return self.keyfunc(key) < self.keyfunc(target)
        except Exception as e:
            raise KeyError(key) from e

    def __bool__(self):
        return self.root is not None

    def new_empty(self):
        return __class__(keyfunc=self.keyfunc)

    def add(self, key, data=None):
        node = Node(key, data)
        if not self:
            self.root = node
            self.left = self.new_empty()
            self.right = self.new_empty()
            return
        parent = self.root.key
        if self.keyfunc(key) < self.keyfunc(parent):
            self.left.add(key, data)
        elif self.keyfunc(key) > self.keyfunc(parent):
            self.right.add(key, data)
        '''
        else: pass will ignore duplicates,
        else: self.right.add(...) will accept duplicates.
        (sure can replace elif above with else, or replace > with >=)
        or can consider it as wrong
        '''

    def find(self, key):
        if not self:
            return None
        current = self.root.key
        if current == key:
            return self.noname_root()
        elif self._lt(key, current):
            return self.left.find(key)
        elif self._kf(key) > self._kf(current):
            return self.right.find(key)

    def __contains__(self, key):
        return self.find(key) is not None

    def print_inorder(self):
        if self:
            self.left.print_inorder()
            print(self.root.key, end=" ")
            self.right.print_inorder()

    def inorder(self):
        if self:
            yield from self.left.inorder()
            yield self.noname_root()
            yield from self.right.inorder()

    def preorder(self):
        if self:
            yield self.noname_root()
            yield from self.left.preorder()
            yield from self.right.preorder()


    def postorder(self):
        if self:
            yield from self.left.postorder()
            yield from self.right.postorder()
            yield self.noname_root()

    def bfs(self):
        q = deque()
        q.append(self)
        while q:
            cur = q.popleft()
            if cur:
                yield cur.noname_root()
                q.append(cur.left)
                q.append(cur.right)

    def noname_root(self):
        return self.root.noname1()

    def add_from(self, iterable):
        if hasattr(iterable, 'items'):
            for key, data in iterable.items():
                self.add(key, data)
        else:
            for item in iterable:
                self.add(item)
        
    


if __name__ == "__main__":
    bst1 = BinarySearchTree(lambda x: -x)
    arr = [2, 6, 4, 3, 2, 7, 8, 1, 9, 5]
    bst1.add_from(arr)
    bst1.print_inorder()
    print([*bst1.inorder()])
