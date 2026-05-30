# photo=PhotoImage(file="Desktop\img3.jpeg")

# label=Label(root, image=photo)
# label.pack()
# root.mainloop()

from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("image")

img = Image.open(r"D:\EDITS\25.04.2026\1c.jpg")
photo = ImageTk.PhotoImage(img)

lab1 = Label(root, image=photo)
lab1.pack()

root.mainloop()