def lcm(a, b):
    res = max(a, b)
    while True:
        if res%a == 0 and res%b == 0:
            return res
        res += 1
    return res

print(lcm(3, 4))


def gcd(a, b):
    if b == 0:
        return b
    return gcd(b, a%b)

print(gcd(6, 8))

# There is a multiplication formula for the a*b = gcd(a,b)*lcm(*a,b)
# So LCM of the a and b = a*b//gcd(a,b)

def lcmformula(a,b):
    return a*b//gcd(a,b)

print(lcmformul(4, 6))

