from linked_list import Node

def insert_at_position(head, data, pos):
    temp = Node(data)
    if pos == 1:
        temp.next = head
        return temp
    
    for i in range(pos-2):
        curr = curr.next 
        if curr == None:
            return head
    temp.next = curr.next
    curr.next = temp
    return head
