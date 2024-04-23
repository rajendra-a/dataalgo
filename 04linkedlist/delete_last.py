from linked_list import Node

def delete_last(head):
    if head == None:
        return None
    
    if head.next == None:
        return None
    curr = head
    
    while curr.next.next != None:
        curr = curr.next
        
    curr.next = None
    return head