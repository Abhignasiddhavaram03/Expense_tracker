import csv

class ExpenseManager:
    def __init__(self):
        self.expenses = []

    def add_expense(self, amount, category):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.expenses.append({"amount": amount, "category": category})

    def total_expense(self):
        return sum(exp["amount"] for exp in self.expenses)

    def save_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["amount", "category"])
            writer.writeheader()
            writer.writerows(self.expenses)

    def load_from_csv(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            self.expenses = [
                {"amount": float(row["amount"]), "category": row["category"]}
                for row in reader
            ]