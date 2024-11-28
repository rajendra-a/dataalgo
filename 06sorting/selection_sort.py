# selection sort
# The selection algorithm sorts an array by repeatedly finding the minimum element from unsorted part and
# and putting it at the beginning. The algorithm maintains two subarrays in a given array
####how it works####
"""
1. go through the array to find the lowest value
2. move the lowest value to the front
3. go through the array as many times as there are values 
"""
def selection_sort(l):
    
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            
            if l[j] < l[min_ind]:
                min_ind = j
                
        min_value = l.pop(min_ind)
        l.insert(i, min_value)


# there is a shifting problem in the above selection sort
# whenever we find a lowest value in unsorted array we are poping it, so the array will be shifting their values to one index down to make up the removal
# likewise to insert in the front we need to shift one position of all the followiing values
        
"""
Solution: Swap values 
swap the first value of unsorted array with lowest value found in array
"""
def selection_sort(l):
    
    for i in range(n - 1):
        min_ind = i
        for j in range(i + 1, n):
            
            if l[j] < l[min_ind]:
                min_ind = j
                
        l[min_ind], l[i] = l[i], l[min_ind]
        