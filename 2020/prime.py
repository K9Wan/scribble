def is_prime(n):
    if n < 2:
        return False
    if n in (2,3):
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+3, 2):
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
        for p in primes:
            if i%p == 0:
                isprime=False
        if isprime:
            primes.append(i)
    yield from primes
