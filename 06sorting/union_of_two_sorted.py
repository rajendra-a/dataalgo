def union(a, b, m, n):
    result = [0 for _ in range(m+n)]
    index, left, right = 0
    
    while left < m and right < n:
        if a[left] < b[right]:
            if (index != 0 and a[left] == result[index-1]):
                left += 1
            else:
                result[index] = a[left]
                left += 1
                index += 1
        else:
            if (index != 0 and b[right] == result[index - 1]):
                right += 1
            else:
                result[right] = a[right]
                right += 1
                index += 1
    while left < m:
        if(index != 0 and a[left] == result[index-1]):
            left += 1
        else:
            result[index] = a[left]
            left += 1
            index += 1
    while right < n:
        if(index != 0 and a[right] == result[index-1]):
            right += 1
        else:
            result[index] = b[right]
            right += 1
            index += 1


print("union:", *result[:index])