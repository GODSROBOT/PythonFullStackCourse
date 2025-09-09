import tkinter as tk

import PIL
from PIL import Image, ImageTk
root = tk.Tk()
root.title("Photo Image")

# Load the image
image = Image.open("D:/V-TechnoSolutions/PythonFullstack/Day29/png.png")
photo = ImageTk.PhotoImage(image)

# Create a label to display the image
Label = tk.Label(root, image=photo)
Label.pack(pady=20)


root.mainloop()