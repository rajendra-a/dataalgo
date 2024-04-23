from linked_list import Node

def insert_at_begining(data):
    temp = Node(data)
    temp.next = head
    return temp
