# ui/input_panel.py
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QIcon

class InputPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Create the layout
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(10)

        # Expense label and input
        self.expense_label = QLabel("Expense:")
        self.expense_input = QLineEdit()
        self.expense_input.setPlaceholderText("Enter expense name")
        self.expense_input.setContentsMargins(0,0,20,0)
        self.expense_input.setFixedWidth(200)

        # Price label and input
        self.price_label = QLabel("Price:")
        self.price_input = QLineEdit()
        self.price_input.setPlaceholderText("Enter price")
        self.price_input.setContentsMargins(0,0,20,0)
        self.price_input.setFixedWidth(150)

        # Add Expense button with an icon
        self.add_button = QPushButton("Add Expense")
        self.add_button.setIcon(QIcon.fromTheme("list-add"))

        # Add widgets to layout
        self.layout.addWidget(self.expense_label)
        self.layout.addWidget(self.expense_input)
        self.layout.addWidget(self.price_label)
        self.layout.addWidget(self.price_input)
        self.layout.addWidget(self.add_button)