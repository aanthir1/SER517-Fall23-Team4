from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(889, 456)

        # Create a scroll area widget to hold the radio buttons
        scroll_area = QtWidgets.QScrollArea(Dialog)
        scroll_area.setGeometry(QtCore.QRect(120, 330, 631, 50))
        scroll_area.setWidgetResizable(True)

        scroll_widget = QtWidgets.QWidget()
        scroll_area.setWidget(scroll_widget)
        scroll_layout = QtWidgets.QVBoxLayout(scroll_widget)

        # Create True and False radio buttons and add them to the layout
        true_radio_button = QtWidgets.QRadioButton("True")
        false_radio_button = QtWidgets.QRadioButton("False")
        scroll_layout.addWidget(true_radio_button)
        scroll_layout.addWidget(false_radio_button)

        # Your existing table widget
        self.tbl_CurrentExample = QtWidgets.QTableWidget(Dialog)
        self.tbl_CurrentExample.setGeometry(QtCore.QRect(120, 140, 631, 181))
        self.tbl_CurrentExample.setObjectName("tbl_CurrentExample")
        self.tbl_CurrentExample.setColumnCount(2)
        self.tbl_CurrentExample.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_CurrentExample.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_CurrentExample.setHorizontalHeaderItem(1, item)
        self.tbl_CurrentExample.horizontalHeader().setStretchLastSection(True)

        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(120, 80, 81, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")

        self.comboBox_2 = QtWidgets.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(220, 80, 81, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")

        self.comboBox_3 = QtWidgets.QComboBox(Dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(320, 80, 81, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")

        self.comboBox_4 = QtWidgets.QComboBox(Dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(420, 80, 81, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")

        self.comboBox_5 = QtWidgets.QComboBox(Dialog)
        self.comboBox_5.setGeometry(QtCore.QRect(520, 80, 81, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        item = self.tbl_CurrentExample.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "Key"))
        item = self.tbl_CurrentExample.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Value"))
        self.comboBox.setItemText(0, _translate("Dialog", "Status"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "Option 2"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Option 3"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Option 4"))
        self.comboBox_5.setItemText(0, _translate("Dialog", "Option 5"))
