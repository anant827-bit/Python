from tkinter import *
root=Tk()
root.title("Frames in tkinter")
root.geometry("827x827")

f1 = Frame(root, bg="blue", borderwidth=8, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y, pady=27)

l1 = Label(f1, text="This is label 1 in frame 1.", fg="white", bg="pink")
l1.pack(padx=27, pady=8)

f2 = Frame(root, bg="green", borderwidth=8, relief=RAISED)
f2.pack(side=TOP, fill=X)

l2 = Label(f2, text="This is label 2 in frame 2.", fg="white", bg="pink")
l2.pack(padx=27, pady=8)

root.mainloop()