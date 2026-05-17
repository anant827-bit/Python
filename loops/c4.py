# Write a Program to check whether a number is palindrome or not.

num=int(input("Enter a number: "));
x=num;
sum=0;
while(num > 0):
    rem=num%10;
    sum = sum*10 + rem;
    num = num//10;

if(x==sum):
    print("Palindrome number.");
else:
    print("Not a palindrome number.");