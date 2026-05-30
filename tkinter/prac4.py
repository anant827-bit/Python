from tkinter import *
root=Tk()
root.title("Frames in tkinter")
root.geometry("800x800")

f1=Frame(root, bg="lightgreen", padx=8, pady=11)
f1.pack(side=LEFT, fill=Y)

l1=Label(f1, text="This is label 1 in frame 1.", fg="white", bg="pink")
l1.pack()

f2= Frame(root, bg="purple", borderwidth=8, relief=SUNKEN, padx=8, pady=11)
f2.pack(side=LEFT, fill=Y)

l2=Label(f2, text="Tryin to do better", fg="blue", font="comicsansms 27 italic")
l2.pack(anchor="sw",side="bottom")

root.mainloop()