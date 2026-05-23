# Write a Program to calculate student grade using class  
class Student:
    def __init__(self, name, marks):
        self._name=name
        self._marks=marks

    def calgrade(self):
        if self._marks>=90 and self._marks<100:
            return 'A'
        elif self._marks>=80 and self._marks<90:
            return 'B'
        elif self._marks>=70 and self._marks<80:
            return 'C'
        elif self._marks>=60 and self._marks<70:
            return 'D'
        elif self._marks>=50 and self._marks<60:
            return 'E'
        else:
            return 'F'
        
    def display(self):
        grade=self.calgrade()
        print("Name:", self._name)
        print("Marks:", self._marks)
        print("Grade:", grade)

name=input("Enter name:")
marks=int(input("Enter marks:"))

s1 = Student(name, marks)
s1.display()