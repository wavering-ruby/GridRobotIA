import tkinter as tk

root = tk.Tk()
canvas = tk.Canvas(root, width=500, height=500)
canvas.pack()

cell_size = 50  # Tamanho das células

for i in range(0, 500, cell_size):
    for j in range(0, 500, cell_size):
        # color = "#ADD8E6" if (i // cell_size + j // cell_size) % 2 == 0 else "#FFFFFF"
        canvas.create_rectangle(i, j, i + cell_size, j + cell_size, fill="#FFFFFF", outline="black")

root.mainloop()