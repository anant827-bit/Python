# 1. Program to match a string that contains only upper and lowercase letters,
# numbers, and underscores

import re

text = "Hello_123"

pattern = r'^[A-Za-z0-9_]+$'

if re.match(pattern, text):
    print("Valid String")
else:
    print("Invalid String")