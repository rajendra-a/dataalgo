def remove_dup(lst):
    res = []
    for ele in lst:
        if ele not in res:
            res.append(ele)
    return res 


print(remove_dup([3, 4, 5, 6, 7, 8, 9, 4, 5, 6]))



