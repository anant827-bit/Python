# Write a program that reads values from the user until a blank line is entered. Display the total of all of the values entered by the user (or 0.0 if the first value entered is a blank line). Complete this task using recursion. Your program may not use any loops.

def sum_rec():
    x=input("Enter a number:")
    if(x==""):
        return 0.0
    else:
        return float(x) + sum_rec()
    
total = sum_rec()
print("Sum:", total)
        