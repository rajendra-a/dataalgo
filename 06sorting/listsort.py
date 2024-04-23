l1 = [1, 4, 5, 6]
l1.sort()
print(l1)

l2 = [3, 5, 4, 7, 2]
l2.sort(reverse=True)
print(l2)

l3 = ['gfg', 'courses', 'python']
l3.sort()
print(l3)

def myfun(s):
    return len(s)
l =  ['gfg', 'courses', 'python']
l.sort(key=myfun)
print(l)


l.sort(key=myfun, reverse=True) #Time complexity O(nlogn) #Space complexity O(1)


# The below example sorts the list in increasing order based on the first value of pair
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def myFun(p):
    return p.x
l = [Point(1, 5), Point(10, 5) , Point(3, 8)]
l.sort(key=myFun)

for i in l:
    print(i.x, i.y)


