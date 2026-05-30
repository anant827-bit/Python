from tkinter import *

root=Tk()
root.title("Ishuuuuu")
root.geometry("400x200")

l1= Label(text="This is a label.", bg="pink", fg="black", font="comicsansms 27 bold", borderwidth=8, relief=RIDGE, padx=8, pady=11)
l1.pack(anchor="se", side=BOTTOM, padx=11, pady=11, fill=X)

root.mainloop()