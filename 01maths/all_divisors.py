def all_divisors(n):   # Naive solution 
    for i in range(1, n+1):
        if n%i == 0:
            print(i)

print(all_divisors(24))


def divisors(n):
    i = 1
    while i*i<=n:
        if n%i == 0:
            print(i)
            if i != n/i:
                print(n/i)
    i += 1
print(divisors(14))
