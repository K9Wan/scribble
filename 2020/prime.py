def is_prime(n):
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

def prime1(n):
    primes = []
    if n>=2:
        primes.append(2)
    if n>=3:
        primes.append(3)
    for i in range(5,n+1,2):
        isprime=True
        sqrt = int(i ** 0.5)
        for p in primes:
            if p > sqrt: break
            if i%p == 0:
                isprime=False
        if isprime:
            primes.append(i)
    yield from primes

def prime2(n):
    yield from filter(is_prime, range(2, n+1))

def prime3(n):  ## original from https://www.linkedin.com/pulse/sieve-eratosthenes-kotlin-john-farrell
    import itertools as it
    def sieve(p, seq):
        for i in seq:
            if i%p:
                yield i
    primes = it.count(2)
    while True:
        p = next(primes)
        if p>n: break
        yield p
        primes = sieve(p, primes)

def prime1_2(n):
    primes = []
    if n>=2:
        primes.append(2)
    if n>=3:
        primes.append(3)
    for i in range(5,n+1,2):
        for p in primes:
            if i%p == 0:
                break
        else:
            primes.append(i)
    yield from primes

def prime3_2(n):
    import itertools as it
    def sieve(p, seq):
        yield from (i for i in seq if i%p)
    primes = it.count(2)
    while True:
        p = next(primes)
        if p>n: break
        yield p
        primes = sieve(p, primes)

def prime4(n):
    def sieve(seq):
        p = next(seq, None)
        if not p:
            return
        yield p
        yield from sieve(x for x in seq if x%p)
    yield from sieve(iter(range(2, n+1)))

