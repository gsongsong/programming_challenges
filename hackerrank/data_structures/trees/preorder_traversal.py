# https://www.hackerrank.com/challenges/tree-preorder-traversal/problem

# Python2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    #Write your code here
    if not root:
        return
    print root.data,
    preOrder(root.left)
    preOrder(root.right)
