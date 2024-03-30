from linked_list import Node

# Naive method
def middle(head):
    if head == None:
        return
    count = 0
    current = head
    while current:
        curr = curr.next
        count += 1
    current = head
    for i in range(count//2):
        current = current.next
    print(current.data)

# the better solution        
def print_middle(head):
    if head == None:
        return
    slow = head
    fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    print(slow.data)