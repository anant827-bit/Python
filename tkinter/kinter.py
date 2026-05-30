from tkinter import *

root=Tk()

root.geometry("827x827")

# width,height
root.minsize(200,400)
root.maxsize(1200,900)

hello = Label(text="This is a label")
hello.pack()
root.mainloop()
