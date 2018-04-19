# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    #Enter Your Code Here
    string = []
    node = root
    idx = 0
    while True:
        if not node.left and not node.right:
            string.append(node.data)
            node = root
        else:
            if idx == len(s):
                break
            if s[idx] == '0':
                node = node.left
            else:
                node = node.right
            idx += 1
    print ''.join(string)

