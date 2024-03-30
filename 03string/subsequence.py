# 'ABC' all the substrings are 'A', 'B', 'C', 'AB', 'AC', 'BC', 'ABC'

def subsequence(s1, s2):
    i, j = 0, 0
    while(i<len(s1) and j<len(s2)):
        if s[i] == s2[j]:
            j = j+1
        i = i + 1
    if j == len(s2):
        return True
    else:
        return False
    
    
    