def is_sorted(l):
    l2 = sorted(l)
    
    if 1 == l2:
        return True
    else:
        return False

print(is_sorted([2, 5, 6, 43, 34]))

def sortedaa(l):
    for i in range(len(l)):
        if l[i-1] > l[i]:
            return False
    return True

print(sortedaa([45, 23, 65, 76]))