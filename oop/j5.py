# Write a Program to illustrate multiple inheritance in Python 
class A:
    def show(self):
        print("This is class A.")
class B:
    def show(self):
        print("This is class B.")
class C(A,B):
    pass

obj = C()
obj.show()