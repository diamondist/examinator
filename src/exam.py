from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QProgressBar

from src.elements import TaskText, CorrectMessage, WrongMessage, AnswerInput, AnswerButton, StatsMessage


class MockApp:
    def __init__(self):
        self.tasks = [
            {
                'text': '1 \u00d7 4',
                'answer': '4',
            },
            {
                'text': '2 \u00d7 4',
                'answer': '8',
            },
            {
                'text': '3 \u00d7 4',
                'answer': '12',
            },
        ]
        self.num_tasks = 6

    def get_task(self):
        for item in self.tasks:
            item = {
                'task': item,
                'num_tasks': self.num_tasks
            }
            yield item


class Exam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Экзамен')
        self.app = MockApp()
        self.get_task = self.app.get_task()
        self.task = next(self.get_task)
        self.answer = ''
        self.correct = 0
        self.wrong = 0
        self.total = 0

        layout = QVBoxLayout()

        self.task_text = TaskText(self.task['task']['text'])

        self.answer_input = AnswerInput()
        self.answer_input.textChanged.connect(self.accept_answer)

        self.answer_button = AnswerButton()
        self.answer_button.pressed.connect(self.check_answer)

        self.progress = QProgressBar()

        layout.addWidget(self.task_text, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.answer_input, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.answer_button, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.progress)

        self.setLayout(layout)

    def accept_answer(self, answer):
        self.answer = answer

    def check_answer(self):
        self.total += 1
        self.progress.setValue(int(self.total / self.task['num_tasks'] * 100))

        if self.answer == self.task['task']['answer']:
            CorrectMessage(self)
            self.correct += 1
        else:
            WrongMessage(self)
            self.wrong += 1

        self.answer_input.setText('')

        try:
            self.task = next(self.get_task)
            self.task_text.setText(self.task['task']['text'])
        except StopIteration:
            stats = StatsMessage(self.total, self.correct, self.wrong, self)
            stats.exec()
