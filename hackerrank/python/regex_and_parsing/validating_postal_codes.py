# https://www.hackerrank.com/challenges/validating-postalcode/problem

import re

postal_code = input().strip()
print(re.search(r'^[1-9][0-9]{5}$', postal_code) is not None and
      re.search(r'(([0-9])([0-9])\2\3)|(([0-9]).\5([0-9]).\6)', postal_code) is None)
