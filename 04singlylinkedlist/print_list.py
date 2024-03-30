from linked_list import Node

def printlist(head):
    curr = head
    while curr != None:
        print(curr.data, end=' ')
        curr = curr.next
        

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(15)


printlist(head)