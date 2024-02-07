def left_rotate(lst):
    lst = lst[1:]+lst[0:1]
    return lst


# Using append pop method
lst = [1, 2, 5, 6, 7, 8]
lst.append(lst.pop(0))
print(lst)


# Using iterative method
def rotatebyone(lst):
    n = len(lst)
    x = lst[0]
    for i in range(1, n):
        lst[i-1] = lst[i]

    lst[n-1] = x
    return lst


print(rotatebyone([12, 45, 56, 65, 67]))