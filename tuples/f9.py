# Check if a Tuple is a Palindrome
t=(1,2,3,2,1)

t2=t[::-1]

if t2 == t:
    print("Tuple is a palindrome.")
else:
    print("Not a palindrome.")