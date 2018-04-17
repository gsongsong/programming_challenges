# https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list/problem

"""
 Insert a node into a sorted doubly linked list
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
def SortedInsert(head, data):
    if not head:
        return Node(data)
    root = head
    while head:
        if data > head.data:
            if not head.next:
                head.next = Node(data, prev_node=head)
                return root
            head = head.next
            continue
        node = Node(data, prev_node=head.prev, next_node=head)
        if not node.prev:
            root = node
        else:
            head.prev.next = node
        head.prev = node
        return root
