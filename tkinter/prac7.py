from tkinter import *
root=Tk()

l1=Label(root, text="First name:", font="20")
l1.grid(row=0, column=0)

l2=Label(root, text="Last name:", font="20")
l2.grid(row=1, column=0)

l2=Label(root, text="Last name:", font="20")
l2.grid(row=1, column=1)

l2=Label(root, text="Last name:", font="20")
l2.grid(row=1, column=2)

l2=Label(root, text="Last name:", font="20")
l2.grid(row=1, column=3)

b1=Button(root, text="Submit", font="15")
b1.grid(row=2, column=0, columnspan=4)

root.mainloop()