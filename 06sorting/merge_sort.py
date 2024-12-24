# Merge sort algorithm is a devide and conquer that sorts an array by breaking down into smaller arrays, and then building the array back
# together the correct way that it sorted

# Devide
# The Algorithm starts with breaking up the array smaller and smaller pieces untitll one such subarray only consists of one element

# Conquer
# The algorithm merges the small pieces of the array back together by putting the lowest value first, resulting in sorted array

# The breaking down and building up of the array to sort the array is done recursively

def merge(arr, start, mid, end):
    # Create and intialize left and right sorted subarray
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    i = j = 0
    k = start

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copying remaining elements of left subarray
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
      

    # Copying remaining element of right subarray
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        


# function definition of merge sort
def mergesort(arr, start, end):
    if start < end:
        mid = start + (end - start) // 2
        mergesort(arr, start, mid)
        mergesort(arr, mid+1, end)
        merge(arr, start, mid, end)



arr = [2, 1, 4, 2, 3, 6, 8, 9, 4, 10, 11, 54, 23]
start = 0
end = len(arr) - 1 
n = len(arr)

for i in range(n):
    print(arr[i], end=' ')

mergesort(arr, start, end)

for i in range(n):
    print(arr[i], end=' ')