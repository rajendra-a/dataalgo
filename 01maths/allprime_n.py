from check_prime import isprime
def prime_n(n):
    for i in range(2, n+1):
        if isprime(i):
            print(i, end=" ")

print(prime_n(23))