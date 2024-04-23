def hoare_partition(arr, l, h):
    pivot = arr[l]
    i = l-1
    j = h+l
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]