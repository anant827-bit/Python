from tkinter import *
root=Tk()
root.title("Buttons in tkinter")
root.geometry("400x400")

def show():
    print("ACK")

f1=Frame(root, bg="lightgrey", borderwidth=6, relief=RIDGE)
f1.pack()

l1=Label(f1, text="ISHU you are the sweetest bbg :)", fg="white", bg="pink", font="italic 27")
l1.pack()

b1= Button(f1, text="Click if you agree.", bg="grey", fg="black", command=show)
b1.pack()

root.mainloop()