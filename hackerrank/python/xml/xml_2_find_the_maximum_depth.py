# https://www.hackerrank.com/challenges/xml2-find-the-maximum-depth/problem

import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    # your code goes here
    stack = [(elem, level)]
    while stack:
        tag, lev = stack.pop()
        children = tag.getchildren()
        if not children:
            maxdepth = max(maxdepth, lev + 1)
            continue
        for child in children:
            stack.append((child, lev + 1))

if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + '\n'
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)
