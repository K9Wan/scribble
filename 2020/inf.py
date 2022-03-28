import functools

class Infinity(object):
    inf = None
    def __new__(cls, *args, **kwargs):
        if cls.inf is None:
            cls.inf = super().__new__(cls, *args, **kwargs)
        return cls.inf
    def __gt__(self, other):
        return True
    def __ge__(self, other):
        return True
    def __lt__(self, other):
        return False
    def __le__(self, other):
        return False

class Infinity2(object):
    inf = None
    def __new__(cls, *args, **kwargs):
        if cls.inf is None:
            cls.inf = super().__new__(cls, *args, **kwargs)
        return cls.inf
    def __gt__(self, other):
        return other is not self
    def __ge__(self, other):
        return True
    def __lt__(self, other):
        return False
    def __le__(self, other):
        return other is self

@functools.total_ordering
class Infinity3(object):
    inf = None
    def __new__(cls, *args, **kwargs):
        if cls.inf is None:
            cls.inf = super().__new__(cls, *args, **kwargs)
        return cls.inf
    def __gt__(self, other):
        return True

@functools.total_ordering
class Infinity4(object):
    inf = None
    def __new__(cls, *args, **kwargs):
        if cls.inf is None:
            cls.inf = super().__new__(cls, *args, **kwargs)
        return cls.inf
    def __ge__(self, other):
        return True

inf = functools.total_ordering(type('Inf',(),{'__ge__':lambda a,b: True}))()
