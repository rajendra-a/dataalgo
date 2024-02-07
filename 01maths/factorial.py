def factorial(n):
    res = 1    
    for i in range(2, n+1):     # Using Iteration
        res = res * i
    return res

print(factorial(7))


def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)          # Using recursion

print(fact(6))

def facto(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while n > 1:
            fact *= n
            n -= 1
        return fact
num = 5
print("Factorial of",num,"is", facto(num))