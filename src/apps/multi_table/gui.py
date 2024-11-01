from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from src.elements import Header, MainButton, MultiButton
from src.exam import Exam


class MultiTableSettings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Таблица умножения")
        self.multis = {}
        for i in range(2, 10):
            self.multis[i] = False

        main_layout = QVBoxLayout()

        main_layout.addWidget(Header("Выбери множители"), alignment=Qt.AlignmentFlag.AlignHCenter)

        boxes = QHBoxLayout()
        for i in range(2, 10):
            check_button = MultiButton(str(i))
            check_button.setCheckable(True)
            check_button.pressed.connect(lambda val=i: self.make_settings(val))
            boxes.addWidget(check_button)

        main_layout.addLayout(boxes)

        main_layout.addWidget(MainButton("Начать экзамен", Exam, parent=self),
                              alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(main_layout)

    def make_settings(self, i):
        self.multis[i] = not self.multis[i]

    def launch(self, parent):
        parent.hide()
        self.showMaximized()
