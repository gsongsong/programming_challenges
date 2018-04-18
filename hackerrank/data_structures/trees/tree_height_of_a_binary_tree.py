# https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def height(root):
    height = 0
    if not root:
        return 0
    queue = [(root, 0)]
    while queue:
        node, h = queue.pop()
        if h > height:
            height = h
        if node.left:
            queue.append((node.left, h + 1))
        if node.right:
            queue.append((node.right, h + 1))
    return height
