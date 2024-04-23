from linked_list import Node

def sorted_insert(head, x):
    temp = Node(x)
    if head == None:
        return temp
    elif x < head.data:
        temp.next = head
        return temp
    else:
        curr = head
        while curr.next != None and curr.next.data < x:
            curr = curr.next
        temp.next = curr.next
        curr.next = temp
        return head