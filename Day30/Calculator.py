# Calculator using the Tkinter library in Python
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("400x500")
root.title("Calculator")
root.config(bg="lightgrey")

# Buttons

Buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+"
]

# Entry widget to display calculations
entry = tk.Entry(root, width=16, font=('Arial', 24), borderwidth=1, relief="solid")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.focus_set()
current_input = ""

# Button click event handler
def button_click(event):
    global current_input
    button_text = event.widget.cget("text")

    if button_text == 'C':
        current_input = ""
        entry.delete(0, tk.END)
    elif button_text == '=':
        try:
            result = str(eval(current_input))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
            current_input = result
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
            current_input = ""
            entry.delete(0, tk.END)
    else:
        current_input += button_text
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_input)

# Create buttons and place them in the grid
row_val = 1
col_val = 0
for button in Buttons:
    btn = tk.Button(root, text=button, width=5, height=2, font=('Arial', 18))
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    btn.bind("<Button-1>", button_click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()