from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout

from src.di import APPS
from src.utils import Header, MainButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        buttons = QVBoxLayout()
        buttons.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        main_layout.addWidget(Header("Выбери экзамен"), alignment=Qt.AlignmentFlag.AlignHCenter)

        for name, api in APPS.items():
            buttons.addWidget(MainButton(name=api['name'], application=api['settings'], parent=self))

        main_layout.addLayout(buttons)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)
