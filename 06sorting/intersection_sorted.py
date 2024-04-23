# def intersection(arr1, arr2, m, n):
#     i, j = 0, 0
#     while i < m and j < n:
#         if arr1[i] < arr2[j]:
#             i += 1
#         elif arr2[j] < arr1[j]:
#             j += 1
#         else:
#             print(arr2[j], end='')
#             j += 1
#             i += 1
            
# arr1 = [1, 2, 3, 4, 5, 6]
# arr2 = [2, 3, 5, 7]
# m = len(arr1)
# n = len(arr2)
# print(intersection(arr1, arr2, m, n))
# The above program to find intersection of two
# Sorted arrays
def intersection_array(a, b, n, m):
    
    intersection = []
    i = j = 0  
    
    while i < n and j < m:
        if a[i] == b[j]:
            
            if len(intersection) > 0 and intersection[-1] == a[i]:
                i += 1
                j += 1
            else:
                intersection.append(a[i])
                i += 1
                j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    if not len(intersection):
        return [-1]
    return intersection