import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width = 500, height = 500)
canvas.pack()

for i in range(0, 500, 50):
    canvas.create_line(i, 0, i, 500, fill="black")
    canvas.create_line(0, i, 500, i, fill="black")

root.mainloop()