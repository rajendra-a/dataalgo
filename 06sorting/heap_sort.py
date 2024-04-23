# Heap sort is a comparision based sorting technique based on binary heap data structure
# It is similar to selection sort first we find the maximum element at the end. We repeat the same process for remaining

# What is binary heap:
# let us first define complete binary tree. A complete binary tree is a binary tree in which every level, except possibly
# the last, is completely filled, and all nodes are as far left as possible

'''
A Binary heap is complete binary tree where items are sorted in special order such that the value in parent node is greater
Than the values in its two children nodes. The former is called as max heap and latter is called min heap. The heap can be
represented by binary tree or array
'''

'''
Array based representation for binary heap: Since binary heap is complete binary tree, It can be easily represented as
array based representation is space efficient. if the parent node is sorted at index i, the left child can be calculated
by 2 * i + 1,  and right child by 2 * i + 2
'''

'''Heap sort algorithm for sorting an array in increasing order:
1. Build the max heap from the input.
2. At this point, the largest item is stored at the root of the heap. Replace it with the last item of the heap followed
by reducing the size of the heap by 1. Finally, heapify the root of the tree.
3. Repeat above steps while size of the heap is greater than 1.
'''

# How to build the heap?
'''Heapify procedure can be applied to a node only if its children nodes are heapified. So the heapification must be
performed in the bottom up order
'''
def build_maxheap(arr):
    n = len(arr)
    for i in range((n-2)//2, -1, -1):
        heapify(arr, n, i)
        
def heapify(arr, n, i):
    # Find largest among root and children
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[i] < arr[l]:
        largest = l
    if r < n and arr[i] < arr[r]:
        largest = r
        
    # If root is not largest, swap with largest and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n ,largest)
        
        
def heapsort(arr):
    n = len(arr)
    
    # Build max heap
    build_maxheap(arr)
        
    for i in range(n-1, 0, -1):
        # Swap
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, n, 0)
        