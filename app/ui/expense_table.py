# ui/expense_table.py
from PyQt5.QtWidgets import QTableWidget, QTableWidgetItem

class ExpenseTable(QTableWidget):
    def __init__(self):
        super().__init__()

        # Set up table with 2 columns
        self.setColumnCount(2)
        self.setHorizontalHeaderLabels(["Expense", "Price"])

    def add_expense(self, expense, price):
        """Add a new expense to the table."""
        row_position = self.rowCount()
        self.insertRow(row_position)
        self.setItem(row_position, 0, QTableWidgetItem(expense))
        self.setItem(row_position, 1, QTableWidgetItem(price))