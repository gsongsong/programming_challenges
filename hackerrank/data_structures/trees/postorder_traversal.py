# https://www.hackerrank.com/challenges/tree-postorder-traversal/problem

# Python2

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    #Write your code here
    if not root:
        return
    postOrder(root.left)
    postOrder(root.right)
    print root.data,
