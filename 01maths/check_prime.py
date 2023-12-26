def is_prime(n):   # Naive solution
    if n == 1:
        return False
    for i in range(2,n):
            if n % i == 0:
                return False
    return True

print(is_prime(11))


def isprime(n):
    if n == 1:
        return False
    i = 2
    while (i*i <= n):
        if n%i == 0:
            return False
        i += 1
    return True