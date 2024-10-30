from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton, QLabel


class MainButton(QPushButton):
    def __init__(self, text, application, parent):
        super().__init__()
        self.setText(text)
        self.setFixedSize(500, 50)
        self.setFont(QFont('Arial', 16))
        self.application=application()
        self.clicked.connect(lambda x: self.application.launch(parent))

class Header(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(QSize(500, 50))
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setFont(QFont('Arial', 36))
