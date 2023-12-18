def factorial(n):
    res = 1    
    for i in range(2, n+1):     # Using Iteration
        res = res * i
    return res



def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)          # Using recursion