# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    #Write code Here
    if not root:
        return
    queue = [root]
    while queue:
        node = queue.pop(0)
        print node.data,
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
