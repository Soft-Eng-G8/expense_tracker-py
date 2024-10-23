# ui/total_panel.py
from PyQt5.QtWidgets import QHBoxLayout, QLabel, QWidget

class TotalPanel(QWidget):
    def __init__(self):
        super().__init__()

        # Create the layout
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 10, 0, 0)

        # Total label and value
        self.total_label = QLabel("Total:")
        self.total_value = QLabel("0.00")
        self.total_value.setStyleSheet("font-size: 16px; color: #5cb85c; font-weight: bold;")

        # Add widgets to layout
        self.layout.addWidget(self.total_label)
        self.layout.addWidget(self.total_value)
        self.layout.addStretch()

    def update_total(self, total):
        self.total_value.setText(f"{total:.2f}")