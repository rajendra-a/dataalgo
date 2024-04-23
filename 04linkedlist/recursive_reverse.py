from linked_list import Node

#Method1
def reverse_list(head):
    if head == None:
        return head
    if head.next  == None:
        return head
    rest_head = reverse_list(head.next)
    rest_tail= head.next
    rest_tail.next = head
    head.next = None
    return rest_head

#Method2
def reverselst(curr, prev= None):
    if curr == None:
        return prev
    next = curr.next
    curr.next = prev
    return reverselst(next, curr)