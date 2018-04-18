# https://www.hackerrank.com/challenges/tree-top-view/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def left(node):
    if not node:
        return
    left(node.left)
    print node.data,

def right(node):
    if not node:
        return
    print node.data,
    right(node.right)

def topView(root):
    #Write your code here
    if not root:
        return
    left(root.left)
    print root.data,
    right(root.right)
