""" original code from
https://stackoverflow.com/a/25344494
"""
def fivesmooth():
    S = [1]
    i2 = 0  # current index in 2S
    i3 = 0  # current index in 3S
    i5 = 0  # current index in 5S
    while True:
        yield S[-1]
        n2 = 2 * S[i2]
        n3 = 3 * S[i3]
        n5 = 5 * S[i5]
        m = min(n2, n3, n5)
        S.append(m)
        i2 += n2 == m
        i3 += n3 == m
        i5 += n5 == m

def a(n):
    a=fivesmooth()
    while True:
        aa=next(a)
        if aa>n:
            break
        yield aa
 
print(tuple([*a(10000)]))

## https://oeis.org/A051037
