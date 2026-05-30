from tkinter import *
root=Tk()
root.title("Entry widget and Grid Layout")
root.geometry("600x600")

def getvals():
    print("Username:",uservalue.get())
    print("Password:", passvalue.get())

l1=Label(root, text="Username", fg="black", font="comicsansms 27 bold")
l1.grid(row=0, column=0)

l2=Label(root, text="Password", fg="black", font="comicsansms 27 bold")
l2.grid(row=1, column=0)

uservalue=StringVar()
passvalue=StringVar()

userentry=Entry(root, textvariable=uservalue)
passentry=Entry(root, textvariable=passvalue)

userentry.grid(row=0, column=1)
passentry.grid(row=1, column=1)

but1= Button(root, text="Submit", fg="black", bg="lightgrey", font="TimesNewRoman 20 italic", command=getvals)
but1.grid(row=2, column=0)
root.mainloop()