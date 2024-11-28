# bubble sort is an algorithm that sorts an array from the lowest value to the heighest value
# The word bubble comes from how this algorithm works it makes the highest values 'bubble up'    
####how it works####
"""
go through the array, one value at a time
for each value compare the value with next value
if the value is higher than next one, swap the values so that the highest values comes last
go through the array as many times as there are values in the array
"""
def bubble_sort(l):
    n = len(l)
    
    for i in range(n-1):
        
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

l = [10, 8, 20, 5]
bubble_sort(l)
print(*l)


# we can add a flag to optimize the bubble sort (basically it stops when list become sorted)
# The below code is slightly optimized the bubble sort
def bubblesort(l):
    n = len(l)
    
    for i in range(n -1):
        swapped = False
        
        for j in range(n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                
                swapped = True
                
        if not swapped:
            break
l = [10, 8, 20, 5]
bubblesort(l)
print(*l)