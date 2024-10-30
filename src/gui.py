from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLabel

from src.apps.di import APPS


class Header(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(QSize(500, 50))
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setFont(QFont('Arial', 36))


class MainButton(QPushButton):
    def __init__(self, text, application, main_window):
        super().__init__()
        self.setText(text)
        self.setFixedSize(500, 50)
        self.setFont(QFont('Arial', 16))
        self.application=application()
        self.clicked.connect(lambda x: self.application.settings(main_window))


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        buttons = QVBoxLayout()
        buttons.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        main_layout.addWidget(Header("Выбери экзамен"), alignment=Qt.AlignmentFlag.AlignHCenter)


        for name, application in APPS.items():
            buttons.addWidget(MainButton(name, application, self))

        main_layout.addLayout(buttons)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)



app = QApplication([])
window = MainWindow()
window.showMaximized()
