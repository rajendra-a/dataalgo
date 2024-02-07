def reverse_lst(lst):
    lst.reverse()
    return lst

print(reverse_lst([3, 4, 6, 1, 9, 10]))

lst2 = [34, 23, 67, 32]
new1 = list(reversed(lst2))
print(new1)

l = [34, 45, 23, 65]
new2 = l[::-1]
print(new2)

# method2: using two pointer approach
def reverselist(l):
    s = 0
    e = len(l) - 1

    while  s < e:
        l[s], l[e] = l[e], l[s]
        s = s+1
        e = e-1
    return l

print(reverselist([2, 5, 7, 8, 2, 16]))