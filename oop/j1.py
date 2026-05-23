# Write a Program to implement destructor and constructors using __del__() and __init__()
class Student():
    # Constructor
    def __init__(self, name):
        self.name=name
        print("Constructor called. Object created for:", self.name)

    # Destructor
    def __del__(self):
        print("Destructor called. Object deleted for:", self.name)

s1 = Student("Anant")



print("Program Finished")