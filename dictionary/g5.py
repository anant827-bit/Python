# Two words are anagrams if they contain all of the same letters, but in a different order. For example, “evil” and “live” are anagrams because each contains one ‘e’, one ‘I’, one ‘l’, and one ‘v’. Create a program that reads two strings from the user, determines whether or not they are anagrams, and reports the result. 

str1 = input("Enter first word: ")
str2 = input("Enter second word: ")

# Convert to dictionary with character counts
d1 = {}
d2 = {}

for ch in str1:
    d1[ch] = d1.get(ch, 0) + 1

for ch in str2:
    d2[ch] = d2.get(ch, 0) + 1

if d1 == d2:
    print("The words are Anagrams")
else:
    print("The words are NOT Anagrams") 

l1=list(str1.upper())
l2=list(str2.upper())
if l1.sort()==l2.sort():
    print("Anagrams")
else:
    print("Not anagrams.")