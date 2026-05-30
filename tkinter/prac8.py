import tkinter as tk

# 1. Initialize the main window
root = tk.Tk()
root.title("Canvas Text Test")

# 2. Create canvas with a gray background to see white/black text easily
canvas = tk.Canvas(root, width=400, height=400, bg="lightgray")
canvas.pack()

# 3. Add text exactly in the center (X=200, Y=200)
# Use 'anchor=tk.CENTER' to ensure it builds outward from the middle
canvas.create_text(
    200, 
    200, 
    text="If you see this, it works!", 
    fill="black", 
    font=("Arial", 16, "bold"),
    anchor=tk.CENTER
)

# 4. Start the application loop (prevents the window from instantly closing)
root.mainloop()
