def count_digits(n):
    result = 0
    while n > 0:
        n = n // 10
        result = result + 1
    return result 

print(count_digits(676686875))


# Key take away: here // operator gives you integral part of  coefficent  123/10 => 12.3  but 123//10 => 12