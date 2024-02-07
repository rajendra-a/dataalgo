def largest(lst: list) -> int:
        for x in lst:
            for y in lst:
                if y > x:
                    break
            else: 
                return x
        return None

print(largest([1, 4, 7, 2, 9, 8]))


def myMax(list1):
    max = list1[0]
    for x in list1:
        if x > max:
            max = x
    return max

print(largest([1, 4, 7, 2, 10, 8]))

