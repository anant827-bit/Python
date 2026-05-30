from tkinter import *
root=Tk()
root.title("Canvas in tkinter")

canvas_width=800
canvas_height=400
root.geometry(f"{canvas_width}x{canvas_height}")

canva=Canvas(root, width=canvas_width, height=canvas_height)
canva.pack()

canva.create_line(0,0,800,400,fill="red")
canva.create_oval(60,60,150,144, fill="lightgreen")
canva.create_rectangle(150,140,220,250,fill="pink")
canva.create_arc(200,300,360,370,start=0,extent=270,fill="orange")
canva.create_text(
    200,
    200, 
    text="Big Guns",
    fill="black", 
    font="Arial 27 bold"
)

root.mainloop()