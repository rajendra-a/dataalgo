def is_palindrome(num):
    rev = 0
    temp = num
    while temp != 0:
        last_digit = temp%10    # get reminder
        rev = rev*10+last_digit  # reversed number
        temp = temp//10         # to coefficent
    return rev ==  num


print(is_palindrome(1034301))