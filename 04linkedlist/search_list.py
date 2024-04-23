from linked_list import Node

        
def search(x):
    pos = 1
    curr = head
    while curr != None:
        if curr.data == x:
            return pos
        pos += 1
        curr = curr.next
    return -1