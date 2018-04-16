# https://www.hackerrank.com/challenges/merge-the-tools/problem

def merge_the_tools(string, k):
    # your code goes here
    import textwrap
    splitted = textwrap.wrap(string, k)
    fixed = []
    for word in splitted:
        string = ''
        observed = dict()
        for c in word:
            if c in observed:
                continue
            observed[c] = True
            string += c
        print(string)
