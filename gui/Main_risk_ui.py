from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class RiskWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Risk Window')
        self.setMinimumSize(1280, 720)

        # Create a button named "Load Dataset"
        self.load_dataset_button = QtWidgets.QPushButton(self)
        self.load_dataset_button.setGeometry(QtCore.QRect(50, 50, 200, 100))

        # Create a label inside the button
        self.label_in_load_dataset_button = QtWidgets.QLabel(self.load_dataset_button)
        self.label_in_load_dataset_button.setGeometry(QtCore.QRect(0, 0, self.load_dataset_button.width(), self.load_dataset_button.height()))
        self.label_in_load_dataset_button.setText("Load Dataset")
        self.label_in_load_dataset_button.setAlignment(QtCore.Qt.AlignCenter)

        # Create a QLabel to display the label "File Path:"
        self.file_path_label = QtWidgets.QLabel(self)
        self.file_path_label.setGeometry(QtCore.QRect(self.load_dataset_button.geometry().right() + 10, 50, 100, 100))
        self.file_path_label.setText("Path:")
        self.file_path_label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)

        # Calculate the width for the file path line edit
        line_edit_width = self.width() - self.load_dataset_button.geometry().right() - 120

        # Create a line edit widget to display the file path
        self.file_path_lineedit = QtWidgets.QLineEdit(self)
        self.file_path_lineedit.setGeometry(QtCore.QRect(self.file_path_label.geometry().right() + 10, 50, line_edit_width, 100))
        self.file_path_lineedit.setPlaceholderText('Selected file path')
        self.file_path_lineedit.setReadOnly(True)

        # Connect the button to the click event
        self.load_dataset_button.clicked.connect(self.btn_Load_Dataset_clicked)

    def btn_Load_Dataset_clicked(self):
        """Clicked event on the Load Datset button.
        Opens a file dialog to select a data file.
        """
        file_dialog = QtWidgets.QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, 'Open Data File', '', 'CSV Files (*.csv);;XML Files (*.xml)')

        if file_path:
            print('Selected file:', file_path)
            # Update the line edit with the selected file path
            self.file_path_lineedit.setText(file_path)
            # Implement the logic to process the selected data file here
            # You can use the file_path to access the selected data file
        
    