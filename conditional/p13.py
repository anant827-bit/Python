# wap to allot grades to students according to number.
marks=int(input("Enter marks of the student: "));

if(marks>=90):
    print("Grade A");
if(marks>=75 and marks<90):
    print("Grade B");
if(marks>=60 and marks<75):
    print("Grade C");
if(marks>=40 and marks<60):
    print("Grade D");
else:
    print("Fail");