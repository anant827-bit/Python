# Write a python program that prints prime numbers less than 20. 
range=int(input("Enter a range: "));

i=2;
while(i<=range):
    j=2;
    key=1;
    while(j<=i/2):
        if(i%j==0):
            key=0;
            break;
        j=j+1;

    if(key==1):
        print("", i);

    i=i+1;