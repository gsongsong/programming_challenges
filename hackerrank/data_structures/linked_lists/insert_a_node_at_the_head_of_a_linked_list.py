# https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem

"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Insert(head, data):
    return Node(data, head)
