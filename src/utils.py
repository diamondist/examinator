from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton, QLabel, QWidget


class MainButton(QPushButton):
    def __init__(self, name, application, parent):
        super().__init__()
        self.setText(name)
        self.setFixedSize(500, 50)
        self.setFont(QFont('Arial', 16))
        self.application = application()
        self.clicked.connect(lambda x: self.application.launch(parent))


class Header(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(QSize(500, 50))
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setFont(QFont('Arial', 36))


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Exam')

    def launch(self, parent):
        parent.hide()
        self.showMaximized()
