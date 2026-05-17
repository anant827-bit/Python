# wap to check if the entered number is Armstrong or not.
num=int(input("Enter a number:"));

x=num;
sum=0;
while(x>0):
    rem=x%10;
    sum=sum+(rem*rem*rem);
    x=x//10;

print("Sum:", sum);

if(sum==num):
    print("Armstrong number.");
else:
    print("Not an Armstrong number.");

