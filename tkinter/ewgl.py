from tkinter import *
root=Tk()
root.title("Entry Widget & Grid Layout in tkinter")
root.geometry("400x400")

def getvals():
    print("Username:",uservalue.get())
    print(f"Password: {passvalue.get()}")

user=Label(root, text="Username")
password = Label(root, text="Password")
user.grid()
password.grid(row=1)

# Variable classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable=uservalue)
passentry=Entry(root, textvariable=passvalue)

userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)

b1=Button(text="Submit", bg="red", fg="white", borderwidth=6, command=getvals)
b1.grid()

root.mainloop()