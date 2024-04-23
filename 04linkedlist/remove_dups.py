from linked_list import Node

def removedups(head):
    curr = head
    while curr != None and curr.next!= None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next