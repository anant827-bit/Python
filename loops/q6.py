# wap to count the number of digits in a number
num=int(input("Enter a nunber: "));
numcp=num;

countw=0;
while(num!=0):
    num=num//10;
    countw=countw+1;
print("Number of digits using while loop: ", countw);

num1=str(input("Enter a number: "));
countf=0;
for i in range(1,len(num1)+1):
    countf=countf+1;
print("No. of digits using for loop: ", countf);