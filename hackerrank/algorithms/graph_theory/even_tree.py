#!/bin/python3

# https://www.hackerrank.com/challenges/even-tree/problem

import sys

class Node:
    def __init__(self, value, parent = None, children = []):
        self.value = value
        self.parent = None
        self.children = []
        self.tree_size = 1
        self.visited = False

    def add_child(self, node):
        self.children.append(node)
        node.parent = self
        self.tree_size += node.tree_size
        parent = self.parent
        while parent:
            parent.tree_size += node.tree_size
            parent = parent.parent

    def remove_child(self, node):
        pass

class Tree:
    def __init__(self):
        self.root = Node(1)
        self.nodes = [self.root]

    def get_node(self, value):
        for node in self.nodes:
            if node.value == value:
                return node
        return None

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, tree_t):
        # Assume parent already exists
        parent = self.get_node(tree_t[1])
        child = Node(tree_t[0])
        parent.add_child(child)
        self.add_node(child)

    def bfs(self):
        num_cuts = 0
        queue = [self.root]
        self.root.visited = True
        while queue:
            node = queue.pop(0)
            for child in node.children:
                if not child.visited:
                    if child.tree_size and child.tree_size % 2 == 0:
                        num_cuts += 1
                    queue.append(child)
                child.visited = True
        return num_cuts

def evenTree(n, m, tree):
    # Complete this function
    t = Tree()
    for tree_t in tree:
        t.add_edge(tree_t)
    # for node in t.nodes:
        # print(node.value, end = ', ')
        # if node.parent:
        #     print('Parent: ' + str(node.parent.value), end = ', ')
        # print(str(node.tree_size) + ' nodes:    ' + ', '.join([str(child.value) for child in node.children]))
    return t.bfs()

if __name__ == "__main__":
    n, m = input().strip().split(' ')
    n, m = [int(n), int(m)]
    tree = []
    for tree_i in range(m):
       tree_t = [int(tree_temp) for tree_temp in input().strip().split(' ')]
       tree.append(tree_t)
    result = evenTree(n, m, tree)
    print(result)
