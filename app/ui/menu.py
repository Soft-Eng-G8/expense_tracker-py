# ui/menu.py
from PyQt5.QtWidgets import QMenuBar, QMenu

def create_menu_bar():
    menu_bar = QMenuBar()
    file_menu = QMenu("File")
    edit_menu = QMenu("Edit")
    help_menu = QMenu("Help")

    menu_bar.addMenu(file_menu)
    menu_bar.addMenu(edit_menu)
    menu_bar.addMenu(help_menu)

    return menu_bar