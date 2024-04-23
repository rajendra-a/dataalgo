# Insertion sort is simple sorting algorithm that works similar to the way you sort playing cards in your hands
# the array is virtually split into sorted and unsorted part. Values from unsorted part are picked and placed at 
# correct position in the sorted part 

def insertion_sort(l):
    
    for i in range(1, len(l)):
        x = l[i]
        j = i-1
        
        while j>=0 and x<l[j]:
            l[j+1] = l[j]
            j = j-1
        
        l[j+1] = x
        

print(insertion_sort([20, 5, 40, 60, 10, 30]))