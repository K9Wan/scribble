from collections import deque
import pprint

''' help from
https://stackoverflow.com/questions/67285277/recursive-class-definition-in-python
https://stackoverflow.com/a/54074933
'''
class Node(object):
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data

    def __repr__(self):
        return f'node({self.key})'

    def noname1(self):
        '''
        can't find appropriate name:
        get derive gain take generate yield obtain take return ...
        retrieve release discharge bring fetch pick invoke pull ...
        extract enumerate collect attain inspect view look obtain ...
        value data pair content element ...
        custom casual normal informal ...
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

def is_iter(obj):
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return True

class BinarySearchTree(object):
    def __init__(self, keyfunc=lambda x: x, *,
                 node=None, left=None, right=None):
        self.root = node
        self.keyfunc = keyfunc
        if node is not None:
            self.left = self.new_empty() if left is None else left
            self.right = self.new_empty() if right is None else right

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
        #'''
        if self.keyfunc(key) < self.keyfunc(parent):
            self.left.add(key, data)
        elif self.keyfunc(key) > self.keyfunc(parent):
            self.right.add(key, data)
        #'''
        '''
        if self._lt(key, parent):
            self.left.add(key, data)
        else:
            self.right.add(key, data)
        #'''
        '''
        else: pass will ignore duplicates,
        else: self.right.add(...) will accept duplicates.
        (sure can replace elif above with else, or replace > with >=)
        or can consider it as wrong
        '''

    def added(self, key, data=None):
        node = Node(key, data)
        if not self:
            return self.f_bst((None, node, None))
        parent = self.root.key
        left, node, right = self
        if self.keyfunc(key) < self.keyfunc(parent):
            left = left.added(key, data)
            return self.f_bst((left, node, right))
        elif self.keyfunc(key) > self.keyfunc(parent):
            right = right.added(key, data)
            return self.f_bst((left, node, right))
        else:
            return self
        

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

    def delete(self, key):
        if not self:
            return self
        cur = self.root.key
        if self._kf(key) == self._kf(cur):
            if self.left and self.right:
                succ = self.right
                while succ.left:
                    succ = succ.left
                self = self.delete(succ.root.key)
                self.root = succ.root
                '''
                above two lines must not exchange order
                self.root = succ.root
                self = self.delete(succ.root.key)
                will lead to bad recursion
                because node to be deleted is duplicated,
                and the duplicated one has both left and right child.
                '''
                return self
            elif not self.left:
                return self.right
            else:
                return self.left
        elif self._kf(key) < self._kf(cur):
            self.left = self.left.delete(key)
            return self
        else:
            self.right = self.right.delete(key)
            return self

    def deleted(self, key):
        if not self:
            return self
        cur = self.root.key
        if self._kf(key) == self._kf(cur):
            if self.left and self.right:
                succ= self.right
                while succ.left:
                    succ = succ.left
                print(succ)
                dltd = self.deleted(succ.root.key)
                left, node, right = dltd
                node = succ.root
                return self.f_bst((left, node, right))
            elif not self.left:
                return self.f_bst(self.right) if self.right else self.new_empty()
            else:
                return self.f_bst(self.left) if self.left else self.new_empty()
        elif self._kf(key) < self._kf(cur):
            left, node, right = self
            left = left.deleted(key)
            return self.f_bst((left, node, right))
        else:
            left, node, right = self
            right = right.deleted(key)
            return self.f_bst((left, node, right))
        

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
        
    def i(self):
        if self:
            if self.left and self.right:
                return (self.left.i(), self.root.key, self.right.i())
            elif self.left and not self.right:
                return (self.left.i(), self.root.key)
            elif self.right and not self.left:
                return (self.root.key, self.right.i())
            else:
                return (self.root.key,)

    def level(self):
        def _level(self):
            if self:
                lev = max(_level(self.left), _level(self.right)) +1
                return lev
            else:
                return 0

        return _level(self)

    def pp(self, idt=0):
        if not self.level():
            return print(None)
        if idt <= 0:
            idt = 60 // self.level()
        return pprint.pprint(self.i(), width=1, indent=idt)

    def __iter__(self):
        it = []
        if self:
            #if self.left:
            if True:
                it.append(self.left)
            it.append(self.root)
            #if self.right:
            if True:
                it.append(self.right)
        self.it = iter(it)
        return self

    def __next__(self):
        return next(self.it)

    def __repr__(self):
        return f"bst({repr(self.root.key)})" if self else repr(None)

    def dic(self):
        '''**bst.dic()'''
        d = {}
        d['keyfunc'] = self.keyfunc
        d['node'] = self.root
        d['left'] = self.left
        d['right'] = self.right
        return d

    def right_rotate1(self):
        left = self.left
        self.left = left.right
        left.right = self
        return left
    
    @staticmethod
    def from_iter(iterbst):
        if not iterbst:
            return None
        try:
            left, node, right = iterbst
        except TypeError:
            raise TypeError('iterbst must be iterable')
        except ValueError:
            raise ValueError('use from_iter2()')
        if not isinstance(node, Node):
            root = Node(node)
        else:
            root = node
        lsub = __class__.from_iter(left)
        rsub = __class__.from_iter(right)
        return __class__(node=root, left=lsub, right=rsub)

    @staticmethod
    def from_iter2(iterbst):
        if not iterbst:
            return None
        try:
            iter(iterbst)
        except TypeError:
            raise TypeError('iterbst must be iterable')
        t = tuple(iterbst)
        if len(t) > 3:
            raise ValueError('iterable of inappropriate form')
        if len(t) == 3:
            left, node, right = t
        elif len(t) == 2:
            if is_iter(t[0]):
                left, node = t
                right = None
            else:
                node, right = t
                left = None
        else:
            node = t[0]
            left = None
            right = None
        if not isinstance(node, Node):
            root = Node(node)
        else:
            root = node
        lsub = __class__.from_iter2(left)
        rsub = __class__.from_iter2(right)
        return __class__(node=root, left=lsub, right=rsub)

    @staticmethod
    def from_bst(bst):
        left, node, right = bst
        d = {}
        d.update(left=left,node=node,right=right)
        return __class__(**d)

    @staticmethod
    def from_bst(bst):
        left, node, right = bst
        d = {}
        d.update(left=left,node=node,right=right)
        return __class__(**d)
    
    def f_bst(self, bst):
        left, node, right = bst
        d = {}
        d.update(left=left,node=node,right=right)
        return __class__(keyfunc=self.keyfunc, **d)

    @staticmethod
    def from_iter_None(t):
        if t is not None:
            left, key, right = t
            root = Node(key)
            lsub = __class__.from_iter_None(left)
            rsub = __class__.from_iter_None(right)
            return __class__(node=root, left=lsub, right=rsub)
        else:
            return __class__()
            
    def right_rotate2(self):
        left, q, c = self
        a, p, b = left
        right = self.f_bst((b, q, c))
        return self.f_bst((a, p, right))

    def __eq__(self, other):
        if not self and not other:
            return True
        elif not self or not other:
            return False
        else:
            return (self.root.key == other.root.key
                    and self.left == other.left
                    and self.right == other.right)

    def display(self):
        if not self:
            return
        def _display(self):
            '''Returns list of str, width, height, horizontal index of root'''
            if not self.left and not self.right:
                line = str(self.root.key)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # only left child
            if not self.right:
                lines, n, p, x = _display(self.left)
                s = str(self.root.key)
                u = len(s)
                first_line = (x+1) * ' ' + (n-x-1) * '_' + s
                next_line = x * ' ' + '/' + (n-x-1+u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, next_line] + shifted_lines, n+u, p+2, n+u//2

            # only right child
            if not self.left:
                lines, m, q, y = _display(self.right)
                s = str(self.root.key)
                u = len(s)
                first_line = s + (y-1) * '_' + (m-y+1 - (not y)) * ' '
                # -(not y) for revise the warped caused by (0-1) * '_' == ''
                next_line = (u+y-1) * ' ' + '\\' + (m-y) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, next_line] + shifted_lines, m+u, q+2, u//2

            # two children.
            left, n, p, x = _display(self.left)
            right, m, q, y = _display(self.right)
            s = str(self.root.key)
            u = len(s)
            first_line = ((x+1) * ' ' + (n-x-1) * '_' + s
                          + (y-1) * '_' + (m-y+1 - (not y)) * ' ')
            next_line = (x * ' ' + '/' + (n-x-1+u+y-1) * ' '
                          + '\\' + (m-y) * ' ')
            if p < q:
                left += [n * ' '] * (q-p)
            elif q < p:
                right += [m * ' '] * (p-q)
            zipped = zip(left, right)
            lines = [first_line, next_line] + [a + u*' ' + b for a, b in zipped]
            return lines, n + m + u, max(p, q) + 2, n + u//2
        lines, *_ = _display(self)
        for line in lines:
            print(line)

    def display2(self):
        if not self:
            return
        def _display(self):
            '''Returns list of str, width, height, horizontal index of root'''
            if not self.left and not self.right:
                line = str(self.root.key)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            # only left child
            if not self.right:
                lines, n, p, x = _display(self.left)
                s = str(self.root.key)
                u = len(s)
                first_line = (x+1) * ' ' + (n-x-1) * '_' + s
                next_line = x * ' ' + '/' + (n-x-1+u) * ' '
                shifted_lines = [line + u * ' ' for line in lines]
                return [first_line, next_line] + shifted_lines, n+u, p+2, n+u//2

            # only right child
            if not self.left:
                lines, n, p, x = _display(self.right)
                s = str(self.root.key)
                u = len(s)
                first_line = s + x * '_' + (n-x) * ' '
                next_line = (u+x) * ' ' + '\\' + (n-x-1) * ' '
                shifted_lines = [u * ' ' + line for line in lines]
                return [first_line, next_line] + shifted_lines, n+u, p+2, u//2

            # two children.
            left, n, p, x = _display(self.left)
            right, m, q, y = _display(self.right)
            s = str(self.root.key)
            u = len(s)
            first_line = ((x+1) * ' ' + (n-x-1) * '_' + s
                          + y * '_' + (m-y) * ' ')
            next_line = (x * ' ' + '/' + (n-x-1+u+y) * ' '
                          + '\\' + (m-y-1) * ' ')
            if p < q:
                left += [n * ' '] * (q-p)
            elif q < p:
                right += [m * ' '] * (p-q)
            zipped = zip(left, right)
            lines = [first_line, next_line] + [a + u*' ' + b for a, b in zipped]
            return lines, n + m + u, max(p, q) + 2, n + u//2
        lines, *_ = _display(self)
        for line in lines:
            print(line)
    
''' below is from original
    def disp(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if not self.right and not self.left:
            line = '%s' % self.root.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if not self.right:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.root.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if not self.left:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.root.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.root.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
#'''
    

def list_recur(iterable):
    l=[]
    for i in iterable:
        try:
            iter(i)
        except TypeError:
            l.append(i)
        else:
            l.append(list_recur(i))
    return l


def tuple_recur(iterable):
    l=[]
    for i in iterable:
        try:
            iter(i)
        except TypeError:
            l.append(i)
        else:
            l.append(tuple_recur(i))
    return tuple(l)

def pp(obj):
    p = pprint.PrettyPrinter(indent=9, width=1)
    p.pprint(obj)


if __name__ == "__main__":
    bst1 = BinarySearchTree(lambda x: -x)
    arr = [2, 6, 4, 3, 2, 7, 8, 1, 9, 5]
    bst1.add_from(arr)
    bst1.print_inorder()
    print([*bst1.inorder()])
    print('describe tree visually (left node in top, root node on left):')
    bst1.pp()
    print()
    print([*bst1])
    print()
    pp(list_recur(bst1))

    from random import randint as r
    b = BinarySearchTree()
    for _ in range(40):
        b.add(r(0,100))

    b.display()
    b.display2()

