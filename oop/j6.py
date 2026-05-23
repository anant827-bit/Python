# Write a Program to illustrate multilevel inheritance in Python 
class A:
    def show(self):
        print("This is class A.")

class B(A):
    pass

class C(B):
    pass

obj = C()
obj.show()