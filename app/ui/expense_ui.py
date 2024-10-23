# ui/expense_ui.py
from PyQt5.QtWidgets import (
    QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSpacerItem, QSizePolicy
)
from app.ui.input_panel import InputPanel
from app.ui.expense_table import ExpenseTable
from app.ui.total_panel import TotalPanel

class ExpenseUI(QWidget):
    def __init__(self):
        super().__init__()

        # Create the main layout
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(15, 15, 15, 15)
        self.layout.setSpacing(10)

        # Input panel (aligned horizontally)
        self.input_panel = InputPanel()
        self.layout.addWidget(self.input_panel)

        # Spacer between the input and table
        self.layout.addSpacerItem(QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Expanding))

        # Expense table
        self.expense_table = ExpenseTable()
        self.layout.addWidget(self.expense_table)

        # Total panel at the bottom
        self.total_panel = TotalPanel()
        self.layout.addWidget(self.total_panel)