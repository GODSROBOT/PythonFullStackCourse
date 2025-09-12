import tkinter as tk
from tkinter import filedialog, messagebox, colorchooser, font
from tkfontchooser import askfont
# Root Properties
root = tk.Tk()
root.title("Text Editor")
root.geometry("800x600")
root.config(bg="lightgrey")

# Functions 
def open_file():
    try:
        file_path = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:  # only proceed if user selected a file
            with open(file_path, 'r') as file:
                text_area.delete(1.0, tk.END)          # clear old content
                text_area.insert(tk.END, file.read())  # insert new content
            
            root.title(f"Text Editor - {file_path}")
            status_bar.config(text=f"Opened: {file_path}")
        else:
            status_bar.config(text="Open operation cancelled.")
    
    except Exception as e:
        messagebox.showerror("Error", f"Failed to open file:\n{e}")

def save_file():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if file_path:  # only proceed if user selected a file
            with open(file_path, 'w') as file:
                file.write(text_area.get(1.0, tk.END))
                root.title(f"Text Editor - {file_path}")
            status_bar.config(text=f"Saved: {file_path}")
    except Exception as e:
            status_bar.config(text="Save operation cancelled.")
            messagebox.showerror("Error", f"Failed to save file:\n{e}")

def clear_text():
    confirm = messagebox.askyesno("Clear Text", "Are you sure you want to clear the text area?")
    if confirm:
        text_area.delete(1.0, tk.END)
        status_bar.config(text="Cleared text area.")

def change_color():
    color = colorchooser.askcolor()[1]
    if color:
        text_area.config(fg=color)
        status_bar.config(text=f"Changed text color to {color}")

def change_font():
    font_choice = askfont(root)  # using tkfontchooser
    if font_choice:
        font_name = font_choice['family']
        font_size = font_choice['size']
        text_area.config(font=(font_name, font_size))
        status_bar.config(text=f"Changed font to {font_name} {font_size}")
def toggle_theme():
    current_bg = text_area.cget("bg")
    if current_bg == "white":
        text_area.config(bg="black", fg="white", insertbackground="white")
    else:
        text_area.config(bg="white", fg="black", insertbackground="black")
def update_status(event=None):
    text = text_area.get("1.0", "end-1c")
    words = len(text.split())
    chars = len(text)
    status_bar.config(text=f"Words: {words} Characters: {chars}")
# Main Window design

text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill=tk.BOTH)
text_area.bind("<KeyRelease>", update_status)

about_Label = messagebox.showinfo("About", "Simple Text Editor")
# Menu Bar
menu_bar = tk.Menu(root)

# File Menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Clear", command=clear_text)
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
# Edit Menu
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Change Color", command=change_color)
edit_menu.add_command(label="Change Font", command=change_font)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
# View Menu
view_menu = tk.Menu(menu_bar, tearoff=0)
view_menu.add_command(label="Toggle Theme", command=toggle_theme)
menu_bar.add_cascade(label="View", menu=view_menu)
root.config(menu=menu_bar)
# Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu(Label = "about us", )

# Status Bar
status_bar = tk.Label(root, text="Welcome to Text Editor", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()