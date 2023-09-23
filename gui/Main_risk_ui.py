from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class RiskWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Risk Window')
        self.setGeometry(100, 100, 400, 300)
        
    