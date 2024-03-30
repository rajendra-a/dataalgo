def left_most(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return i
    return -1
    
char = 256
def leftmost(string):
    count[0]*char
    for i in range(len(string)):
        count[ord(string[i])] += 1
    for i in range(len(string)):
        if count[ord(string[i])] > 1:
            return i

import sys
def leftmost3(string):
        findex = [-1]*char
        res = sys.maxsize
        for i in range(len(str)):
            if fndex[ord(string[i])] == -1:
                findex[ord(string[i])] = i
            else: 
                res = min(res,findex[ord(string[i])])
        if res == sys.maxsize:
            return -1
        else:
            return res
        