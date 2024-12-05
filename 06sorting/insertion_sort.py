# An array values to sort
# An outerloop that fix a value to be sorted. For an array with n values, this outer loop skips the first value, and must run n-1 times
# An innerloop that goes through the sorted part of array, to find where to insert the value. if the value to be sorted is at index i, the sorted part of array
# Start at index 0 and ends at index i-1

def insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        insert_index = i
        current_value = array.pop(i)
        for j in range(i-1, -1, -1):
            if array[j] > current_value:
                insert_index = j
        array.insert(insert_index, current_value)

print(insertion_sort([20, 5, 40, 60, 10, 30]))


# insertion sort can be improved a little bit more
# The way the code above first removes a value and then inserts it somewhere else is intuitive, It is how you would do insertion sort physically with a hand of cards
# for example, If low value cards are sorted to the left, you pick up a new unsorted card, and insert in the correct place between other already sorted cards
def insertionsort(array):
    n = len(array)
    for i in range(1, n):
        insert_index = i
        current_value = array.pop(i)
        for j in range(j-1, -1, -1):
            if array[j] > current_value:
                array[j+1] = array[j]
                insert_index = j
            else:
                break
    array[insert_index] = current_value
        