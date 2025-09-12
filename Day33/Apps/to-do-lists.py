import tkinter as tk
from tkinter import ttk, messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.geometry("400x500")

        # Style
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TButton", font=("Segoe UI", 10), padding=6)
        style.configure("Treeview", font=("Segoe UI", 10), rowheight=25)
        style.configure("Treeview.Heading", font=("Segoe UI", 11, "bold"))
        # Entry Field
        self.task_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.task_var, width=40).pack(pady=10)

        # Buttons
        button_frame = ttk.Frame(root)
        button_frame.pack(pady=5)

        ttk.Button(button_frame, text="Add Task", command=self.add_task).pack(side="left", padx=5)
        ttk.Button(button_frame, text="Remove Task", command=self.remove_task).pack(side="left", padx=5)

        # Treeview for tasks
        self.tree = ttk.Treeview(root, columns=("Task",), show="headings", selectmode="browse")
        self.tree.heading("Task", text="Task")
        self.tree.column("Task", width=380, anchor="w")
        self.tree.pack(fill="both", expand=True, pady=10)

    def add_task(self):
        task = self.task_var.get().strip()
        if task:
            self.tree.insert("", "end", values=(task,))
            self.task_var.set("")
        else:
            messagebox.showwarning("Empty Task", "Please enter a task.")

    def remove_task(self):
        selected_item = self.tree.selection()
        if selected_item:
            self.tree.delete(selected_item)
        else:
            messagebox.showwarning("No Selection", "Please select a task to remove.")


# ✅ Run only once
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
