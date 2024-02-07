def second_largest(list2):
    if len(list2) < 2:
        print('Inavalid input')
        return

    largest = second = -2356
    # Find the largest 
    for i in range(0, len(list2)):
        largest = max(largest, list2[i])

    # Find the second largest
    for i in range(0, len(list2)):
        if list[i] != largest:
            second = max(second, list2[i])

    if second == -2356:
         print('There is no second largest element')
    else:
        print('The second largest element is \n', second)
    

print(second_largest([1, 5, 6, 7, 3, 4, 9, 10]))


def second_max(lst: list) -> int:
    if len(lst) < 2:
        print('Invalid input')
        return 

    first = second = -23456
    for i in range(0, len(lst)):
        largest = max(first, lst[i])
        if lst[i] > first:
            second = first
            first = lst[i]

        elif lst[i] > second and lst[i] != first:
            second = lst[i]
    if second == -23456:
        print('There is no second largest element')
    else:
        print('The second largest is: ', second)

print(second_max([4, 5, 3, 7, 2, 8, 1, 10]))