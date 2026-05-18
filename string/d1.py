# wap to create, concatenate, and print a string and accessing sub-string from a given string.
string1=str(input("Enter a string: "));

ans=str(input("Do you want to add/concatenate another string?(Y/N)"));
if(ans=='Y' or ans=='y'):
    string2=str(input("Enter another string you want to concatenate: "));
    print(string1+string2);
else:
    print("Thank You.");

ans1=str(input("Do you want to access sub-string from string1?(Y/N)"));
if(ans=='Y' or ans=='y'):
    a=int(input("Enter start: "));
    b=int(input("Enter finish: "));
    print(string1[a:b]);
else:
    print("Thank You.");
    
