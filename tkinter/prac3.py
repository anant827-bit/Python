from tkinter import *
root=Tk()
root.title("Python Window")
root.geometry("400x600")

exp = Label(root, text="Explorer", fg="Black", bg="red", font="TimesNewRoman 27 italic", padx=8, pady=11)
exp.pack(side=LEFT, fill=Y)

ter = Label(root, text="Terminal", fg="white", bg="pink", font="comicsansms 22 italic", padx=8, pady=11)
ter.pack(side=TOP, fill=X)

root.mainloop()