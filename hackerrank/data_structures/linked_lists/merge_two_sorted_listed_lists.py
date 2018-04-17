# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists/problem

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
"""

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

"""
 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    root = Node()
    last = root
    while headA and headB:
        if headA.data < headB.data:
            last.next = headA
            headA = headA.next
        else:
            last.next = headB
            headB = headB.next
        last =  last.next
    if headA:
        last.next = headA
    else:
        last.next = headB
    return root.next
