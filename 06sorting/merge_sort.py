# The merge sort algorithm is algorithm that is based on the devide and conquer paradigm. In this algorithm, the array
# is initially devided into two equal halves and then they are combined in a sorted manner


# Merge sort working process:
# Think of it as a recursive algorithm continuously splits the array in half until it cannnot be further devided.
# This means that if the array becomes empty or has only one element left, the deviding will stop, i.e. it is the base 
# case to stop recursion. If the array has multiple elements. split the array into halves and recursively invoke merge
# sort on each of the halves. Finally when both halves are sorted, the merge operation is applied. Merge operation
# merge opertion is the process of taking two smaller sorted arrays and combining them eventually make a larger one.

<<<<<<< HEAD
def merge(arr, low, mid, high):
    # creating left and right sub arrays
    left = arr[low:mid + 1]
    right = arr[mid + 1: high + 1]
=======
def merge(arr, start, mid, end):
    # creating and intializing the left subarray and right sub arrays
    # extra space - outplace sorting algorithm
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
>>>>>>> f483e652a735d5d5b103600db9a9c271d3841686
    i = j = 0
    k = start
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
<<<<<<< HEAD
            arr[k] = left[i]
            
            k += 1
=======
            arr[k] = left[i]
>>>>>>> f483e652a735d5d5b103600db9a9c271d3841686
            i += 1
        else: 
<<<<<<< HEAD
            arr[k] = right[j]
            
            k += 1
=======
            arr[k] = right[j]
>>>>>>> f483e652a735d5d5b103600db9a9c271d3841686
            j += 1
    k  += 1

    # Copying the remaining elements from left subtree
    while i < len(left):
<<<<<<< HEAD
        arr[k] = arr[i]
        
=======
        arr[k] = arr[i]
>>>>>>> f483e652a735d5d5b103600db9a9c271d3841686
        i += 1
        k += 1

    # Copying the remaining elements from right subtree
    while j < len(right):
<<<<<<< HEAD
        arr[k] = right[j] 
        
=======
        arr[k] = right[j] 
>>>>>>> f483e652a735d5d5b103600db9a9c271d3841686
        j += 1
        k += 1
        
<<<<<<< HEAD
def merge_sort(arr, low, high):
    if low > high:
        mid = (low+high)//2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)
        merge(arr, low, mid, high)
        
=======
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
>>>>>>> f483e652a735d5d5b103600db9a9c271d3841686
arr = [10, 5, 30, 15, 7]

start = 0

end =len(arr) - 1

n = len(arr)


# function calling
merge_sort(arr, 0, 4)

print(arr)

