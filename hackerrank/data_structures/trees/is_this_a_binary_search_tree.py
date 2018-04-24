# https://www.hackerrank.com/challenges/is-binary-search-tree/problem

arr = []
def check_binary_search_tree_(root):
    if root.left and not check_binary_search_tree_(root.left):
        return False
    if arr:
        if arr[-1] >= root.data:
            return False
    arr.append(root.data)
    if root.right and not check_binary_search_tree_(root.right):
        return False
    return True
