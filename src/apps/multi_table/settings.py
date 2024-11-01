from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from src.elements import Header, MainButton, MultiButton
from src.exam import Exam


class MultiTableSettings(QWidget):
    def __init__(self, parent, app):
        super().__init__()
        self.setWindowTitle("Таблица умножения")
        self.multis = {}
        self.app = app

        main_layout = QVBoxLayout()

        main_layout.addWidget(Header("Выбери множители"), alignment=Qt.AlignmentFlag.AlignHCenter)

        boxes = QHBoxLayout()
        for i in range(2, 10):
            self.multis[i] = False
            check_button = MultiButton(str(i))
            check_button.setCheckable(True)
            check_button.pressed.connect(lambda val=i: self.make_settings(val))
            boxes.addWidget(check_button)

        main_layout.addLayout(boxes)

        exam_button = MainButton("Начать экзамен")
        exam_button.clicked.connect(self.call_exam)
        main_layout.addWidget(exam_button, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(main_layout)
        parent.hide()
        self.showMaximized()

    def call_exam(self, parent):
        self.exam = Exam(self.app(self.multis))
        self.hide()
        self.exam.showMaximized()

    def make_settings(self, i):
        self.multis[i] = not self.multis[i]
