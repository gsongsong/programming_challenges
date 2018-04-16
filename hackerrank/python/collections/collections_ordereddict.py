# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

import collections

if __name__ == "__main__":
    n = int(input())
    d = collections.OrderedDict()
    for _ in range(n):
        line = input().strip().split(' ')
        item_name = ' '.join(line[:-1])
        net_price = int(line[-1])
        if item_name not in d:
            d[item_name] = net_price
        else:
            d[item_name] += net_price
    for item_name in d:
        print(item_name, d[item_name])
