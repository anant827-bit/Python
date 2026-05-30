from tkinter import *
root=Tk()
root.title("Canvas in tkinter")
width=800
height=400

root.geometry(f"{width}x{height}")

canvas=Canvas(root, width=width, height=height, bg="lightgrey")
canvas.pack()

canvas.create_line(0,0,800,400, fill="red")
canvas.create_rectangle(10,10,80,90, fill="blue")
canvas.create_oval(100,150,200,300, fill="yellow")
canvas.create_polygon(50,60,170,80,100,110,150,180)
canvas.create_arc(200,200,300,350,start=0, extent=45, fill="pink")
canvas.create_text(400,200, text="Ishu pagal h", fill="purple", font="Arial 27 bold")

root.mainloop()