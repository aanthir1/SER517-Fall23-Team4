# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'datasets.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHeaderView


class Ui_DatasetsWindow(object):
    def setupUi(self, DatasetsWindow):
        DatasetsWindow.setObjectName("DatasetsWindow")
        DatasetsWindow.resize(1280, 720)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        DatasetsWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        DatasetsWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ML4CYBER_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        DatasetsWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DatasetsWindow)
        self.centralwidget.setObjectName("centralwidget")

        # The horizontal layout for the widget to help resizing the window
        self.hlayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.hlayout.setObjectName("hlayout")
        self.hlayout.setContentsMargins(0, 0, 0, 0)
        self.hlayout.setSpacing(0)

        self.vlayout1 = QtWidgets.QVBoxLayout()
        self.vlayout1.setObjectName("vlayout1")
        self.vlayout1.setContentsMargins(30, 20, 0, 30)
        self.vlayout1.setSpacing(10)

        self.vlayout2 = QtWidgets.QVBoxLayout()
        self.vlayout2.setObjectName("vlayout2")
        self.vlayout2.setContentsMargins(20, 20, 50, 30)
        self.vlayout2.setSpacing(10)

        self.hlayout.addLayout(self.vlayout1, stretch=4)
        self.hlayout.addLayout(self.vlayout2, stretch=1)

        #group 1
        self.group_hlayout1 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.group_hlayout1.setObjectName("group_hlayout1")
        self.group_hlayout1.setContentsMargins(0, 0, 0, 31)
        self.vlayout1.addLayout(self.group_hlayout1, stretch=1)

        self.btn_LoadDataset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_LoadDataset.setGeometry(QtCore.QRect(30, 20, 171, 31))
        self.btn_LoadDataset.setObjectName("btn_LoadDataset")
        self.group_hlayout1.addWidget(self.btn_LoadDataset, stretch=2)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 20, 51, 31))
        self.label.setObjectName("label")
        self.label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.group_hlayout1.addWidget(self.label, stretch=1)

        self.txtB_DatasetPath = QtWidgets.QLineEdit(self.centralwidget)
        self.txtB_DatasetPath.setEnabled(True)
        self.txtB_DatasetPath.setGeometry(QtCore.QRect(280, 21, 701, 31))
        self.txtB_DatasetPath.setReadOnly(True)
        self.txtB_DatasetPath.setObjectName("txtB_DatasetPath")
        self.group_hlayout1.addWidget(self.txtB_DatasetPath, stretch=9)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 70, 0, 610))
        self.groupBox.setObjectName("groupBox")
        self.vlayout1.addWidget(self.groupBox, stretch=9)

        self.group_vlayout1 = QtWidgets.QVBoxLayout(self.groupBox)
        self.group_vlayout1.setObjectName("group_vlayout1")
        self.group_vlayout1.setContentsMargins(20, 0, 20, 0)
        self.groupBox.setLayout(self.group_vlayout1)

        #hlayout2
        self.group_hlayout2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.group_hlayout2.setObjectName("group_hlayout2")
        self.group_hlayout2.setContentsMargins(0, 10, 0, 10)
        self.group_vlayout1.addLayout(self.group_hlayout2)

        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(30, 0, 71, 31))
        self.label_13.setObjectName("label_13")

        self.cBox_Root = QtWidgets.QComboBox(self.groupBox)
        self.cBox_Root.setEnabled(False)
        self.cBox_Root.setGeometry(QtCore.QRect(70, 0, 621, 31))
        self.cBox_Root.setObjectName("cBox_Root")
        # Tooltip stating the functionality of the 'Root' box with tooltip duration of 6 seconds.
        self.cBox_Root.setToolTip("It depicts the hierarchy of XML tags.")
        self.cBox_Root.setToolTipDuration(6000)

        self.btn_AddColumn = QtWidgets.QPushButton(self.groupBox)
        self.btn_AddColumn.setGeometry(QtCore.QRect(760, 0, 161, 31))
        self.btn_AddColumn.setObjectName("btn_AddColumn")

        self.group_hlayout2.addWidget(self.label_13, stretch=1)
        self.group_hlayout2.addWidget(self.cBox_Root, stretch=6)
        self.group_hlayout2.addWidget(self.btn_AddColumn, stretch=2)

        #hlayout3
        self.group_hlayout3 = QtWidgets.QHBoxLayout(self.groupBox)
        self.group_hlayout3.setObjectName("group_hlayout3")
        self.group_hlayout3.setContentsMargins(0, 0, 0, 10)
        self.group_vlayout1.addLayout(self.group_hlayout3)

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 71, 31))
        self.label_2.setObjectName("label_2")

        self.cBox_Column = QtWidgets.QComboBox(self.groupBox)
        self.cBox_Column.setGeometry(QtCore.QRect(110, 10, 621, 31))
        self.cBox_Column.setObjectName("cBox_Column")

        # Tooltip stating the functionality of the 'Column' box with tooltip duration of 6 seconds.
        self.cBox_Column.setToolTip("Displays a dropdown of the columns present in the dataset.")
        self.cBox_Column.setToolTipDuration(6000)

        self.btn_RemoveColumn = QtWidgets.QPushButton(self.groupBox)
        self.btn_RemoveColumn.setGeometry(QtCore.QRect(760, 10, 161, 31))
        self.btn_RemoveColumn.setObjectName("btn_RemoveColumn")

        self.group_hlayout3.addWidget(self.label_2, stretch=1)
        self.group_hlayout3.addWidget(self.cBox_Column, stretch=6)
        self.group_hlayout3.addWidget(self.btn_RemoveColumn, stretch=2)

        #hlayout4
        self.group_hlayout4 = QtWidgets.QHBoxLayout(self.groupBox)
        self.group_hlayout4.setObjectName("group_hlayout4")
        self.group_hlayout4.setContentsMargins(0, 0, 0, 10)
        self.group_vlayout1.addLayout(self.group_hlayout4)

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 41, 31))
        self.label_4.setObjectName("label_4")

        self.cBox_Data = QtWidgets.QComboBox(self.groupBox)
        self.cBox_Data.setGeometry(QtCore.QRect(70, 160, 121, 31))
        self.cBox_Data.setObjectName("cBox_Data")
        self.cBox_Data.setToolTip("Type of the data - Categorical(label values) or Numerical.")
        self.cBox_Data.setToolTipDuration(6000)

        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(200, 160, 51, 31))
        self.label_15.setObjectName("label_15")
        self.label_15.setAlignment(Qt.AlignRight)

        self.cBox_Training = QtWidgets.QComboBox(self.groupBox)
        self.cBox_Training.setGeometry(QtCore.QRect(260, 160, 61, 31))
        self.cBox_Training.setObjectName("cBox_Training")
        self.cBox_Training.setToolTip("It shows if the data has been trained or not.")
        self.cBox_Training.setToolTipDuration(6000)

        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(330, 160, 121, 31))
        self.label_3.setObjectName("label_3")
        self.label_3.setAlignment(Qt.AlignRight)

        self.cBox_Transformation = QtWidgets.QComboBox(self.groupBox)
        self.cBox_Transformation.setGeometry(QtCore.QRect(430, 160, 131, 31))
        self.cBox_Transformation.setObjectName("cBox_Transformation")
        self.cBox_Transformation.setToolTip("Converts label values to binary values.")
        self.cBox_Transformation.setToolTipDuration(6000)

        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(570, 160, 51, 31))
        self.label_5.setObjectName("label_5")
        self.label_5.setAlignment(Qt.AlignRight)

        self.cBox_Type = QtWidgets.QComboBox(self.groupBox)
        self.cBox_Type.setGeometry(QtCore.QRect(610, 160, 121, 31))
        self.cBox_Type.setObjectName("cBox_Type")
        self.cBox_Type.setToolTip("Type of the data - Input or Output.")
        self.cBox_Type.setToolTipDuration(6000)

        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(740, 160, 81, 31))
        self.label_12.setObjectName("label_12")
        self.label_12.setAlignment(Qt.AlignRight)

        self.cBox_TPLabel = QtWidgets.QComboBox(self.groupBox)
        self.cBox_TPLabel.setGeometry(QtCore.QRect(800, 160, 121, 31))
        self.cBox_TPLabel.setObjectName("cBox_TPLabel")
        self.cBox_TPLabel.setToolTip("Displays the available labels for the selected column.")
        self.cBox_TPLabel.setToolTipDuration(6000)

        self.group_hlayout4.addWidget(self.label_4)
        self.group_hlayout4.addWidget(self.cBox_Data)
        self.group_hlayout4.addWidget(self.label_15)
        self.group_hlayout4.addWidget(self.cBox_Training)
        self.group_hlayout4.addWidget(self.label_3)
        self.group_hlayout4.addWidget(self.cBox_Transformation)
        self.group_hlayout4.addWidget(self.label_5)
        self.group_hlayout4.addWidget(self.cBox_Type)
        self.group_hlayout4.addWidget(self.label_12)
        self.group_hlayout4.addWidget(self.cBox_TPLabel)

        self.tbl_Dataset = QtWidgets.QTableWidget(self.groupBox)
        self.tbl_Dataset.setGeometry(QtCore.QRect(30, 220, 891, 350))
        self.tbl_Dataset.setRowCount(1)
        self.tbl_Dataset.setColumnCount(5)
        self.tbl_Dataset.setObjectName("tbl_Dataset")
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Dataset.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Dataset.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Dataset.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Dataset.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tbl_Dataset.setHorizontalHeaderItem(4, item)
        self.tbl_Dataset.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbl_Dataset.verticalHeader().setVisible(True)

        self.group_vlayout1.addWidget(self.tbl_Dataset)

        # second vlayout2
        self.btn_Labeler = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Labeler.setGeometry(QtCore.QRect(1010, 20, 241, 51))
        self.btn_Labeler.setObjectName("btn_Labeler")
        self.btn_Labeler.setFont(font)
        self.vlayout2.addWidget(self.btn_Labeler, stretch=2)

        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(1010, 90, 241, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.vlayout2.addWidget(self.groupBox_2, stretch=1)

        self.group_vlayout2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.group_vlayout2.setObjectName("group_vlayout2")
        self.groupBox_2.setLayout(self.group_vlayout2)

        self.group_hlayout5 = QtWidgets.QHBoxLayout(self.groupBox)
        self.group_hlayout5.setObjectName("group_hlayout5")
        self.group_vlayout2.addLayout(self.group_hlayout5)

        self.group_hlayout6 = QtWidgets.QHBoxLayout(self.groupBox)
        self.group_hlayout6.setObjectName("group_hlayout6")
        self.group_vlayout2.addLayout(self.group_hlayout6)

        self.txtB_InfoSamples = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtB_InfoSamples.setEnabled(True)
        self.txtB_InfoSamples.setGeometry(QtCore.QRect(30, 30, 80, 22))
        self.txtB_InfoSamples.setReadOnly(True)
        self.txtB_InfoSamples.setAlignment(Qt.AlignCenter)
        self.txtB_InfoSamples.setObjectName("txtB_InfoSamples")
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.group_hlayout5.addWidget(self.txtB_InfoSamples, stretch=1)
        self.group_hlayout5.addWidget(self.label_6, stretch=1)

        self.txtB_InfoFeatures = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtB_InfoFeatures.setEnabled(True)
        self.txtB_InfoFeatures.setText("")
        self.txtB_InfoFeatures.setReadOnly(True)
        self.txtB_InfoFeatures.setObjectName("txtB_InfoFeatures")
        self.txtB_InfoFeatures.setAlignment(Qt.AlignCenter)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(130, 80, 91, 16))
        self.label_7.setObjectName("label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.group_hlayout6.addWidget(self.txtB_InfoFeatures, stretch=1)
        self.group_hlayout6.addWidget(self.label_7, stretch=1)

        self.group_hlayout7 = QtWidgets.QHBoxLayout(self.groupBox)
        self.group_hlayout7.setObjectName("group_hlayout7")
        self.vlayout2.addLayout(self.group_hlayout7, stretch=1)

        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1008, 220, 61, 31))
        self.label_14.setObjectName("label_14")

        self.cBox_Preset = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_Preset.setGeometry(QtCore.QRect(1070, 220, 181, 31))
        self.cBox_Preset.setObjectName("cBox_Preset")
        # Tooltip stating the functionality of the 'Preset' box with tooltip duration of 6 seconds.
        self.cBox_Preset.setToolTip("List of static code analyser tools and corresponding report formats.")
        self.cBox_Preset.setToolTipDuration(6000)

        self.group_hlayout7.addWidget(self.label_14, stretch=1)
        self.group_hlayout7.addWidget(self.cBox_Preset, stretch=3)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1010, 270, 241, 191))
        self.groupBox_3.setObjectName("groupBox_3")
        self.vlayout2.addWidget(self.groupBox_3, stretch=1)

        self.group_vlayout3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.group_vlayout3.setObjectName("group_vlayout3")
        self.groupBox_3.setLayout(self.group_vlayout3)

        self.group_hlayout8 = QtWidgets.QHBoxLayout(self.groupBox)
        self.group_hlayout8.setObjectName("group_hlayout8")
        self.group_vlayout3.addLayout(self.group_hlayout8)

        self.txtB_TestPercentage = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtB_TestPercentage.setEnabled(True)
        self.txtB_TestPercentage.setGeometry(QtCore.QRect(160, 40, 61, 22))
        self.txtB_TestPercentage.setText("")
        self.txtB_TestPercentage.setReadOnly(True)
        self.txtB_TestPercentage.setObjectName("txtB_TestPercentage")

        self.txtB_TrainPercentage = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtB_TrainPercentage.setEnabled(True)
        self.txtB_TrainPercentage.setGeometry(QtCore.QRect(20, 40, 61, 22))
        self.txtB_TrainPercentage.setReadOnly(True)
        self.txtB_TrainPercentage.setObjectName("txtB_TrainPercentage")

        self.group_hlayout8.addWidget(self.txtB_TrainPercentage)
        self.group_hlayout8.addWidget(self.txtB_TestPercentage)

        self.group_hlayout9 = QtWidgets.QHBoxLayout(self.groupBox)
        self.group_hlayout9.setObjectName("group_hlayout9")
        self.group_vlayout3.addLayout(self.group_hlayout9)

        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 70, 71, 21))
        self.label_9.setObjectName("label_9")

        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(160, 70, 61, 21))
        self.label_8.setObjectName("label_8")

        self.group_hlayout9.addWidget(self.label_9)
        self.group_hlayout9.addWidget(self.label_8)

        self.group_hlayout10 = QtWidgets.QHBoxLayout(self.groupBox)
        self.group_hlayout10.setObjectName("group_hlayout10")
        self.group_vlayout3.addLayout(self.group_hlayout10)

        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 110, 51, 21))
        self.label_10.setObjectName("label_10")

        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(190, 110, 41, 20))
        self.label_11.setObjectName("label_11")

        self.group_hlayout10.addWidget(self.label_10)
        self.group_hlayout10.addWidget(self.label_11)

        self.hSld_TrainTestSplit = QtWidgets.QSlider(self.groupBox_3)
        self.hSld_TrainTestSplit.setGeometry(QtCore.QRect(30, 130, 181, 51))
        self.hSld_TrainTestSplit.setMaximum(100)
        self.hSld_TrainTestSplit.setProperty("value", 10)
        self.hSld_TrainTestSplit.setOrientation(QtCore.Qt.Horizontal)
        self.hSld_TrainTestSplit.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.hSld_TrainTestSplit.setTickInterval(10)
        self.hSld_TrainTestSplit.setObjectName("hSld_TrainTestSplit")

        self.group_vlayout3.addWidget(self.hSld_TrainTestSplit)

        self.btn_SaveDataset = QtWidgets.QPushButton(self.centralwidget)
        self.btn_SaveDataset.setGeometry(QtCore.QRect(1010, 470, 241, 51))
        self.btn_SaveDataset.setObjectName("btn_SaveDataset")

        self.btn_SaveSchema = QtWidgets.QPushButton(self.centralwidget)
        self.btn_SaveSchema.setGeometry(QtCore.QRect(1010, 530, 241, 51))
        self.btn_SaveSchema.setObjectName("btn_SaveSchema")

        self.btn_LoadSchema = QtWidgets.QPushButton(self.centralwidget)
        self.btn_LoadSchema.setGeometry(QtCore.QRect(1010, 590, 241, 51))
        self.btn_LoadSchema.setObjectName("btn_LoadSchema")

        self.btn_Help = QtWidgets.QPushButton(self.centralwidget)
        self.btn_Help.setGeometry(QtCore.QRect(1010, 650, 241, 51))
        self.btn_Help.setObjectName("btn_Help")

        self.vlayout2.addWidget(self.btn_SaveDataset)
        self.vlayout2.addWidget(self.btn_SaveSchema)
        self.vlayout2.addWidget(self.btn_LoadSchema)
        self.vlayout2.addWidget(self.btn_Help)

        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.btn_Labeler.setStyleSheet("* {\n"
"    background-color:#ffffff;\n"
"    border-radius:0px;\n"
"    border:2px solid #2982ff;\n"
"    color:#355398;\n"
"    font: 75 12pt \"MS Shell Dlg 2\";\n"
"    font-weight: bold;\n"
"    padding:12px 31px;\n"
"    text-decoration:none;\n"
"}\n"
"*:hover {\n"
"    background-color:#def2ff;\n"
"}\n"
"*:active {\n"
"    position:relative;\n"
"    top:1px;\n"
"}")

        DatasetsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(DatasetsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        DatasetsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(DatasetsWindow)
        self.statusbar.setObjectName("statusbar")
        DatasetsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DatasetsWindow)
        QtCore.QMetaObject.connectSlotsByName(DatasetsWindow)

    def retranslateUi(self, DatasetsWindow):
        _translate = QtCore.QCoreApplication.translate
        DatasetsWindow.setWindowTitle(_translate("DatasetsWindow", "Datasets | Vinci ML Tool"))
        self.btn_LoadDataset.setText(_translate("DatasetsWindow", "Load Dataset"))
        self.label.setText(_translate("DatasetsWindow", "Path:"))
        self.groupBox.setTitle(_translate("DatasetsWindow", "Dataset - Columns and Types"))
        self.label_2.setText(_translate("DatasetsWindow", "Column:"))
        self.label_3.setText(_translate("DatasetsWindow", "Transformation:"))
        self.label_4.setText(_translate("DatasetsWindow", "Data:"))
        self.label_5.setText(_translate("DatasetsWindow", "Type:"))
        item = self.tbl_Dataset.horizontalHeaderItem(0)
        item.setText(_translate("DatasetsWindow", "Column"))
        item = self.tbl_Dataset.horizontalHeaderItem(1)
        item.setText(_translate("DatasetsWindow", "Use for training?"))
        item = self.tbl_Dataset.horizontalHeaderItem(2)
        item.setText(_translate("DatasetsWindow", "Data"))
        item = self.tbl_Dataset.horizontalHeaderItem(3)
        item.setText(_translate("DatasetsWindow", "Transformation"))
        item = self.tbl_Dataset.horizontalHeaderItem(4)
        item.setText(_translate("DatasetsWindow", "Type"))
        self.btn_AddColumn.setText(_translate("DatasetsWindow", "Add Column"))
        self.btn_RemoveColumn.setText(_translate("DatasetsWindow", "Remove Column"))
        self.label_12.setText(_translate("DatasetsWindow", "TP Label:"))
        self.label_13.setText(_translate("DatasetsWindow", "Root:"))
        self.label_15.setText(_translate("DatasetsWindow", "Training:"))
        self.btn_SaveSchema.setText(_translate("DatasetsWindow", "Save Schema"))
        self.btn_LoadSchema.setText(_translate("DatasetsWindow", "Load Schema"))
        self.groupBox_3.setTitle(_translate("DatasetsWindow", "Dataset - Stratified Sampling"))
        self.label_9.setText(_translate("DatasetsWindow", "% Train"))
        self.label_8.setText(_translate("DatasetsWindow", "% Test"))
        self.label_10.setText(_translate("DatasetsWindow", "Train"))
        self.label_11.setText(_translate("DatasetsWindow", "Test"))
        self.groupBox_2.setTitle(_translate("DatasetsWindow", "Dataset - Information"))
        self.label_6.setText(_translate("DatasetsWindow", "Samples"))
        self.label_7.setText(_translate("DatasetsWindow", "Features"))
        self.label_14.setText(_translate("DatasetsWindow", "Preset:"))
        self.btn_Labeler.setText(_translate("DatasetsWindow", "LABELER"))
        self.btn_SaveDataset.setText(_translate("DatasetsWindow", "Save New Dataset"))
        self.btn_Help.setText(_translate("DatasetsWindow", "Help"))
    
import menu_res_rc