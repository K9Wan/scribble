### https://oeis.org/A002473
def prime29(m):   # will be displaced by non-hardcoded version
    return list(filter(lambda x: x<=m, [2,3,5,7,11,13,17,19,23,29]))

def smooth(n):
    primes = prime29(n)
    S = [1]
    index = [0]*len(primes)
    n = [0]*len(primes)
    while True:
        yield S[-1]
        for i, p in enumerate(primes):
            n[i] = p * S[index[i]]
        m = min(n)
        S.append(m)
        for i in range(len(primes)):
            index[i] += n[i]==m

s = smooth(7)
for n in s:
    if n>=100:
        print(n)
        break
    print(n, end=', ')

