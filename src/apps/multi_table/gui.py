from PyQt6.QtWidgets import QWidget


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Настройки")

    def settings(self, main_window):
        main_window.hide()
        self.showMaximized()

