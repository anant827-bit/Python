# 6. Program that matches a word at the beginning of a string

import re

text = "Python is easy"

pattern = r'^\w+'

match = re.search(pattern, text)

if match:
    print("Matched Word:", match.group())