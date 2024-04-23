# Given two sorted arrays
def printUnion(arr1, arr2, m, n):
    i, j = 0, 0
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            print(arr1[i], end='')
            i += 1
        elif arr1[j] < arr2[i]:
            print(arr2[j], end='')
            j += 1
        else:
            print(arr2[j], end='')
            i += 1
            j += 1
    while i < m:
        print(arr1[i], end='')
        i += 1
    while j < n:
        print(arr2[j], end='')
        j += 1
        

    