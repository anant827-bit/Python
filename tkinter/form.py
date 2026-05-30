from tkinter import *
root=Tk()
root.title("Registration Form")
root.minsize(1200,1200)

def getvals():
    print("Button clicked")
    with open(r"C:\Users\user\OneDrive\Desktop\JECRCU\SEM 4\Python\tkinter\record.txt", "a") as f:
        f.write(f"{namevalue.get(), phonevalue.get(), gendervalue.get(), emergencyvalue.get(), paymentvalue.get(),foodvalue.get()}\n")

Label(root,text="Welcome to Harry Travels", font="comicsansms 27 bold",bg="pink", fg="white").grid(row=0, column=4)

name=Label(root,text="Full Name", fg="black", font="comicsansms 20 italic")
phone=Label(root,text="Phone", fg="black", font="comicsansms 20 italic")
gender=Label(root,text="Gender", fg="black", font="comicsansms 20 italic")
emergency=Label(root,text="Emergency Number", fg="black", font="comicsansms 20 italic")
payment=Label(root,text="Payment Method", fg="black", font="comicsansms 20 italic")

name.grid(row=1, column=0)
phone.grid(row=2, column=0)
gender.grid(row=3, column=0)
emergency.grid(row=4, column=0)
payment.grid(row=5, column=0)

namevalue=StringVar()
phonevalue=StringVar()
gendervalue=StringVar()
emergencyvalue=StringVar()
paymentvalue=StringVar()
foodvalue=IntVar()

food=Checkbutton(root, text="Want to prebook your meals?", fg="black", font="comicsansms 15 italic", variable=foodvalue)
food.grid(row=6,column=4)

nameentry=Entry(root, textvariable=namevalue)
phonentry=Entry(root, textvariable=phonevalue)
genderentry=Entry(root, textvariable=gendervalue)
emergencyentry=Entry(root, textvariable=emergencyvalue)
paymententry=Entry(root, textvariable=paymentvalue)

nameentry.grid(row=1, column=1)
phonentry.grid(row=2, column=1)
genderentry.grid(row=3, column=1)
emergencyentry.grid(row=4, column=1)
paymententry.grid(row=5, column=1)

submit=Button(root,text="Submit your response", font="comicsansms 20 bold", fg="white", bg="lightgrey", padx=2, pady=2, command=getvals)
submit.grid(row=7, column=4)

root.mainloop()