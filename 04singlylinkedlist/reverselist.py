from linked_list import Node

# Naive solution

def reverse(head):
    stack = []
    curr = head
    while curr is not None:
        stack.append(curr.data)
        curr = curr.next
    curr = head
    while curr is not None:
        curr.data = stack.pop()
        curr = curr.next
    return head
        

def reverselist(head):
    curr = head
    prev = None
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev

