from tkinter import *
import matplotlib.pyplot as plt
import numpy as np

def plot_graph():
    u=float(entry_u.get())
    a=float(entry_a.get())

    t=np.linspace(0,10,100)
    v=u+a*t
    s=u*t + 0.5 * a * (t**2)

    # velocity-time graph
    plt.figure(figsize=(6,4))
    plt.plot(t, v)
    plt.xlabel("Time")
    plt.ylabel("Velocity")
    plt.title("Velocity-Time Graph")
    plt.show()

root=Tk()
root.title("Equations of Motion")

Label1=Label(root, text="Intial Velocity(u)").grid(row=0, column=0)
Label2=Label(root, text="Acceleration(a)").grid(row=1, column=0)

u_value=DoubleVar
a_value=DoubleVar

entry_u=Entry(root, textvariable=u_value)
entry_u.grid(row=0, column=1)
entry_a=Entry(root, textvariable=a_value)
entry_a.grid(row=1, column=1)

but=Button(root, text="Submit", command=plot_graph).grid(row=2, column=0, columnspan=2)

root.mainloop()