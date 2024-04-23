from linked_list import Node

#method1
def printnth_node_from_end(head, n):
    len = 0
    curr = head
    while curr:
        curr = curr.next
        len += 1
    if len < n:
        return
    curr = head
    for i in range(1, len-n+1):
        curr = curr.next 
        print(curr.data)
        
#method2
def printnthfromend(head, n):
    if head == None:
        return
    first = head
    for i in range(n):
        if first == None:
            return
        first= first.next
        second = head
    while first != None:
        second = second.next
        first = first.next
    print(second.data)
        