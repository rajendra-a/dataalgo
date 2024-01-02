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
    # divisors of a number always appear in pair
    # if (x,y) is in pair
    # and if   x <= y
            #  x*x<=n
            #   x = sqrt(n)
    while (i*i <= n): 
        if n%i == 0:
            return False
        i += 1
    return True

print(isprime(34))

def check_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n%i == 0:
            return False
        i += 6
    return True

print(check_prime(23))