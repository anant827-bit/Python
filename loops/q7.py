# wap to find the sum of digits of a number
num=int(input("Enter a number: "));

i=1;
sum=0;
while(num!=0):
    rem=num%10;
    sum=sum+rem;
    num=num//10;

print("Sum of digits using while: ", sum);

