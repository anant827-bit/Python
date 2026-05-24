# 4. Program that matches a string that has an a followed by three 'b'

import re

text = ["abbb", "abbbb", "abb"]

pattern = r'^abbb$'

for i in text:
    if re.match(pattern, i):
        print(i, "Matched")
    else:
        print(i, "Not Matched")