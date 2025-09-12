import tkinter as tk
from tkinter import messagebox
import mysql.connector as mysql
import json

# Database connection
try:
    print("Connecting to database...")
    db = mysql.connect(
        host="localhost",
        user="root",
        password="Root",
        database="Register_Login"
    )
    cursor = db.cursor()
    print("✅ Connected to database.")
except mysql.Error as e:
    print(f"❌ Database connection failed: {e}")
    exit()


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login/Signup App")
        self.geometry("400x300")

        # Container
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (LoginPage, SignupPage, ExportData):   # 🔹 Include ExportData
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()

        tk.Label(self, text="Login", font=("Arial", 14)).pack(pady=10)
        tk.Label(self, text="Username").pack(pady=5)
        tk.Entry(self, textvariable=self.username_var).pack(pady=5)
        tk.Label(self, text="Password").pack(pady=5)
        tk.Entry(self, textvariable=self.password_var, show="*").pack(pady=5)

        tk.Button(self, text="Login", command=self.login_user).pack(pady=10)
        tk.Button(self, text="Go to Signup",
                  command=lambda: controller.show_frame(SignupPage)).pack(pady=5)
        tk.Button(self, text="Go to Export",
                  command=self.go_to_export).pack(pady=5)

    def login_user(self):
        username = self.username_var.get()
        password = self.password_var.get()

        if not username or not password:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            messagebox.showinfo("Success", f"✅ Welcome {username}!")
        else:
            messagebox.showerror("Error", "❌ Invalid credentials.")

    def go_to_export(self):
        """Pass login data to Export page"""
        username = self.username_var.get()
        password = self.password_var.get()

        # Update ExportData frame with current credentials
        export_page = self.controller.frames[ExportData]
        export_page.set_data(username, password)

        self.controller.show_frame(ExportData)


class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        self.new_username_var = tk.StringVar()
        self.new_password_var = tk.StringVar()
        self.confirm_password_var = tk.StringVar()

        tk.Label(self, text="Signup", font=("Arial", 14)).pack(pady=10)
        tk.Label(self, text="New Username").pack(pady=5)
        tk.Entry(self, textvariable=self.new_username_var).pack(pady=5)
        tk.Label(self, text="New Password").pack(pady=5)
        tk.Entry(self, textvariable=self.new_password_var, show="*").pack(pady=5)
        tk.Label(self, text="Confirm Password").pack(pady=5)
        tk.Entry(self, textvariable=self.confirm_password_var, show="*").pack(pady=5)

        tk.Button(self, text="Signup", command=self.signup_user).pack(pady=10)
        tk.Button(self, text="Go to Login",
        command=lambda: controller.show_frame(LoginPage)).pack(pady=5)

    def signup_user(self):
        new_username = self.new_username_var.get()
        new_password = self.new_password_var.get()
        confirm_password = self.confirm_password_var.get()

        if not new_username or not new_password or not confirm_password:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "❌ Passwords do not match!")
            return

        try:
            query = "INSERT INTO users (username, password) VALUES (%s, %s)"
            cursor.execute(query, (new_username, new_password))
            db.commit()
            messagebox.showinfo("Success", f"✅ Account created for {new_username}!")
            self.controller.show_frame(LoginPage)
        except mysql.IntegrityError:
            messagebox.showerror("Error", "❌ Username already exists!")


class ExportData(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.username = None
        self.password = None

        tk.Label(self, text="Export Data", font=("Arial", 14)).pack(pady=10)
        tk.Button(self, text="Export to JSON", command=self.to_json).pack(pady=10)
        tk.Button(self, text="Back to Login",
        command=lambda: controller.show_frame(LoginPage)).pack(pady=5)

    def set_data(self, username, password):
        """Set user data when navigating here"""
        self.username = username
        self.password = password

    def to_json(self):
        if not self.username or not self.password:
            messagebox.showerror("Error", "No user data to export!")
            return

        data = {
            "username": self.username,
            "password": self.password
        }
        with open("user_data.json", "w") as f:
            json.dump(data, f)

        messagebox.showinfo("Export", "✅ User data exported to user_data.json")


if __name__ == "__main__":
    app = App()
    app.mainloop()
