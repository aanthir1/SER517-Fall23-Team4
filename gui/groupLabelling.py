import pandas as pd
from groupLabelling_ui import Ui_Dialog
from PyQt5 import QtWidgets

class Impl_GroupLabelling_Window(Ui_Dialog, QtWidgets.QMainWindow):
    """Creates Group Labeler window"""

    def __init__(self, dataset_path):
        """Initializes Group Labeler window object"""
        super(Impl_GroupLabelling_Window, self).__init__()
        self.setupUi(self)
        self.path = dataset_path

        # Add items to the comboBox
        try:
            df = pd.read_csv(dataset_path)  # Use read_excel for Excel files
            column_names = df.columns
            self.comboBox.addItems(column_names)  # Add column names directly to the comboBox
        except Exception as e:
            print("Error:", e)

