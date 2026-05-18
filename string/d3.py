# wap to check whether a string is palindrome or not

text = input("Enter a string: ")

# Convert to lowercase
text = text.lower()

# Reverse the string
reverse_text = text[::-1]

if text == reverse_text:
    print("The string is a Palindrome.")
else:
    print("The string is NOT a Palindrome.")
