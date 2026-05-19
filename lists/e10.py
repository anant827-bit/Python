# Wap that reads integers from the user and stores them in a list. Use 0 as a sentinel value to mark the end of the input. Once all of the values have been read your program should display them (except for the 0) in reverse order. 
numbers = []

print("Enter integers (Enter 0 to stop):")

while True:
    num = int(input())
    
    if num == 0:
        break
    else:
        numbers.append(num)

print("\nNumbers in reverse order:")

for value in reversed(numbers):
    print(value)