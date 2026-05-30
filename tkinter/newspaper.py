from tkinter import *
from PIL import Image, ImageTk

root=Tk()
root.title("Newspaper")
root.geometry("1000x600")

f1=Frame(root, width=1000, height=11)

l1=Label(f1, text="Times Of India", fg="black", bg="white", font="TimesNewRoman 28 bold")
l1.pack()
l2=Label(f1, text="19 May 2026, Tuesday", fg="black", bg="white", font="TimesNewRoman 20 bold")
l2.pack()


f2=Frame(root, width=999, height=20).pack()


head1=Label(f2, text="Hottest & Cuttest Girl Ever in the history of Humankind", fg="black", bg="white", font="comicsansms 20 bold")
head1.pack()
img1=Image.open(r"D:\EDITS\catt\WhatsApp Image 2026-05-09 at 2.43.30 PM.jpeg")
photo1=ImageTk.PhotoImage(img1)

i1=Label(f2, image=photo1)
i1.pack()

head2=Label(f2, text="Did You Know?", fg="black", bg="white", font="comicsansms 20 bold")
head2.pack()

head3=Label(f2, text="Temperature rising day-by-day", fg="black", bg="white", font="comicsansms 20 bold")
head3.pack()

root.mainloop()