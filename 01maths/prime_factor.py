from check_prime import is_prime

def prime_factor(n):
    for i in range(2, n+1):
        if is_prime(i):
            x = i
            while n%x == 0:
                print(x)
                x *= i
    
print(prime_factor(100))