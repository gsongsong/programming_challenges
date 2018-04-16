# https://www.hackerrank.com/challenges/re-start-re-end/problem

import re

if __name__ == "__main__":
    string = input().strip()
    pattern = input().strip()
    offset, num_match = 0, 0
    while string:
        m = re.search(pattern, string)
        if m:
            num_match += 1
            print('({0}, {1})'.format(offset + m.start(), offset + m.end() - 1))
            offset += m.start() + 1
            string = string[m.start() + 1:]
        else:
            if not num_match:
                print('(-1, -1)')
            break

