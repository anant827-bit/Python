from tkinter import *
root=Tk()
root.title("Place instead of pack")
root.geometry("400x400")

l1=Label(root,text="Hello guyyyyssss", fg="black", bg="purple", font="27")
l1.place(x=89, y=89)

root.mainloop()