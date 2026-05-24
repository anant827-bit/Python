# 2. Program that matches a string that has an a followed by zero or more b's

import re

text = ["a", "ab", "abbb", "ac"]

pattern = r'^ab*$'

for i in text:
    if re.match(pattern, i):
        print(i, "Matched")
    else:
        print(i, "Not Matched")