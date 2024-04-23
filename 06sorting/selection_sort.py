# selection sort
# The selection algorithm sorts an array by repeatedly finding the minimum element from unsorted part and
# and putting it at the beginning. The algorithm maintains two subarrays in a given array
# The subarray which is already sorted.
# The remaining subarray which is unsorted. in every iteration of selection sort, the minimum element 
# from the unsorted subarray is picked and moved to the sorted subarray
def selection_sort(l):
    
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            
            if l[j] > l[min_ind]:
                min_ind = j
                
        l[min_ind], l[i] = l[i], l[min_ind]
        