def comp_power(x, n):
    res = 1
    for _ in range(n):
        res = res * x
    return res

print(comp_power(3, 4))


def pow_comp(x, n):
    if n == 0:
        return 1
    temp = pow_comp(x, n//2)
    temp = temp * temp
    if n%2 == 0:
        return temp
    else:
        return temp*x
    
print(pow_comp(3, 5))