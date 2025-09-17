# db.py - Database setup and operations for Personal Finance App
import mysql.connector as mysql
import bcrypt

# ==============================
# Database Connection
# ==============================
try:
    print("Connecting to database...")
    connection = mysql.connect(
        host="localhost",
        user="root",
        password="Root"
    )
    print("Connected to MySQL server.")
except mysql.Error as e:
    print(f"Error connecting to MySQL: {e}")
    exit()

cursor = connection.cursor()

# ==============================
# Create Database
# ==============================
cursor.execute("CREATE DATABASE IF NOT EXISTS personal_finance;")
cursor.execute("USE personal_finance;")

# ==============================
# Tables
# ==============================
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    account_name VARCHAR(100) NOT NULL,
    account_type ENUM('checking','savings','credit','investment') NOT NULL,
    balance DECIMAL(15,2) NOT NULL DEFAULT 0.00,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    amount DECIMAL(15,2) NOT NULL,
    category VARCHAR(100) NOT NULL,
    expense_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS subscriptions (
    subscription_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    service_name VARCHAR(100) NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    billing_cycle ENUM('monthly','yearly') NOT NULL,
    next_billing_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS groceries (
    grocery_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    item_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(15,2) NOT NULL,
    purchase_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS investments (
    investment_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    investment_type ENUM('stock','bond','mutual_fund','real_estate') NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    investment_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS income (
    income_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    amount DECIMAL(15,2) NOT NULL,
    source VARCHAR(100) NOT NULL,
    income_date DATE NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS savings (
    saving_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    amount DECIMAL(15,2) NOT NULL,
    goal VARCHAR(100),
    saving_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS bills (
    bill_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    amount DECIMAL(15,2) NOT NULL,
    bill_type VARCHAR(100) NOT NULL,
    due_date DATE NOT NULL,
    paid BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    loan_type VARCHAR(100) NOT NULL,
    amount DECIMAL(15,2) NOT NULL,
    interest_rate DECIMAL(5,2) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS extra_expenses (
    extra_expense_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    amount DECIMAL(15,2) NOT NULL,
    reason VARCHAR(255) NOT NULL,
    expense_date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id) ON DELETE CASCADE
);
""")

connection.commit()
print("Database schema setup complete.")

# ==============================
# User Functions
# ==============================
def signup_user(username, email, password):
    """Create a new user with hashed password"""
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    query = "INSERT INTO users (username, email, password_hash) VALUES (%s,%s,%s)"
    try:
        cursor.execute(query, (username, email, hashed))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Signup error: {e}")
        return False


def login_user(username, password, email):
    """Check if username/password match"""
    query = "SELECT password_hash FROM users WHERE username=%s OR email=%s"
    cursor.execute(query, (username, email))
    row = cursor.fetchone()
    if row:
        stored_hash = row[0].encode("utf-8")
        return bcrypt.checkpw(password.encode("utf-8"), stored_hash)
    return False


# ==============================
# Account Functions
# ==============================
def add_account(user_id, account_name, account_type, balance=0.00):
    query = "INSERT INTO accounts (user_id, account_name, account_type, balance) VALUES (%s,%s,%s,%s)"
    try:
        cursor.execute(query, (user_id, account_name, account_type, balance))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Add account error: {e}")
        return False


def get_user_accounts(username):
    """Return accounts for a given username as list of dicts"""
    query = """
    SELECT a.account_id, a.account_name, a.account_type, a.balance
    FROM accounts a
    JOIN users u ON a.user_id = u.user_id
    WHERE u.username = %s
    """
    cursor.execute(query, (username,))
    rows = cursor.fetchall()
    return [
        {"account_id": r[0], "account_name": r[1], "account_type": r[2], "balance": float(r[3])}
        for r in rows
    ]

def add_expense(username, amount, category, date, description):
    try:
        # Get the account_id of the logged-in user (we'll just use their first account)
        cursor.execute("""
            SELECT a.account_id 
            FROM accounts a
            JOIN users u ON a.user_id = u.user_id
            WHERE u.username = %s
            LIMIT 1
        """, (username,))
        result = cursor.fetchone()

        if not result:
            print("No account found for this user.")
            return False

        account_id = result[0]

        query = """
        INSERT INTO expenses (account_id, amount, category, expense_date, description)
        VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(query, (account_id, amount, category, date, description))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Add expense error: {e}")
        return False

def get_expenses(username):
    """Return all expenses for the given username"""
    try:
        query = """
        SELECT e.expense_id, e.amount, e.category, e.expense_date, e.description
        FROM expenses e
        JOIN accounts a ON e.account_id = a.account_id
        JOIN users u ON a.user_id = u.user_id
        WHERE u.username = %s
        ORDER BY e.expense_date DESC
        """
        cursor.execute(query, (username,))
        rows = cursor.fetchall()
        return [
            {
                "expense_id": r[0],
                "amount": float(r[1]),
                "category": r[2],
                "expense_date": r[3].strftime("%Y-%m-%d"),
                "description": r[4] or ""
            }
            for r in rows
        ]
    except mysql.Error as e:
        print(f"Get expenses error: {e}")
        return []

def add_loan(account_id, loan_type, amount, interest_rate, start_date, end_date):
    try:
        query = """
        INSERT INTO loans (account_id, loan_type, amount, interest_rate, start_date, end_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (account_id, loan_type, amount, interest_rate, start_date, end_date))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Add loan error: {e}")
        return False

def get_accounts(username):
    query = """
    SELECT a.account_id, a.account_name, a.account_type, a.balance
    FROM accounts a
    JOIN users u ON a.user_id = u.user_id
    WHERE u.username = %s
    """
    cursor.execute(query, (username,))
    rows = cursor.fetchall()
    return [{"account_id": r[0], "account_name": r[1], "account_type": r[2], "balance": float(r[3])} for r in rows]

def update_account(account_id, balance):
    try:
        cursor.execute("UPDATE accounts SET balance=%s WHERE account_id=%s", (balance, account_id))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Update account error: {e}")
        return False

def get_loans(username):
    query = """
    SELECT l.loan_id, l.loan_type, l.amount, l.interest_rate, l.start_date, l.end_date
    FROM loans l
    JOIN accounts a ON l.account_id = a.account_id
    JOIN users u ON a.user_id = u.user_id
    WHERE u.username = %s
    """
    cursor.execute(query, (username,))
    rows = cursor.fetchall()
    return [{"loan_id": r[0], "loan_type": r[1], "amount": float(r[2]), "interest_rate": float(r[3]), "start_date": r[4], "end_date": r[5]} for r in rows]

def update_loan(loan_id, amount, interest_rate):
    try:
        cursor.execute("UPDATE loans SET amount=%s, interest_rate=%s WHERE loan_id=%s", (amount, interest_rate, loan_id))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Update loan error: {e}")
        return False

def delete_expense(expense_id):
    try:
        cursor.execute("DELETE FROM expenses WHERE expense_id=%s", (expense_id,))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Delete expense error: {e}")
        return False

def delete_account(account_id):
    try:
        cursor.execute("DELETE FROM accounts WHERE account_id=%s", (account_id,))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Delete account error: {e}")
        return False
    

def delete_loan(loan_id):
    try:
        cursor.execute("DELETE FROM loans WHERE loan_id=%s", (loan_id,))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Delete loan error: {e}")
        return False
    
# ==============================
# Close Connection
# ==============================
def close_connection():
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Database connection closed.")
