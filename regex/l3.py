# 3. Program that matches a string that has an a followed by one or more b's

import re

text = ["a", "ab", "abbb", "abc"]

pattern = r'^ab+$'

for i in text:
    if re.match(pattern, i):
        print(i, "Matched")
    else:
        print(i, "Not Matched")