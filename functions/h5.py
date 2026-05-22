# Write a function that generates a random password. The password should have a random length of between 7 and 10 characters. Each character should be randomly selected from positions 33 to 126 in the ASCII table. Your function will not take any parameters. It will return the randomly generated password as its only result.

def password():
    import random
    length = random.randint(7, 10)
    str = ""
    for i in range(length):
        ch = random.randint(33,126)
        char = chr(ch)
        str = str + char

    print("Password:", str)

password()