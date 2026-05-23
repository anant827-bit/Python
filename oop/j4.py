# Write a Program to illustrate single inheritance in Python
class A:
    def show(self):
        print("This is class A.")
class B(A):
    pass

obj = B()
obj.show()