from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QVBoxLayout, QLabel


class Header(QLabel):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(QSize(500, 50))
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setFont(QFont('Arial', 36))


class MainButton(QPushButton):
    def __init__(self, text):
        super().__init__()
        self.setText(text)
        self.setFixedSize(500, 50)
        self.setFont(QFont('Arial', 16))


class Multi_Table_Settings(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('NEW')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        main_layout = QVBoxLayout()
        buttons = QVBoxLayout()
        buttons.setAlignment(Qt.AlignmentFlag.AlignHCenter)

        main_layout.addWidget(Header("Выбери экзамен"), alignment=Qt.AlignmentFlag.AlignHCenter)

        multi_table_button = MainButton("Таблица умножения")
        multi_table_button.clicked.connect(self.multi_table)
        buttons.addWidget(multi_table_button)
        main_layout.addLayout(buttons)

        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    def multi_table(self):
        self.w = Multi_Table_Settings()
        self.hide()
        self.w.showMaximized()


app = QApplication([])
window = MainWindow()
window.showMaximized()
print(window.size())
