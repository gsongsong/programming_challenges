# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem

#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
"""

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

"""
 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    root = head
    numel = 0
    while head:
        numel += 1
        head = head.next
    position = numel - position
    head = root
    for _ in range(position - 1):
        head = head.next
    return head.data
