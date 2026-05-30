from tkinter import *
root=Tk()
root.title("Helllooo")
root.geometry("444x222")

# Important Label Funtions
# text - adds the text
# bg - background
# fg - foreground
# font - sets the font
# ("Times New Roman",20, "bold")
# padx - paddingx
# pady - paddingy
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

label=Label(text="This is a label.", bg="pink", fg="white", padx="8", pady="27", font=("comicsansms 19 bold"), borderwidth=3, relief=SUNKEN)

# Important pack options
# anchor = nw
# side = top,bottom,left,right
# fill = fill x,y
# padx, pady = padding in x and y

label.pack(side=BOTTOM,anchor="nw",fill=X, padx=27, pady=8)

root.mainloop()