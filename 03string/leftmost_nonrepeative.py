def lefmost_nonrepeat(string):
    for i in range(len(string)):
        flag = False
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                flag = True
                break
            if flag == False:
                return i
    return -1

print(nonrepeative('rajendra'))


char = 256
def nonrep(string):
    count = [0]*char
    for i in string:
        count[ord(i)] += 1
    for i in range(len(string)):
        if count[ord(string[i])] == 1:
            return i
    return -1


import sys
def leftmostnonrepetitive(string):
    fi = [-1]*char
    for i in range(len(string)):
        if fi[ord(string[i])] == -1:
            fi[ord(string[i])] = i
        else:
            fi[ord[string[i]]] = -2
        res = sys.maxsize
        for i in range(char):
            if fi[i] >= 0:
                res = min(res, fi[i])
        if sys.maxsize:
            return -1
        else:
            return res
    
