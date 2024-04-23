# The merge sort algorithm is algorithm that is based on the devide and conquer paradigm. In this algorithm, the array
# is initially devided into two equal halves and then they are combined in a sorted manner


# Merge sort working process:
# Think of it as a recursive algorithm continuously splits the array in half until it cannnot be further devided.
# This means that if the array becomes empty or has only one element left, the deviding will stop, i.e. it is the base 
# case to stop recursion. If the array has multiple elements. split the array into halves and recursively invoke merge
# sort on each of the halves. Finally when both halves are sorted, the merge operation is applied. Merge operation
# merge opertion is the process of taking two smaller sorted arrays and combining them eventually make a larger one.

def merge(a, low, mid, high):
    left = a[low:mid + 1]
    right = a[mid + 1: high + 1]
    i = j = 0
    k = low
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a[k] = left[i]
            
            k += 1
            i += 1
        else: 
            a[k] = right[j]
            
            k += 1
            j += 1
            
    while i < len(left):
        a[k] = left[i]
        
        i += 1
        k += 1
    
    while j < len(right):
        a[k] = right[j]
        
        j += 1
        k += 1
    
def merge_sort(arr, l, r):
    if r > l:
        m = (r+l)//2
        merge_sort(arr, l, m)
        merge_sort(arr, m+1, r)
        merge(arr, l, m, r)
        
arr = [10, 5, 30, 15, 7]

merge_sort(arr, 0, 4)

print(*arr)  