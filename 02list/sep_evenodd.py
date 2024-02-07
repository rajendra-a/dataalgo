def even_odd(lst):
    even = []
    odd = []
    for ele in lst:
        if ele%2 == 0:
            even.append(ele)
        else:
            odd.append(ele)
    return even, odd

print(even_odd([14, 16, 3, 2, 1]))