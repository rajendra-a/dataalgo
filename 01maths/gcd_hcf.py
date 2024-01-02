def gcd_hcf(m, n):   # Euclidean algorithm
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

print(gcd_hcf(23, 34))

def hcf_gcd(a, b):    # Optimised euclidean algorithm
    if b == 0:
        return a
    return hcf_gcd(b, a%b)

print(hcf_gcd(5, 7))



