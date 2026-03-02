import tkinter as tk
from tkinter import messagebox
from expense_manager import ExpenseManager

manager = ExpenseManager()

def add_expense():
    try:
        amount = float(amount_entry.get())
        category = category_entry.get()
        manager.add_expense(amount, category)
        messagebox.showinfo("Success", "Expense Added")
        update_total()
    except ValueError:
        messagebox.showerror("Error", "Invalid amount")

def update_total():
    total_label.config(text=f"Total: {manager.total_expense()}")

def save_data():
    manager.save_to_csv("expenses.csv")
    messagebox.showinfo("Saved", "Data saved to CSV")

def load_data():
    manager.load_from_csv("expenses.csv")
    update_total()
    messagebox.showinfo("Loaded", "Data loaded from CSV")

root = tk.Tk()
root.title("Expense Tracker")

tk.Label(root, text="Amount").pack()
amount_entry = tk.Entry(root)
amount_entry.pack()

tk.Label(root, text="Category").pack()
category_entry = tk.Entry(root)
category_entry.pack()

tk.Button(root, text="Add Expense", command=add_expense).pack()
tk.Button(root, text="Save", command=save_data).pack()
tk.Button(root, text="Load", command=load_data).pack()

total_label = tk.Label(root, text="Total: 0")
total_label.pack()

root.mainloop()