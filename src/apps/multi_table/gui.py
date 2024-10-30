from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QCheckBox

from src.utils import Header, MainButton, Exam


class CheckBox(QCheckBox):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(QSize(100, 50))
        self.setFont(QFont('Arial', 36))
        self.setStyleSheet("QCheckBox::indicator { width: 50px; height: 50px;}")


class MultiTableSettings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Таблица умножения")

        main_layout = QVBoxLayout()

        main_layout.addWidget(Header("Выбери множители"), alignment=Qt.AlignmentFlag.AlignHCenter)

        boxes = QHBoxLayout()
        for i in range(2, 10):
            boxes.addWidget(CheckBox(str(i)))



        main_layout.addLayout(boxes)

        main_layout.addWidget(MainButton("Начать экзамен", Exam, parent=self),
                              alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(main_layout)

    def launch(self, parent):
        parent.hide()
        self.showMaximized()
