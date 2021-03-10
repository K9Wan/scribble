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
