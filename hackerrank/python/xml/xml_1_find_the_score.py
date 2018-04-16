# https://www.hackerrank.com/challenges/xml-1-find-the-score/problem

def get_attr_number(node):
    # your code goes here
    num_attr = 0
    queue = [node]
    while queue:
        n = queue.pop()
        num_attr += len(n.attrib)
        for child in n.getchildren():
            queue.append(child)
    return num_attr
