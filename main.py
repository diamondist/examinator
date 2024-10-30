from PyQt6.QtWidgets import QApplication

from src.gui import MainWindow

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.showMaximized()
    app.exec()
