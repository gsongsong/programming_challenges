# https://www.hackerrank.com/challenges/binary-search-tree-insertion/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def insert(r,val):
    #Enter you code here.
    if not r:
        return Node(val)
    root = r
    while True:
        if val < r.data:
            if r.left:
                r = r.left
            else:
                r.left = Node(val)
                return root
        else:
            if r.right:
                r = r.right
            else:
                r.right = Node(val)
                return root
