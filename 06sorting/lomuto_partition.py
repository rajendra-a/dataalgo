def lomuto_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1] 
    return i+1           
        
print(lomuto_partition([2, 4, 5, 12, 9, 7, 8, 11], 0, 7))
