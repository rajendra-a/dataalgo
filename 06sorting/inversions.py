# Count inversions
def inversions(arr):
    n = len(arr)
    res = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                res += 1
    return res


print(inversions([3, 4, 5, 2, 6, 1]))

# efficient solution
def countmerge(arr, l, m, r):
    left = arr[l:m+1]
    right = arr[m+1:r+1]
    res, i, j, k = 0, 0, 0, l
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += (len(left)-i)
        k += 1
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[j] = right[j]
        j += 1
        k += 1
    return res
        
def inversioncount(arr, l, r):
    res = 0
    if l < r:
        m = (l+r)//2
        res += inversioncount(arr, l, m)
        res += inversioncount(arr, m+1, r)
        res += countmerge(arr, l, m , r)