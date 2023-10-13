import pandas as pd
import numpy as np
import tensorflow as tf
import json
from groupLabelling_ui import Ui_Dialog
from datasets_workers import WorkerLoadXMLDataset, WorkerLoadXMLCols
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget
from help import Impl_HelpWindow

class Impl_GroupLabelling_Window(Ui_Dialog, QtWidgets.QMainWindow):
    """Creates Group Labeler window"""

    def __init__(self):
        """Initializes Group Labeler window object"""
        super(Impl_GroupLabelling_Window, self).__init__()
        self.setupUi(self)