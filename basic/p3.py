# wap to swap two numbers & print the numbers before and after swapping
a= int(input("Enter first number:"));
b= int(input("Enter second number:"));

print("before swapping: ", a, b);

a=a+b;
b=a-b;
a=a-b;

print("after swapping: ", a, b);