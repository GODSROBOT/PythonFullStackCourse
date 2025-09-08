import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.geometry("500x380")
root.title("Login Form")

# Function

def login():
    username = Username_Textbox.get()
    password = Password_Textbox.get()

    if username == "admin" and password == "password":
        messagebox.showinfo("Login Info", "Login Successful")
        status_label.config(text="Status: Logged In", fg="green")
    else:
        messagebox.showerror("Login Info", "Invalid Credentials")
        status_label.config(text="Status: Login Failed", fg="red")

# Username
Username_Label = tk.Label(root, text="Enter Username")
Username_Label.pack(anchor=tk.W, padx=10)

Username_Textbox = tk.Entry(root)
Username_Textbox.pack(anchor=tk.W, padx=10)

# Password
Password_Label = tk.Label(root, text="Enter Password")
Password_Label.pack(anchor=tk.W, padx=10)

Password_Textbox = tk.Entry(root, show="*")
Password_Textbox.pack(anchor=tk.W, padx=10)

# Status Label
status_label = tk.Label(root, text="Status: Not Logged In", fg="black")
status_label.pack(anchor=tk.W, padx=10, pady=10)

# Button

Button = tk.Button(root, text="Login", command=login)
Button.pack(anchor=tk.W, padx=10)

root.mainloop()