from linked_list import Node

def insert_at_end(data):
    if head == None:
        return Node(data)
    curr = head
    while curr.next != None:
        curr = curr.next
    curr.next = Node(data)
    return head