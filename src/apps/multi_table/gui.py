from PyQt6.QtWidgets import QWidget



class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Таблица умножения")


    def launch(self, parent):
        parent.hide()
        self.showMaximized()

