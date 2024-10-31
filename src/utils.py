from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QPushButton, QLabel, QWidget, QCheckBox, QVBoxLayout, QMessageBox


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


class CheckButton(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(QSize(100, 50))
        self.setFont(QFont('Arial', 36))
        self.setStyleSheet("QCheckBox::indicator { width: 50px; height: 50px;}")


class TaskText(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(QSize(500, 50))
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setFont(QFont('Arial', 56))
        self.setMinimumHeight(300)


class CorrectMessage(QMessageBox):
    def __init__(self, parent):
        super().__init__()
        self.information(
            parent,
            'Правильно!',
            'Твой ответ правильный!'
        )


class WrongMessage(QMessageBox):
    def __init__(self, parent):
        super().__init__()
        self.warning(
            parent,
            'Ошибка',
            f'Твой ответ {parent.answer} \n Правильный ответ {parent.task['task']['answer']}',
        )
