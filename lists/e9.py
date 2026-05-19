# wap that reads integers from the user and stores them in a list. Your program should continue reading values until the user enters 0. Then it should display all of the values entered by the user (except for the 0) in order from smallest to largest, with one value appearing on each line
numbers = []

print("Enter integers (Enter 0 to stop):")

while True:
    num = int(input())
    
    if num == 0:
        break
    else:
        numbers.append(num)

# Sort the list
numbers.sort()

print("\nNumbers in ascending order:")

for value in numbers:
    print(value)