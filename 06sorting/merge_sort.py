# The merge sort algorithm is algorithm that is based on the devide and conquer paradigm. In this algorithm, the array
# is initially devided into two equal halves and then they are combined in a sorted manner


# Merge sort working process:
# Think of it as a recursive algorithm continuously splits the array in half until it cannnot be further devided.
# This means that if the array becomes empty or has only one element left, the deviding will stop, i.e. it is the base 
# case to stop recursion. If the array has multiple elements. split the array into halves and recursively invoke merge
# sort on each of the halves. Finally when both halves are sorted, the merge operation is applied. Merge operation
# merge opertion is the process of taking two smaller sorted arrays and combining them eventually make a larger one.

def merge(arr, start, mid, end):
    # creating and intializing the left subarray and right sub arrays
    # extra space - outplace sorting algorithm
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
    k  += 1

    # Copying the remaining elements from left subtree
    while i < len(left):
        arr[k] = arr[i]
        i += 1
        k += 1

    # Copying the remaining elements from right subtree
    while j < len(right):
        arr[k] = right[j] 
        j += 1
        k += 1
        
def merge_sort(arr, start, end):
    if start < end:
        # Devide
        mid = start+(end-start)//2

        # Conquer
        # Recursive call for left subtree
        merge_sort(arr, start, mid)
        # Recursive call for right subtree
        merge_sort(arr, mid+1, end)
        # combine
        # combine the left and right subtrees
        merge(arr, start, mid, end)
        
# Drivercode
arr = [10, 5, 30, 15, 7]

start = 0

end =len(arr) - 1

n = len(arr)


# function calling
merge_sort(arr, 0, 4)

print(arr)

