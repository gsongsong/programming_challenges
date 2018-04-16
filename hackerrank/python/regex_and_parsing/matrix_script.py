# https://www.hackerrank.com/challenges/matrix-script/problem

import re

pattern = r'([0-9a-zA-Z])([!@#$%& ]+)([0-9a-zA-Z])'
n, m = map(int, input().strip().split())
mat = [input() for row in range(n)]
melted = ''.join([mat[i][j] for j in range(m) for i in range(n)])
decoded = re.sub(pattern, r'\g<1> \g<3>', melted)
print(decoded)
