from linked_list import Node


def del_node(pointer):
    temp = pointer.next
    pointer.data = temp.data
    pointer.next = temp.next