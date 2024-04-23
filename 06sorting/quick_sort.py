def lomudo_partition(arr, l, h):
    pivot = arr[h]
    i = l-1
    for j in range(l,h):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[h] = arr[i+1], arr[h]
    return i + 1

def quicksort(arr, l, h):
    if l < h:
        lomudo_partitionpartition(arr, l , h)
        quicksort(arr, l, p-1)
        quicksort(arr, p+1, h)
        



def hoarse_partition(arr, l , h):
    pivot = arr[l]
    i = l-1
    j = h-1
    while True:
        i+= 1
        while arr[i] < pivot:
            i += 1
        j-=1
        while arr[j] < pivot:
            j-= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, l, h):
    if l < h:
        hoarse_partition(arr, l, h)
        quick_sort(arr, l , p)
        quick_sort(arr, p+1, h)    