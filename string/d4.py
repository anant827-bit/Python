# wap to count all letters, digits, and special symbols from a given string
str1=input("Enter a string: ")
lower=0
upper=0
digits=0
symbols=0

for char in str1:
    if char.isalpha():
        low="abcdefghijklmnopqrstuvwxyz"
        
        if char in low:
            lower+=1
        else:
            upper+=1

    elif char.isdigit():
        digits+=1
    else:
        symbols+=1

print("No. of lowercase: ", lower)
print("No. of uppercase: ", upper)
print("No. of digits: ", digits)
print("No. of special symbols: ", symbols)