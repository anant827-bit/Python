from tkinter import *
root=Tk()
root.title("Button in tkinter")
root.geometry("400x400")

def hello():
    print("kuch nahiiiii")

f1=Frame(root, bg="purple", borderwidth=8, relief=GROOVE)
f1.pack()

l1=Label(f1,text="kuch samajh nahi aa raha", fg="white", bg="black")
l1.pack()

b1= Button(f1, bg="red", text="main kya karun?", command=hello)
b1.pack()

root.mainloop()