# https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem 

"""
 Delete Node at a given position in a linked list
 Node is defined as
"""

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

"""
 return back the head of the linked list in the below method. 
"""

def Delete(head, position):
    if not head:
        return head
    if position == 0:
        return head.next
    root = head
    for _ in range(position - 1):
        head = head.next
    if head.next:
        head.next = head.next.next
    else:
        head.next = None
    return root
