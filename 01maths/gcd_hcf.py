def gcd_hcf(m, n):   # Euclidean algorithm
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    return m

def hcf_gcd(a, b):    # Optimised euclidean algorithm
    if b == 0:
        return a
    return hcf_gcd(b, a%b)
    



