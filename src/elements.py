from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont, QPalette, QColor
from PyQt6.QtWidgets import QPushButton, QLabel, QWidget, QCheckBox, QVBoxLayout, QMessageBox, QLineEdit, QDialog, \
    QDialogButtonBox


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


class MultiButton(QPushButton):
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
        # self.setFixedSize(QSize(600, 500))
        self.setFont(QFont('Arial', 56))


class WrongMessage(QMessageBox):
    def __init__(self, parent):
        super().__init__()
        self.warning(
            parent,
            'Ошибка',
            f'Твой ответ {parent.answer} \n Правильный ответ {parent.task['task']['answer']}',
        )

class AnswerInput(QLineEdit):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(300, 100))
        self.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setFont(QFont('Arial', 56))

class AnswerButton(QPushButton):
    def __init__(self):
        super().__init__()
        self.setText("Ответить")
        self.setFixedSize(500, 50)
        self.setFont(QFont('Arial', 16))

class StatsMessage(QDialog):
    def __init__(self, total, correct, wrong, parent):
        super().__init__()
        self.setWindowTitle('Экзамен завершен')
        self.stats = Header(f'Всего вопросов: {total}')
        self.stats2 = Header(f'Правильно: {correct}')
        self.stats3 = Header(f'Ошибок: {wrong}')

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.stats, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.stats2, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.layout.addWidget(self.stats3, alignment=Qt.AlignmentFlag.AlignHCenter)


        if correct / total >= 0.8:
            text = 'Экзамен сдан успешно!'
            color = 'green'
        else:
            text = 'Экзамен не сдан'
            color = 'red'

        self.result = QLabel()
        self.result.setText(text)
        self.result.setFixedSize(QSize(600, 50))
        self.result.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.result.setFont(QFont('Arial', 36))
        self.result.setStyleSheet(f"background-color: {color}")
        self.layout.addWidget(self.result, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.setLayout(self.layout)
        parent.hide()
        self.showMaximized()
