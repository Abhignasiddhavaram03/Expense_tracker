import unittest
from expense_manager import ExpenseManager
import os

class TestExpenseManager(unittest.TestCase):

    def test_total_calculation(self):
        manager = ExpenseManager()
        manager.add_expense(100, "Food")
        manager.add_expense(50, "Transport")
        self.assertEqual(manager.total_expense(), 150)

    def test_invalid_input(self):
        manager = ExpenseManager()
        with self.assertRaises(ValueError):
            manager.add_expense(-10, "Food")

    def test_csv_save_load(self):
        manager = ExpenseManager()
        manager.add_expense(100, "Food")
        manager.save_to_csv("test.csv")

        new_manager = ExpenseManager()
        new_manager.load_from_csv("test.csv")

        self.assertEqual(new_manager.total_expense(), 100)

        os.remove("test.csv")

if __name__ == "__main__":
    unittest.main()