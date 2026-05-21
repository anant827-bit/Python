# Write a Program that determines and displays the number of unique characters in a string entered by the user. For example, “Hello, World!” has 10 unique characters while “zzz” has only one unique character. Use a dictionary to solve this problem.

string = input("Enter a string: ")

char_dict = {}

for ch in string:
    char_dict[ch] = 1

print("Unique characters:", len(char_dict))
print(char_dict)