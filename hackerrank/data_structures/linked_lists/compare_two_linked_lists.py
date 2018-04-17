# https://www.hackerrank.com/challenges/compare-two-linked-lists/problem

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def CompareLists(headA, headB):
    while headA and headB:
        if headA.data != headB.data:
            return 0
        headA, headB = headA.next, headB.next
    if headA:
        return 0
    if headB:
        return 0
    return 1
