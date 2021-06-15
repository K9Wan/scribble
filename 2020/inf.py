class Infinity(object):
    inf = None
    def __new__(cls, *args, **kwargs):
        if cls.inf is None:
            cls.inf = super().__new__(cls, *args, **kwargs)
        return cls.inf
    def __gt__(self, other):
        return True
    
    pass
