# Sorted always returns new list containing the sorted elements from an iterable (like a list, tuple, string etc).
# It does not modify the original iterable in-place

# Python sorted function
l = [10, 20, 14]
ls = sorted(l)
print(l)
print(ls)
l = [10, -15, -2, 1]
ls = sorted(l, key=abs, reverse=True)
print(ls)

# Time complexity O(n logn)
t = (10, 12, 5, 1)
print(sorted(t))

s = {'gfg', 'courses', 'python'}
print(sorted(s))

d = {10: 'gfg', 15: 'ide', 5: 'courses'}
print(sorted(d))

l = [(10, 15), (1, 8), (2, 3)]
print(sorted(l))