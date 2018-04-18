# https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):
    #Enter your code here
    if not root:
        return
    node = root
    while True:
        if v1 < node.data and v2 < node.data:
            node = node.left
            continue
        if v1 > node.data and v2 > node.data:
            node = node.right
            continue
        return node

