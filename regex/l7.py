# 7. Program to search some literal strings in a string

import re

text = "Python is simple and Python is powerful"

pattern = r'Python'

match = re.findall(pattern, text)

print("Occurrences found:", len(match))