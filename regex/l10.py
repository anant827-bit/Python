# 10. Program to validate a 10-digit mobile number

import re

mobile = input("Enter mobile number: ")

pattern = r'^[0-9]{10}$'

if re.match(pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")