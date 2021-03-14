import math
def reverse1(n):
    if n < 0:
        n &= 2 ** (math.floor(math.log2(-n)) + 1) -1
    if n == 0:
        return 0
    if n%2 == 0:
        return reverse1(n//2)
    return reverse1(n-1) + 2 ** math.floor(math.log2(n))


def b1(n):
    if n < 0:
        return n & (2 ** (math.floor(math.log2(-n)) + 1) -1)
    return n

def b2(n):
    if n < 0:
        return n & (2 ** (math.ceil(math.log2(-n)) + 1) -1)
    return n

def r1(n):
    if n == 0:
        return 0
    n = b1(n)
    if n%2 == 0:
        return r1(n//2)
    return r1(n-1) + 2 ** math.floor(math.log2(n))

def r2(n):
    if n == 0:
        return 0
    n = b2(n)
    if n%2 == 0:
        return r2(n//2)
    return r2(n-1) + 2 ** math.floor(math.log2(n))
