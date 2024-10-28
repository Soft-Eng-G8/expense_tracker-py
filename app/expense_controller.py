# expense_controller.py
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from app.ui.expense_ui import ExpenseUI

class ExpenseApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the main window
        self.setWindowTitle("Expense Tracker")
        self.setGeometry(100, 100, 600, 400)

        # Create the UI and set it as the central widget
        self.ui = ExpenseUI()
        self.setCentralWidget(self.ui)

        # Connect the button to the add_expense method
        self.ui.input_panel.add_button.clicked.connect(self.add_expense)

        # Connect the row_deleted signal to the delete_expense method
        self.ui.expense_table.row_deleted.connect(self.delete_expense)

        # Add default data
        self.add_default_data()

    def add_default_data(self):
        initial_data = [("Groceries", 50.0), ("Fuel", 70.0), ("Gym", 30.0)]
        for expense, price in initial_data:
            self.add_expense_to_table(expense, price)
        self.update_total()

    def add_expense(self):
        expense = self.ui.input_panel.expense_input.text().strip()
        price = self.ui.input_panel.price_input.text().strip()

        if self.is_valid_expense(expense, price):
            self.add_expense_to_table(expense, price)
            self.clear_input_fields()
            self.update_total()

    def update_total(self):
        total = self.calculate_total()
        self.ui.total_panel.update_total(total)

    def add_expense_to_table(self, expense, price):
        self.ui.expense_table.add_expense(expense, str(price))

    def clear_input_fields(self):
        self.ui.input_panel.expense_input.clear()
        self.ui.input_panel.price_input.clear()

    def is_valid_expense(self, expense, price):
        return expense and price

    def calculate_total(self):
        total = 0.0
        for row in range(self.ui.expense_table.rowCount()):
            item = self.ui.expense_table.item(row, 1)
            if item:
                total += float(item.text())
        return total

    def delete_expense(self, row):
        """Delete an expense from the table and update the total."""
        self.ui.expense_table.removeRow(row)
        self.update_total()
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load the QSS stylesheet
    with open("app/ui/style.qss", "r") as f:
        app.setStyleSheet(f.read())

    window = ExpenseApp()
    window.show()
    sys.exit(app.exec_())