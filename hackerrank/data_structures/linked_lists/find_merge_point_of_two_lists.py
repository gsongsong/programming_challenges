# https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists/problem

"""
 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as
"""

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def FindMergeNode(headA, headB):
    rootB = headB
    while headA:
        headB = rootB
        while headB:
            if headA == headB:
                return headA.data
            headB = headB.next
        headA = headA.next
