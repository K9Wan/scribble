from math import inf

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def add(t, q, func=lambda x: x):
    if not t:
        return Node(q)
    elif func(q) < func(t.data):
        return Node(t.data, add(t.left, q, func), t.right)
    elif func(q) > func(t.data):
        return Node(t.data, t.left, add(t.right, q, func))
    else:
        return Node(q, t.left, t.right)

def inorder1(t):
    if not t:
        return
    yield from inorder1(t.left)
    yield t.data
    yield from inorder1(t.right)

def to_str1(t):
    return "->".join(map(str, inorder1(t)))

def minimum(t, r=inf, func=lambda x: x):
    pass

class btree:
  def __init__(self, t=None, func=lambda x: x)
      self.t = t
      self.func = func
  def __str__(self):
      return to_str1(self.t)
  def add(self, q):
      return btree(add(self.t, q))
  def inorder1(self):
      return inorder1(self.t)



