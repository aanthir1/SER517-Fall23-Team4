# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupLabelling.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from common_ui import add_actions_to_toolbar


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(889, 600)  # Increase the height of the main window
        
        #tool bar
        self.toolbar = Dialog.addToolBar("TopToolBar")
        self.toolbar, self.go_back_button, self.home_button = add_actions_to_toolbar(self.toolbar, self)

        # Create a scroll area widget to hold the radio buttons
        scroll_area = QtWidgets.QScrollArea(Dialog)
        scroll_area.setGeometry(QtCore.QRect(120, 480, 631, 100))  # Adjust the position and size of the scroll area
        scroll_area.setWidgetResizable(True)

        scroll_widget = QtWidgets.QWidget()
        scroll_area.setWidget(scroll_widget)
        scroll_layout = QtWidgets.QVBoxLayout(scroll_widget)

        # Create True and False radio buttons and add them to the layout
        self.true_radio_button = QtWidgets.QRadioButton("True")
        self.false_radio_button = QtWidgets.QRadioButton("False")
        self.clear_button = QtWidgets.QRadioButton("None")
        scroll_layout.addWidget(self.true_radio_button)
        scroll_layout.addWidget(self.false_radio_button)
        scroll_layout.addWidget(self.clear_button)

        self.tbl_MatchingRecords = QtWidgets.QTableWidget(Dialog)
        self.tbl_MatchingRecords.setGeometry(QtCore.QRect(120, 140, 631, 331))  # Increase the height of the table widget
        self.tbl_MatchingRecords.setObjectName("tbl_MatchingRecords")
        self.tbl_MatchingRecords.setColumnCount(3)
        self.tbl_MatchingRecords.setHorizontalHeaderLabels(["Key", "Value", "Output"])
        self.tbl_MatchingRecords.horizontalHeader().setStretchLastSection(True)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(161, 80, 81, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(341, 80, 81, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setGeometry(QtCore.QRect(80, 80, 81, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(260, 80, 81, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(450, 80, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.save_dataset_button = QtWidgets.QPushButton("Save Dataset", Dialog)
        self.save_dataset_button.setGeometry(QtCore.QRect(680, 80, 131, 31))  # Adjust the position and size
        self.save_dataset_button.setObjectName("save_dataset_button")
        # self.go_back_button = QtWidgets.QPushButton("Go back to Labeler", Dialog)
        # self.go_back_button.setGeometry(QtCore.QRect((Dialog.width() - self.go_back_button.width()) / 2, 550, 141, 31))
        #self.go_back_button.setObjectName("go_back_button")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "GroupLabeling | Vinci ML Tool"))
        self.comboBox.setItemText(0, _translate("Dialog", "Status"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Select"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "Key :"))
        self.plainTextEdit_2.setPlainText(_translate("Dialog", "Value :"""))
        self.pushButton.setText(_translate("Dialog", "LABEL"))

        self.save_dataset_button.setText(_translate("Dialog", "Save Dataset"))
        self.go_back_button.setText(_translate("Dialog", "Go back to Labeler"))