def get_smaller(arr, x):
    res = []
    for ele in arr:     
        if ele < x:
            res.append(ele)
    return res