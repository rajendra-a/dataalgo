# Trailing 0s of n! = count of 5s in prime factors of n! 
                   # = floor(n/5) + floor(n/25) + floor(n/125)
def trailing(n):
    count = 0
    # keep dividing by powers of 5 and update count
    i = 5
    while n/i >= 1:
        count += int(n/i)
        i *= 5
    return int(count)

n = 100
print("Count of trailing is"+"in 100 ! is", trailing(n))
