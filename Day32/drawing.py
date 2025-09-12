import tkinter as tk
from tkinter import colorchooser

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing app")
        self.root.geometry("800x600")
        self.brush_color = "black"
        self.brush_size = 3

        # Toolbar
        toolbar = tk.Frame(root, pady=5)
        toolbar.pack()

        tk.Button(toolbar, text="Brush Color", command=self.choose_color).pack(side=tk.LEFT, padx=5)
        tk.Button(toolbar, text="Clear Canvas", command=self.clear_canvas).pack(side=tk.LEFT, padx=5)

        size_slider = tk.Scale(toolbar, from_=1, to=10, orient=tk.HORIZONTAL, label="Brush Size")
        size_slider.set(self.brush_size)
        size_slider.pack(side=tk.LEFT)
        size_slider.bind("<Motion>", lambda e: self.update_brush_size(size_slider.get()))

        # Canvas
        self.Canvas = tk.Canvas(root, bg="white", width=600, height=400, scrollregion=(0, 0, 1000, 1000))
        self.Canvas.pack(fill=tk.BOTH, expand=True)

        # Bind painting
        self.Canvas.bind("<B1-Motion>", self.paint)

    # --- Methods (must be outside __init__) ---
    def choose_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color

    def update_brush_size(self, size):
        self.brush_size = int(size)

    def clear_canvas(self):
        self.Canvas.delete("all")

    def paint(self, event):
        x1, y1 = (event.x - self.brush_size), (event.y - self.brush_size)
        x2, y2 = (event.x + self.brush_size), (event.y + self.brush_size)
        self.Canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color)

root = tk.Tk()
app = DrawingApp(root)
root.mainloop()
