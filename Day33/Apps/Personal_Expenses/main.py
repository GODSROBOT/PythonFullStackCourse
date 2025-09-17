# Personal Expenses App (with ttkbootstrap theme + full fixes)
import db as database
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
import pandas as pd
import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# ==============================
# Main App with Theme + Navbar
# ==============================
class App(ttk.Window):
    def __init__(self):
        super().__init__(themename="darkly")  # 🎨 Themes: flatly, darkly, cyborg, superhero, solar
        self.title("Personal Expenses App")
        self.geometry("1000x700")


        self.current_user = None
        self.user_var = ttk.StringVar(value="Logged in as: None")

        # Container for frames
        self.container = ttk.Frame(self)
        self.container.pack(fill="both", expand=True)
        self.frames = {}

        for F in (LoginPage, SignupPage, DashboardPage, AddExpensePage, ViewExpensesPage, ExportData, AddAccountPage, AddLoanPage, ViewAccountsPage, ViewLoansPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(LoginPage)

    def show_frame(self, page_class):
        frame = self.frames[page_class]
        frame.tkraise()
        if hasattr(frame, "refresh_data"):
            frame.refresh_data()
        if hasattr(self, "user_label"):
            self.refresh_user_label()

    def add_navbar(self, parent):
        """Reusable navbar for logged-in pages"""
        navbar = ttk.Frame(parent, bootstyle="secondary")
        navbar.pack(fill="x")

        ttk.Button(navbar, text="Dashboard", bootstyle="primary-outline",
        command=lambda: self.show_frame(DashboardPage)).pack(side="left", padx=5, pady=5)
        ttk.Button(navbar, text="Accounts", bootstyle="info-outline",
        command=lambda: self.show_frame(AddAccountPage)).pack(side="left", padx=5, pady=5)
        ttk.Button(navbar, text="View Accounts", bootstyle="info-outline",
        command=lambda: self.show_frame(ViewAccountsPage)).pack(side="left", padx=5, pady=5)
        ttk.Button(navbar, text="Add Expenses", bootstyle="success-outline",
        command=lambda: self.show_frame(AddExpensePage)).pack(side="left", padx=5, pady=5)
        ttk.Button(navbar, text="View Expenses", bootstyle="success-outline",
        command=lambda: self.show_frame(ViewExpensesPage)).pack(side="left", padx=5, pady=5)
        ttk.Button(navbar, text="Loans", bootstyle="warning-outline",
        command=lambda: self.show_frame(AddLoanPage)).pack(side="left", padx=5, pady=5)
        ttk.Button(navbar, text="View Loans", bootstyle="warning-outline",
        command=lambda: self.show_frame(ViewLoansPage)).pack(side="left", padx=5, pady=5)
        ttk.Button(navbar, text="Export", bootstyle="secondary-outline",
        command=lambda: self.show_frame(ExportData)).pack(side="left", padx=5, pady=5)

        # Current user label
        self.user_label = ttk.Label(navbar, textvariable=self.user_var, font=("Arial", 10, "italic"), bootstyle="danger")
        self.user_label.pack(side="right", padx=5)
        ttk.Button(navbar, text="Logout", bootstyle="danger-outline", command=self.logout).pack(side="right", padx=5, pady=5)

    def logout(self):
        self.current_user = None
        self.refresh_user_label()
        self.show_frame(LoginPage)

    def refresh_user_label(self):
        if hasattr(self, "user_var"):
            self.user_var.set(f"Logged in as: {self.current_user or 'None'}")


# ==============================
# Login Page
# ==============================
class LoginPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.username_var = ttk.StringVar()
        self.password_var = ttk.StringVar()

        ttk.Label(self, text="🔐 Login", font=("Helvetica", 18, "bold")).pack(pady=20)
        ttk.Label(self, text="Username:").pack(pady=5)
        ttk.Entry(self, textvariable=self.username_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="Password:").pack(pady=5)
        ttk.Entry(self, textvariable=self.password_var, bootstyle="info", show="*", width=30).pack(pady=5)

        ttk.Button(self, text="Login", bootstyle="success", command=self.login_user).pack(pady=10)
        ttk.Button(self, text="Go to Signup", bootstyle="secondary",
        command=lambda: controller.show_frame(SignupPage)).pack()

    def login_user(self):
        username = self.username_var.get()
        password = self.password_var.get()
        if not username or not password:
            messagebox.showerror("Error", "Please enter both username and password.")
            return
        if database.login_user(username, password):
            messagebox.showinfo("Success", "Login successful!")
            self.controller.current_user = username
            self.controller.refresh_user_label()
            self.controller.show_frame(DashboardPage)
        else:
            messagebox.showerror("Error", "Invalid username or password.")


# ==============================
# Signup Page
# ==============================
class SignupPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.email_var = ttk.StringVar()
        self.username_var = ttk.StringVar()
        self.password_var = ttk.StringVar()

        ttk.Label(self, text="📝 Signup", font=("Helvetica", 18, "bold")).pack(pady=20)
        ttk.Label(self, text="Email:").pack(pady=5)
        ttk.Entry(self, textvariable=self.email_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="Username:").pack(pady=5)
        ttk.Entry(self, textvariable=self.username_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="Password:").pack(pady=5)
        ttk.Entry(self, textvariable=self.password_var, bootstyle="info", show="*", width=30).pack(pady=5)

        ttk.Button(self, text="Signup", bootstyle="success", command=self.signup_user).pack(pady=10)
        ttk.Button(self, text="Go to Login", bootstyle="secondary",
        command=lambda: controller.show_frame(LoginPage)).pack()

    def signup_user(self):
        if database.signup_user(self.username_var.get(), self.email_var.get(), self.password_var.get()):
            messagebox.showinfo("Success", "Signup successful! Please login.")
            self.controller.show_frame(LoginPage)
        else:
            messagebox.showerror("Error", "Username or email already exists.")


# ==============================
# Dashboard Page
# ==============================
class DashboardPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        controller.add_navbar(self)


        ttk.Label(self, text="📊 Dashboard", font=("Helvetica", 18, "bold")).pack(pady=10)

        # Stats labels
        self.total_expenses_label = ttk.Label(self, text="Total Expenses: 0", font=("Arial", 12, "bold"))
        self.total_expenses_label.pack()
        self.total_loans_label = ttk.Label(self, text="Total Loans: 0", font=("Arial", 12, "bold"))
        self.total_loans_label.pack()
        self.total_balance_label = ttk.Label(self, text="Total Account Balance: 0", font=("Arial", 12, "bold"))
        self.total_balance_label.pack()

        # Matplotlib figure with subplots
        self.figure = Figure(figsize=(8, 4), dpi=100)
        self.ax_expenses = self.figure.add_subplot(121)
        self.ax_loans = self.figure.add_subplot(122)
        self.canvas = FigureCanvasTkAgg(self.figure, self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

    def refresh_data(self):
        # Fetch data
        expenses = database.get_expenses(self.controller.current_user)
        loans = database.get_loans(self.controller.current_user)
        accounts = database.get_accounts(self.controller.current_user)

        total_exp = sum(float(x["amount"]) for x in expenses) if expenses else 0
        total_loan = sum(float(x["amount"]) for x in loans) if loans else 0
        total_balance = sum(float(x["balance"]) for x in accounts) if accounts else 0

        # Update stats
        self.total_expenses_label.config(text=f"Total Expenses: {total_exp}")
        self.total_loans_label.config(text=f"Total Loans: {total_loan}")
        self.total_balance_label.config(text=f"Total Account Balance: {total_balance}")

        # Clear axes
        self.ax_expenses.clear()
        self.ax_loans.clear()

        # Expenses by category
        if expenses:
            df_exp = pd.DataFrame(expenses)
            cat_summary = df_exp.groupby("category")["amount"].sum()
            self.ax_expenses.pie(cat_summary, labels=cat_summary.index, autopct="%1.1f%%", startangle=90)
        self.ax_expenses.set_title("Expenses by Category")

        # Loans distribution
        if loans:
            df_loans = pd.DataFrame(loans)
            loan_types = df_loans.groupby("loan_type")["amount"].sum()
            self.ax_loans.pie(loan_types, labels=loan_types.index, autopct="%1.1f%%", startangle=90)
        self.ax_loans.set_title("Loans Distribution")

        self.figure.tight_layout()
        self.canvas.draw()


# ==============================
# Add Expense Page
# ==============================
class AddExpensePage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        controller.add_navbar(self)

        self.amount_var = ttk.DoubleVar()
        self.category_var = ttk.StringVar()
        self.date_var = ttk.StringVar()
        self.description_var = ttk.StringVar()

        ttk.Label(self, text="➕ Add Expense", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(self, text="Amount:").pack(pady=5)
        ttk.Entry(self, textvariable=self.amount_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="Category:").pack(pady=5)
        ttk.Combobox(self, textvariable=self.category_var,
        values=["Subscription", "Groceries", "Shopping", "Bills", "Extra Expenses"], width=27).pack(pady=5)
        ttk.Label(self, text="Date (YYYY-MM-DD):").pack(pady=5)
        ttk.Entry(self, textvariable=self.date_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="Description (optional):").pack(pady=5)
        ttk.Entry(self, textvariable=self.description_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Button(self, text="Add Expense", bootstyle="success", command=self.add_expense).pack(pady=10)

    def add_expense(self):
        amount = self.amount_var.get()
        category = self.category_var.get()
        date = self.date_var.get()
        description = self.description_var.get()

        if not amount or not category or not date:
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        try:
            datetime.datetime.strptime(date, '%Y-%m-%d')
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use YYYY-MM-DD.")
            return

        if database.add_expense(self.controller.current_user, amount, category, date, description):
            messagebox.showinfo("Success", "Expense added successfully!")
            self.amount_var.set(0.0)
            self.category_var.set("")
            self.date_var.set("")
            self.description_var.set("")
        else:
            messagebox.showerror("Error", "Failed to add expense.")


# ==============================
# View Expenses Page
# ==============================
class ViewExpensesPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        controller.add_navbar(self)

        ttk.Label(self, text="📂 View Expenses", font=("Arial", 16, "bold")).pack(pady=10)
        self.tree = ttk.Treeview(self, columns=("ID", "Amount", "Category", "Date", "Description"), show='headings')
        for col in ("ID", "Amount", "Category", "Date", "Description"):
            self.tree.heading(col, text=col)
        self.tree.pack(pady=10, fill="both", expand=True)

        ttk.Button(self, text="Delete Selected Expense", bootstyle="danger", command=self.delete_expense).pack(pady=5)

    def refresh_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        data = database.get_expenses(self.controller.current_user)
        if data:
            for row in data:
                self.tree.insert("", "end",
                    values=(row['expense_id'], row['amount'], row['category'], row['expense_date'], row.get('description', "")))
    def delete_expense(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select an expense to delete")
            return
        expense_id = self.tree.item(selected[0])["values"][0]
        if database.delete_expense(expense_id):
            messagebox.showinfo("Success", "Expense deleted!")
            self.refresh_data()
        else:
            messagebox.showerror("Error", "Failed to delete expense.")
# ==============================
# Add Loan Page
# ==============================
class AddLoanPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        controller.add_navbar(self)

        self.loan_type_var = ttk.StringVar()
        self.amount_var = ttk.DoubleVar()
        self.interest_var = ttk.DoubleVar()
        self.start_date_var = ttk.StringVar()
        self.end_date_var = ttk.StringVar()

        ttk.Label(self, text="🏦 Add Loan", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(self, text="Loan Type:").pack(pady=5)
        ttk.Entry(self, textvariable=self.loan_type_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="Amount:").pack(pady=5)
        ttk.Entry(self, textvariable=self.amount_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="Interest Rate (%):").pack(pady=5)
        ttk.Entry(self, textvariable=self.interest_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="Start Date (YYYY-MM-DD):").pack(pady=5)
        ttk.Entry(self, textvariable=self.start_date_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="End Date (YYYY-MM-DD):").pack(pady=5)
        ttk.Entry(self, textvariable=self.end_date_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Button(self, text="Add Loan", bootstyle="warning", command=self.add_loan).pack(pady=10)

    def add_loan(self):
        username = self.controller.current_user
        accounts = database.get_user_accounts(username)
        if not accounts:
            messagebox.showerror("Error", "Please create an account first.")
            return

        account_id = accounts[0]['account_id']  # use first account for now
        success = database.add_loan(
            account_id,
            self.loan_type_var.get(),
            self.amount_var.get(),
            self.interest_var.get(),
            self.start_date_var.get(),
            self.end_date_var.get()
        )

        if success:
            messagebox.showinfo("Success", "Loan added successfully!")
        else:
            messagebox.showerror("Error", "Failed to add loan.")


# =============================
# Accounts Page
# =============================
class AddAccountPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        controller.add_navbar(self)

        self.account_name_var = ttk.StringVar()
        self.account_type_var = ttk.StringVar()
        self.balance_var = ttk.DoubleVar()

        ttk.Label(self, text="🏦 Add Account", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Label(self, text="Account Name:").pack(pady=5)
        ttk.Entry(self, textvariable=self.account_name_var, bootstyle="info", width=30).pack(pady=5)
        ttk.Label(self, text="Account Type:").pack(pady=5)
        ttk.Combobox(self, textvariable=self.account_type_var,
        values=["checking", "savings", "credit", "investment"], width=27).pack(pady=5)
        ttk.Label(self, text="Balance:").pack(pady=5)
        ttk.Entry(self, textvariable=self.balance_var, bootstyle="info", width=30).pack(pady=5)

        ttk.Button(self, text="Add Account", bootstyle="info", command=self.add_account).pack(pady=10)

    def add_account(self):
        username = self.controller.current_user
        user = database.get_user(username)
        if not user:
            messagebox.showerror("Error", "User not found.")
            return

        user_id = user['user_id']
        success = database.add_account(
            user_id,
            self.account_name_var.get(),
            self.account_type_var.get(),
            self.balance_var.get()
        )

        if success:
            messagebox.showinfo("Success", "Account added successfully!")
        else:
            messagebox.showerror("Error", "Failed to add account.")

# ==============================
# View Accounts Page
# ==============================
class ViewAccountsPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        controller.add_navbar(self)

        ttk.Label(self, text="🏦 Accounts Overview", font=("Arial", 16, "bold")).pack(pady=10)
        self.tree = ttk.Treeview(self, columns=("ID", "Name", "Type", "Balance"), show="headings")
        for col in ("ID", "Name", "Type", "Balance"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, pady=10)

        ttk.Button(self, text="Update Balance", bootstyle="info", command=self.update_balance).pack(pady=5)
        ttk.Button(self, text="Delete Selected Account", bootstyle="danger", command=self.delete_account).pack(pady=5)

    def refresh_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        accounts = database.get_accounts(self.controller.current_user)
        for acc in accounts:
            self.tree.insert("", "end", values=(acc["account_id"], acc["account_name"], acc["account_type"], acc["balance"]))

    def update_balance(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select an account to update")
            return
        account_id = self.tree.item(selected[0])["values"][0]
        new_balance = ttk.simpledialog.askfloat("Update Balance", "Enter new balance:")
        if new_balance is not None:
            if database.update_account(account_id, new_balance):
                messagebox.showinfo("Success", "Balance updated!")
                self.refresh_data()

    def delete_account(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select an account to delete")
            return
        account_id = self.tree.item(selected[0])["values"][0]
        if database.delete_account(account_id):
            messagebox.showinfo("Success", "Account deleted!")
            self.refresh_data()
        else:
            messagebox.showerror("Error", "Failed to delete account.")
# ==============================
# View Loans Page
# ==============================
class ViewLoansPage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        controller.add_navbar(self)

        ttk.Label(self, text="💳 Loans Overview", font=("Arial", 16, "bold")).pack(pady=10)
        self.tree = ttk.Treeview(self, columns=("ID", "Type", "Amount", "Interest", "Start", "End"), show="headings")
        for col in ("ID", "Type", "Amount", "Interest", "Start", "End"):
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, pady=10)

        ttk.Button(self, text="Update Loan", bootstyle="warning", command=self.update_loan).pack(pady=5)
        ttk.Button(self, text="Delete Selected Loan", bootstyle="danger", command=self.delete_loan).pack(pady=5)

    def refresh_data(self):
        for row in self.tree.get_children():
            self.tree.delete(row)
        loans = database.get_loans(self.controller.current_user)
        for loan in loans:
            self.tree.insert("", "end", values=(loan["loan_id"], loan["loan_type"], loan["amount"], loan["interest_rate"], loan["start_date"], loan["end_date"]))

    def update_loan(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a loan to update")
            return
        loan_id = self.tree.item(selected[0])["values"][0]
        new_amount = ttk.simpledialog.askfloat("Update Loan", "Enter new loan amount:")
        new_interest = ttk.simpledialog.askfloat("Update Interest", "Enter new interest rate:")
        if new_amount is not None and new_interest is not None:
            if database.update_loan(loan_id, new_amount, new_interest):
                messagebox.showinfo("Success", "Loan updated!")
                self.refresh_data()
    def delete_loan(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showerror("Error", "Select a loan to delete")
            return
        loan_id = self.tree.item(selected[0])["values"][0]
        if database.delete_loan(loan_id):
            messagebox.showinfo("Success", "Loan deleted!")
            self.refresh_data()
        else:
            messagebox.showerror("Error", "Failed to delete loan.")

# ==============================
# Export Data Page
# ==============================
class ExportData(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        controller.add_navbar(self)

        ttk.Label(self, text="📤 Export Data", font=("Arial", 16, "bold")).pack(pady=10)
        ttk.Button(self, text="Export Everything as CSV", bootstyle="success", command=self.export_all_csv).pack(pady=5)
        ttk.Button(self, text="Export Everything as JSON", bootstyle="info", command=self.export_all_json).pack(pady=5)

    def export_all_csv(self):
        username = self.controller.current_user
        # Expenses
        expenses = database.get_expenses(username)
        if expenses:
            pd.DataFrame(expenses).to_csv(f"expenses_{username}.csv", index=False)
        # Accounts
        accounts = database.get_accounts(username)
        if accounts:
            pd.DataFrame(accounts).to_csv(f"accounts_{username}.csv", index=False)
        # Loans
        loans = database.get_loans(username)
        if loans:
            pd.DataFrame(loans).to_csv(f"loans_{username}.csv", index=False)
        messagebox.showinfo("Success", "All data exported as CSV!")

    def export_all_json(self):
        username = self.controller.current_user
        export_data = {
            "expenses": database.get_expenses(username) or [],
            "accounts": database.get_accounts(username) or [],
            "loans": database.get_loans(username) or []
        }
        filename = f"user_data_{username}.json"
        pd.DataFrame(export_data["expenses"]).to_json(f"expenses_{username}.json", orient='records', lines=True)
        pd.DataFrame(export_data["accounts"]).to_json(f"accounts_{username}.json", orient='records', lines=True)
        pd.DataFrame(export_data["loans"]).to_json(f"loans_{username}.json", orient='records', lines=True)
        messagebox.showinfo("Success", f"All data exported as JSON (separate files).")



# ==============================
# Runner
# ==============================
def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()
