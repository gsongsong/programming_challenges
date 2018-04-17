# https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list/problem

"""
 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as
"""
class Node(object):

    def __init__(self, data=None, next_node=None, prev_node = None):
        self.data = data
        self.next = next_node
        self.prev = prev_node
"""
 return the head node of the updated list 
"""
def Reverse(head):
    if not head:
        return
    root = head
    head = head.next
    root.prev, root.next = None, None
    while head:
        root.prev = head
        head = head.next
        root.prev.next, root.prev.prev = root, None
        root = root.prev
    return root
