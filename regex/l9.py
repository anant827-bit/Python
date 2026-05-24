# 9. Program to remove all whitespaces from a string

import re

text = "Python Programming Language"

result = re.sub(r'\s+', '', text)

print(result)