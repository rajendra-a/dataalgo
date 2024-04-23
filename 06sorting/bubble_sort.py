# bubble sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
# if they are in the wrong order. This algorithm is not suitable for large data sets as its average and worst case
# time complexity is quite high
# consider asceding order
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
                
        if swapped == False:
                return 
l = [10, 8, 20, 5]
bubblesort(l)
print(*l)