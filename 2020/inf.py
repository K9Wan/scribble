import functools

class Infinity(object):
    _inf = None
    def __new__(cls, *args, **kwargs):
        if cls._inf is None:
            cls._inf = super().__new__(cls, *args, **kwargs)
        return cls._inf
    def __gt__(self, other):
        return True
    def __ge__(self, other):
        return True
    def __lt__(self, other):
        return False
    def __le__(self, other):
        return False

class Infinity2(object):
    _inf = None
    def __new__(cls, *args, **kwargs):
        if cls._inf is None:
            cls._inf = super().__new__(cls, *args, **kwargs)
        return cls._inf
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
    _inf = None
    def __new__(cls, *args, **kwargs):
        if cls._inf is None:
            cls._inf = super().__new__(cls, *args, **kwargs)
        return cls._inf
    def __gt__(self, other):
        return True

@functools.total_ordering
class Infinity4(object):
    _inf = None
    def __new__(cls, *args, **kwargs):
        if cls._inf is None:
            cls._inf = super().__new__(cls, *args, **kwargs)
        return cls._inf
    def __ge__(self, other):
        return True

inf = functools.total_ordering(type('Inf',(),{'__ge__':lambda a,b: True}))()
