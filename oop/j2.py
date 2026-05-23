# Write a Program to implement Getters and Setters in a class
class Student:
    def __init__(self, name, marks):
        self.__name=name  
        self.__marks=marks

    def get_name(self):
        return self.__name
    
    def set_name(self,name):
        self.__name=name

    def get_marks(self):
        return self.__marks
    
    def set_marks(self, marks):
        if(marks>=0 and marks<=100):
            self.__marks=marks
        else:
            print("Invalid value for marks!")

s1 = Student("Anant", 8)
print("Name:", s1.get_name())
print("Marks:", s1.get_marks())

s1.set_name("Vaibhavi")
s1.set_marks(27)
print("Updated Name:", s1.get_name())
print("Updated Marks:", s1.get_marks())