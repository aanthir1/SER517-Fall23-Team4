# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'models.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from common_ui import add_actions_to_toolbar


class Ui_ModelsWindow(object):
    def setupUi(self, ModelsWindow):
        ModelsWindow.setObjectName("ModelsWindow")
        ModelsWindow.resize(1280, 720)
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
        ModelsWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        ModelsWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ML4CYBER_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        ModelsWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(ModelsWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.toolbar = ModelsWindow.addToolBar("TopToolBar")
        self.toolbar, self.go_back_button, self.home_button = add_actions_to_toolbar(self.toolbar, self)

        # The horizontal layout for the widget to help resizing the window
        self.vlayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.vlayout.setObjectName("hlayout")
        self.vlayout.setContentsMargins(0, 0, 0, 0)
        self.vlayout.setSpacing(0)

        self.hlayout1 = QtWidgets.QHBoxLayout()
        self.hlayout1.setObjectName("hlayout1")
        self.hlayout1.setContentsMargins(30, 20, 20, 20)
        self.hlayout1.setSpacing(10)

        self.hlayout2 = QtWidgets.QHBoxLayout()
        self.hlayout2.setObjectName("hlayout2")
        self.hlayout2.setContentsMargins(30, 20, 20, 20)
        self.hlayout2.setSpacing(10)

        self.vlayout.addLayout(self.hlayout1)
        self.vlayout.addLayout(self.hlayout2)

        #group1
        self.group_vlayout1 = QtWidgets.QVBoxLayout()
        self.group_vlayout1.setObjectName("group_vlayout1")
        self.group_vlayout1.setContentsMargins(10, 10, 10, 10)
        self.hlayout1.addLayout(self.group_vlayout1)

        self.group_vlayout2 = QtWidgets.QVBoxLayout()
        self.group_vlayout2.setObjectName("group_vlayout2")
        self.group_vlayout2.setContentsMargins(10, 10, 10, 10)
        self.hlayout1.addLayout(self.group_vlayout2) 

        self.group_hlayout1 = QtWidgets.QHBoxLayout()
        self.group_hlayout1.setObjectName("group_hlayout1")
        self.group_hlayout1.setContentsMargins(10, 10, 10, 10)
        self.group_vlayout1.addLayout(self.group_hlayout1)
        
        self.btn_LoadSchema = QtWidgets.QPushButton(self.centralwidget)
        self.btn_LoadSchema.setGeometry(QtCore.QRect(30, 20, 131, 31))
        self.btn_LoadSchema.setFont(font)
        self.btn_LoadSchema.setObjectName("btn_LoadSchema")
        self.group_hlayout1.addWidget(self.btn_LoadSchema)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 20, 51, 31))
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.group_hlayout1.addWidget(self.label)

        self.txtB_DatasetPath = QtWidgets.QLineEdit(self.centralwidget)
        self.txtB_DatasetPath.setEnabled(True)
        self.txtB_DatasetPath.setGeometry(QtCore.QRect(230, 21, 751, 31))
        self.txtB_DatasetPath.setReadOnly(True)
        self.txtB_DatasetPath.setObjectName("txtB_DatasetPath")
        self.group_hlayout1.addWidget(self.txtB_DatasetPath)

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 70, 951, 161))
        self.groupBox.setObjectName("groupBox")
        self.group_vlayout1.addWidget(self.groupBox)

        self.grp_hlayout1 = QtWidgets.QHBoxLayout()
        self.grp_hlayout1.setObjectName("group_hlayout1")
        self.grp_hlayout1.setContentsMargins(10, 10, 10, 10)
        self.groupBox.setLayout(self.grp_hlayout1)

        self.group_vlayout3 = QtWidgets.QVBoxLayout()
        self.group_vlayout3.setObjectName("group_vlayout3")
        self.group_vlayout3.setContentsMargins(0, 0, 0, 0)
        self.grp_hlayout1.addLayout(self.group_vlayout3)

        self.group_vlayout4 = QtWidgets.QVBoxLayout()
        self.group_vlayout4.setObjectName("group_vlayout4")
        self.group_vlayout4.setContentsMargins(0, 0, 0, 0)
        self.grp_hlayout1.addLayout(self.group_vlayout4)    

        self.group_hlayout2 = QtWidgets.QHBoxLayout()
        self.group_hlayout2.setObjectName("group_hlayout2")
        self.group_hlayout2.setContentsMargins(10, 0, 0, 0)
        self.group_vlayout3.addLayout(self.group_hlayout2)             

        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(80, 40, 61, 31))
        self.label_2.setObjectName("label_2")
        self.group_hlayout2.addWidget(self.label_2)

        self.sBox_Epochs = QtWidgets.QSpinBox(self.groupBox)
        self.sBox_Epochs.setGeometry(QtCore.QRect(151, 41, 111, 31))
        self.sBox_Epochs.setMaximum(10000000)
        self.sBox_Epochs.setProperty("value", 100)
        self.sBox_Epochs.setObjectName("sBox_Epochs")
        # Tooltip stating the functionality of the 'Epochs' box with tooltip duration of 6 seconds.
        self.sBox_Epochs.setToolTip("Number of complete passes a training dataset takes through the algorithm.")
        self.sBox_Epochs.setToolTipDuration(6000)
        self.group_hlayout2.addWidget(self.sBox_Epochs)

        self.group_hlayout3 = QtWidgets.QHBoxLayout()
        self.group_hlayout3.setObjectName("group_hlayout3")
        self.group_hlayout3.setContentsMargins(10, 0, 0, 0)
        self.group_vlayout3.addLayout(self.group_hlayout3)   

        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(30, 100, 111, 31))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.group_hlayout3.addWidget(self.label_4)

        self.txtB_LearningRate = QtWidgets.QLineEdit(self.groupBox)
        self.txtB_LearningRate.setGeometry(QtCore.QRect(150, 101, 111, 31))
        self.txtB_LearningRate.setObjectName("txtB_LearningRate")
        # Tooltip stating the functionality of the 'Learning Rate' box with tooltip duration of 6 seconds.
        self.txtB_LearningRate.setToolTip("The speed at which an algorithm learns the values of a parameter estimate. Optimal range - 0.0 to 1.0")
        self.txtB_LearningRate.setToolTipDuration(6000)
        self.group_hlayout3.addWidget(self.txtB_LearningRate)

        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(290, 30, 631, 101))
        self.groupBox_4.setObjectName("groupBox_4")
        self.group_vlayout4.addWidget(self.groupBox_4)

        self.group_hlayout4 = QtWidgets.QHBoxLayout()
        self.group_hlayout4.setObjectName("group_hlayout4")
        self.group_hlayout4.setContentsMargins(10, 0, 0, 0)
        self.groupBox_4.setLayout(self.group_hlayout4)   

        #continue
        self.cBox_MetricsAccuracy = QtWidgets.QCheckBox(self.groupBox_4)
        self.cBox_MetricsAccuracy.setGeometry(QtCore.QRect(70, 50, 101, 20))
        self.cBox_MetricsAccuracy.setChecked(True)
        self.cBox_MetricsAccuracy.setObjectName("cBox_MetricsAccuracy")
        self.group_hlayout4.addWidget(self.cBox_MetricsAccuracy)
        # Tooltip stating the functionality of the 'Accuracy' box with tooltip duration of 6 seconds.
        self.cBox_MetricsAccuracy.setToolTip("The measure of how often the algorithm is predicting correctly.")
        self.cBox_MetricsAccuracy.setToolTipDuration(6000)
        self.cBox_MetricsPrecision = QtWidgets.QCheckBox(self.groupBox_4)
        self.cBox_MetricsPrecision.setEnabled(False)
        self.cBox_MetricsPrecision.setGeometry(QtCore.QRect(280, 50, 101, 20))
        self.cBox_MetricsPrecision.setObjectName("cBox_MetricsPrecision")
        self.group_hlayout4.addWidget(self.cBox_MetricsPrecision)
        # Tooltip stating the functionality of the 'Precision' box with tooltip duration of 6 seconds.
        self.cBox_MetricsPrecision.setToolTip("Measure of relevant data from model's predictions.")
        self.cBox_MetricsPrecision.setToolTipDuration(6000)
        self.cBox_MetricsRecall = QtWidgets.QCheckBox(self.groupBox_4)
        self.cBox_MetricsRecall.setEnabled(False)
        self.cBox_MetricsRecall.setGeometry(QtCore.QRect(490, 50, 101, 20))
        self.cBox_MetricsRecall.setObjectName("cBox_MetricsRecall")
        self.group_hlayout4.addWidget(self.cBox_MetricsRecall)
        # Tooltip stating the functionality of the 'Recall' box with tooltip duration of 6 seconds.
        self.cBox_MetricsRecall.setToolTip("Measures the model's ability to detect positive samples.")
        self.cBox_MetricsRecall.setToolTipDuration(6000)

        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(1010, 20, 241, 211))
        self.groupBox_3.setObjectName("groupBox_3")
        self.group_vlayout2.addWidget(self.groupBox_3)   

        self.group_vlayout5 = QtWidgets.QVBoxLayout()
        self.group_vlayout5.setObjectName("group_vlayout5")
        self.group_vlayout5.setContentsMargins(0, 0, 0, 0)
        self.groupBox_3.setLayout(self.group_vlayout5)   

        self.group_hlayout5 = QtWidgets.QHBoxLayout()
        self.group_hlayout5.setObjectName("group_hlayout5")
        self.group_hlayout5.setContentsMargins(10, 0, 0, 0)
        self.group_vlayout5.addLayout(self.group_hlayout5) 

        self.group_hlayout6 = QtWidgets.QHBoxLayout()
        self.group_hlayout6.setObjectName("group_hlayout6")
        self.group_hlayout6.setContentsMargins(10, 0, 0, 0)
        self.group_vlayout5.addLayout(self.group_hlayout6)  

        self.group_hlayout7 = QtWidgets.QHBoxLayout()
        self.group_hlayout7.setObjectName("group_hlayout7")
        self.group_hlayout7.setContentsMargins(10, 0, 0, 0)
        self.group_vlayout5.addLayout(self.group_hlayout7)   

        self.txtB_InfoFeatures = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtB_InfoFeatures.setEnabled(True)
        self.txtB_InfoFeatures.setGeometry(QtCore.QRect(20, 50, 81, 22))
        self.txtB_InfoFeatures.setText("")
        self.txtB_InfoFeatures.setReadOnly(True)
        self.txtB_InfoFeatures.setObjectName("txtB_InfoFeatures")
        # Tooltip stating the functionality of the 'Features' box with tooltip duration of 6 seconds.
        self.txtB_InfoFeatures.setToolTip("Number of features in the dataset.")
        self.txtB_InfoFeatures.setToolTipDuration(6000)
        self.group_hlayout5.addWidget(self.txtB_InfoFeatures)

        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(110, 50, 111, 20))
        self.label_7.setObjectName("label_7")
        self.group_hlayout5.addWidget(self.label_7)

        self.txtB_InfoTrainSamples = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtB_InfoTrainSamples.setEnabled(True)
        self.txtB_InfoTrainSamples.setGeometry(QtCore.QRect(20, 100, 81, 22))
        self.txtB_InfoTrainSamples.setReadOnly(True)
        self.txtB_InfoTrainSamples.setObjectName("txtB_InfoTrainSamples")
        # Tooltip stating the functionality of the 'Train Samples' box with tooltip duration of 6 seconds.
        self.txtB_InfoTrainSamples.setToolTip("Number of training samples in the dataset.")
        self.txtB_InfoTrainSamples.setToolTipDuration(6000)
        self.group_hlayout6.addWidget(self.txtB_InfoTrainSamples)    

        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(110, 100, 111, 20))
        self.label_8.setObjectName("label_8")    
        self.group_hlayout6.addWidget(self.label_8)     

        self.txtB_InfoTestSamples = QtWidgets.QLineEdit(self.groupBox_3)
        self.txtB_InfoTestSamples.setEnabled(True)
        self.txtB_InfoTestSamples.setGeometry(QtCore.QRect(20, 150, 81, 22))
        self.txtB_InfoTestSamples.setReadOnly(True)
        self.txtB_InfoTestSamples.setObjectName("txtB_InfoTestSamples")
        # Tooltip stating the functionality of the 'Test Samples' box with tooltip duration of 6 seconds.
        self.txtB_InfoTestSamples.setToolTip("Number of test samples in the dataset.")
        self.txtB_InfoTestSamples.setToolTipDuration(6000)
        self.group_hlayout7.addWidget(self.txtB_InfoTestSamples)     

        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(110, 150, 111, 20))
        self.label_6.setObjectName("label_6") 
        self.group_hlayout7.addWidget(self.label_6)
        
        #horizontal 2
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 260, 1221, 381))
        self.groupBox_2.setObjectName("groupBox_2")
        self.hlayout2.addWidget(self.groupBox_2)

        self.group_vlayout6 = QtWidgets.QVBoxLayout()
        self.group_vlayout6.setObjectName("group_vlayout6")
        self.group_vlayout6.setContentsMargins(0, 0, 0, 0)
        self.groupBox_2.setLayout(self.group_vlayout6)

        self.group_hlayout8 = QtWidgets.QHBoxLayout()
        self.group_hlayout8.setObjectName("group_hlayout8")
        self.group_hlayout8.setContentsMargins(10, 0, 0, 0)
        self.group_vlayout6.addLayout(self.group_hlayout8)              

        self.btn_TrainNow = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_TrainNow.setGeometry(QtCore.QRect(30, 40, 161, 41))
        self.btn_TrainNow.setObjectName("btn_TrainNow")
        self.group_hlayout8.addWidget(self.btn_TrainNow)

        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(210, 50, 81, 21))
        self.label_3.setObjectName("label_3")
        self.group_hlayout8.addWidget(self.label_3)

        self.lbl_TrainProgress = QtWidgets.QLabel(self.groupBox_2)
        self.lbl_TrainProgress.setGeometry(QtCore.QRect(300, 50, 521, 21))
        self.lbl_TrainProgress.setObjectName("lbl_TrainProgress")
        self.group_hlayout8.addWidget(self.lbl_TrainProgress)

        self.btn_SaveModel = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_SaveModel.setEnabled(False)
        self.btn_SaveModel.setGeometry(QtCore.QRect(720, 40, 211, 41))
        self.btn_SaveModel.setObjectName("btn_SaveModel")
        self.group_hlayout8.addWidget(self.btn_SaveModel)

        self.btn_Help = QtWidgets.QPushButton(self.groupBox_2)
        self.btn_Help.setGeometry(QtCore.QRect(950, 40, 211, 41))
        self.btn_Help.setObjectName("btn_Help")
        self.group_hlayout8.addWidget(self.btn_Help)

        self.group_hlayout9 = QtWidgets.QHBoxLayout()
        self.group_hlayout9.setObjectName("group_hlayout9")
        self.group_hlayout9.setContentsMargins(10, 0, 0, 0)
        self.group_vlayout6.addLayout(self.group_hlayout9)   
        
        self.pBar_TrainProgress = QtWidgets.QProgressBar(self.groupBox_2)
        self.pBar_TrainProgress.setGeometry(QtCore.QRect(30, 110, 1161, 23))
        self.pBar_TrainProgress.setProperty("value", 24)
        self.pBar_TrainProgress.setObjectName("pBar_TrainProgress")
        # Tooltip stating the functionality of the 'Train Progress' bar with tooltip duration of 6 seconds.
        self.pBar_TrainProgress.setToolTip("Progress of model training.")
        self.pBar_TrainProgress.setToolTipDuration(6000)
        self.group_hlayout9.addWidget(self.pBar_TrainProgress)

        #-------------------------------------------------

        self.group_hlayout10 = QtWidgets.QHBoxLayout()
        self.group_hlayout10.setObjectName("group_hlayout10")
        self.group_hlayout10.setContentsMargins(10, 0, 0, 0)
        self.group_vlayout6.addLayout(self.group_hlayout10)

        self.group_hlayout11 = QtWidgets.QHBoxLayout()
        self.group_hlayout11.setObjectName("group_hlayout11")
        self.group_hlayout11.setContentsMargins(10, 0, 0, 0)
        
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 160, 1161, 191))
        self.groupBox_5.setObjectName("groupBox_5")
        self.group_hlayout10.addWidget(self.groupBox_5)
        self.groupBox_5.setLayout(self.group_hlayout11)

        self.group_vlayout7 = QtWidgets.QVBoxLayout()
        self.group_vlayout7.setObjectName("group_vlayout7")
        self.group_vlayout7.setContentsMargins(0, 0, 0, 0)

        self.group_vlayout8 = QtWidgets.QVBoxLayout()
        self.group_vlayout8.setObjectName("group_vlayout8")
        self.group_vlayout8.setContentsMargins(0, 0, 0, 0)

        self.group_hlayout11.addLayout(self.group_vlayout7)
        self.group_hlayout11.addLayout(self.group_vlayout8)

        self.label_9 = QtWidgets.QLabel(self.groupBox_5)
        self.label_9.setGeometry(QtCore.QRect(20, 60, 131, 31))
        self.label_9.setObjectName("label_9")
        self.group_vlayout7.addWidget(self.label_9)

        self.cBox_EvaluateDataset = QtWidgets.QComboBox(self.groupBox_5)
        self.cBox_EvaluateDataset.setGeometry(QtCore.QRect(20, 100, 131, 22))
        self.cBox_EvaluateDataset.setObjectName("cBox_EvaluateDataset")
        # Tooltip stating the functionality of the 'Dataset Sample' box with tooltip duration of 6 seconds.
        self.cBox_EvaluateDataset.setToolTip("Type of the dataset sample selected - Train or Test")
        self.cBox_EvaluateDataset.setToolTipDuration(6000)
        self.group_vlayout7.addWidget(self.cBox_EvaluateDataset)
        
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setGeometry(QtCore.QRect(170, 20, 961, 161))
        self.groupBox_6.setObjectName("groupBox_6")
        self.group_vlayout8.addWidget(self.groupBox_6)

        self.group_hlayout12 = QtWidgets.QHBoxLayout()
        self.group_hlayout12.setObjectName("group_hlayout12")
        self.group_hlayout12.setContentsMargins(10, 0, 0, 0)
        self.groupBox_6.setLayout(self.group_hlayout12)    

        self.group_vlayout9 = QtWidgets.QVBoxLayout()
        self.group_vlayout9.setObjectName("group_vlayout9")
        self.group_vlayout9.setContentsMargins(0, 0, 0, 0)

        self.group_vlayout10 = QtWidgets.QVBoxLayout()
        self.group_vlayout10.setObjectName("group_vlayout10")
        self.group_vlayout10.setContentsMargins(0, 0, 0, 0)

        self.group_vlayout11 = QtWidgets.QVBoxLayout()
        self.group_vlayout11.setObjectName("group_vlayout11")
        self.group_vlayout11.setContentsMargins(0, 0, 0, 0)

        self.group_vlayout12 = QtWidgets.QVBoxLayout()
        self.group_vlayout12.setObjectName("group_vlayout12")
        self.group_vlayout12.setContentsMargins(0, 0, 0, 0)

        self.group_vlayout13 = QtWidgets.QVBoxLayout()
        self.group_vlayout13.setObjectName("group_vlayout13")
        self.group_vlayout13.setContentsMargins(0, 0, 0, 0)   

        self.group_hlayout12.addLayout(self.group_vlayout9)  
        self.group_hlayout12.addLayout(self.group_vlayout10)  
        self.group_hlayout12.addLayout(self.group_vlayout11)  
        self.group_hlayout12.addLayout(self.group_vlayout12)  
        self.group_hlayout12.addLayout(self.group_vlayout13)  

        self.group_hlayout13 = QtWidgets.QHBoxLayout()
        self.group_hlayout13.setObjectName("group_hlayout13")
        self.group_hlayout13.setContentsMargins(10, 0, 0, 0)

        self.label_19 = QtWidgets.QLabel(self.groupBox_6)
        self.label_19.setGeometry(QtCore.QRect(30, 40, 191, 31))
        self.label_19.setObjectName("label_19")
        self.group_hlayout13.addWidget(self.label_19)
        
        self.dsBox_Threshold = QtWidgets.QDoubleSpinBox(self.groupBox_6)
        self.dsBox_Threshold.setGeometry(QtCore.QRect(140, 40, 121, 31))
        self.dsBox_Threshold.setDecimals(2)
        self.dsBox_Threshold.setMaximum(1.0)
        self.dsBox_Threshold.setSingleStep(0.1)
        self.dsBox_Threshold.setProperty("value", 0.5)
        self.dsBox_Threshold.setObjectName("dsBox_Threshold")
        # Tooltip stating the functionality of the 'Threshold' box with tooltip duration of 6 seconds.
        self.dsBox_Threshold.setToolTip("Helps map a logistic regression value to binary value. Optimal value - 0.50")
        self.dsBox_Threshold.setToolTipDuration(6000)
        self.group_hlayout13.addWidget(self.dsBox_Threshold)
        self.group_vlayout9.addLayout(self.group_hlayout13)

        self.txtB_EvalMetricsLoss = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtB_EvalMetricsLoss.setEnabled(True)
        self.txtB_EvalMetricsLoss.setGeometry(QtCore.QRect(30, 90, 121, 22))
        self.txtB_EvalMetricsLoss.setText("")
        self.txtB_EvalMetricsLoss.setReadOnly(True)
        self.txtB_EvalMetricsLoss.setObjectName("txtB_EvalMetricsLoss")
        # Tooltip stating the functionality of the 'Loss' box with tooltip duration of 6 seconds.
        self.txtB_EvalMetricsLoss.setToolTip("Errors made by the model for each sample.")
        self.txtB_EvalMetricsLoss.setToolTipDuration(6000)
        self.group_vlayout9.addWidget(self.txtB_EvalMetricsLoss) 

        self.label_13 = QtWidgets.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(30, 120, 91, 21))
        self.label_13.setObjectName("label_13")
        self.group_vlayout9.addWidget(self.label_13)    

        self.txtB_EvalMetricsTP = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtB_EvalMetricsTP.setEnabled(True)
        self.txtB_EvalMetricsTP.setGeometry(QtCore.QRect(330, 30, 121, 22))
        self.txtB_EvalMetricsTP.setText("")
        self.txtB_EvalMetricsTP.setObjectName("txtB_EvalMetricsTP")
        # Tooltip stating the functionality of the 'True Positive' box with tooltip duration of 6 seconds.
        self.txtB_EvalMetricsTP.setToolTip("Outcome where model correctly predicts the positive result.")
        self.txtB_EvalMetricsTP.setToolTipDuration(6000)
        self.group_vlayout10.addWidget(self.txtB_EvalMetricsTP)         

        self.label_14 = QtWidgets.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(330, 60, 121, 21))
        self.label_14.setObjectName("label_14")
        self.group_vlayout10.addWidget(self.label_14) 

        self.txtB_EvalMetricsAccuracy = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtB_EvalMetricsAccuracy.setEnabled(True)
        self.txtB_EvalMetricsAccuracy.setGeometry(QtCore.QRect(330, 90, 121, 22))
        self.txtB_EvalMetricsAccuracy.setText("")
        self.txtB_EvalMetricsAccuracy.setReadOnly(True)
        self.txtB_EvalMetricsAccuracy.setObjectName("txtB_EvalMetricsAccuracy")
        # Tooltip stating the functionality of the 'Accuracy' box with tooltip duration of 6 seconds.
        self.txtB_EvalMetricsAccuracy.setToolTip("The measure of how often the algorithm is predicting correctly.")
        self.txtB_EvalMetricsAccuracy.setToolTipDuration(6000)
        self.group_vlayout10.addWidget(self.txtB_EvalMetricsAccuracy) 

        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(330, 120, 121, 21))
        self.label_10.setObjectName("label_10")
        self.group_vlayout10.addWidget(self.label_10) 

        self.txtB_EvalMetricsTN = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtB_EvalMetricsTN.setEnabled(True)
        self.txtB_EvalMetricsTN.setGeometry(QtCore.QRect(490, 30, 121, 22))
        self.txtB_EvalMetricsTN.setText("")
        self.txtB_EvalMetricsTN.setReadOnly(True)
        self.txtB_EvalMetricsTN.setObjectName("txtB_EvalMetricsTN")
        # Tooltip stating the functionality of the 'True Negative' box with tooltip duration of 6 seconds.
        self.txtB_EvalMetricsTN.setToolTip("Outcome where model correctly predicts the negative result.")
        self.txtB_EvalMetricsTN.setToolTipDuration(6000)
        self.group_vlayout11.addWidget(self.txtB_EvalMetricsTN) 

        self.label_15 = QtWidgets.QLabel(self.groupBox_6)
        self.label_15.setGeometry(QtCore.QRect(490, 60, 121, 21))
        self.label_15.setObjectName("label_15")
        self.group_vlayout11.addWidget(self.label_15) 

        self.txtB_EvalMetricsPrecision = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtB_EvalMetricsPrecision.setEnabled(True)
        self.txtB_EvalMetricsPrecision.setGeometry(QtCore.QRect(490, 90, 121, 22))
        self.txtB_EvalMetricsPrecision.setText("")
        self.txtB_EvalMetricsPrecision.setReadOnly(True)
        self.txtB_EvalMetricsPrecision.setObjectName("txtB_EvalMetricsPrecision")
        # Tooltip stating the functionality of the 'Precision' box with tooltip duration of 6 seconds.
        self.txtB_EvalMetricsPrecision.setToolTip("Measure of relevant data from model's predictions.")
        self.txtB_EvalMetricsPrecision.setToolTipDuration(6000)
        self.group_vlayout11.addWidget(self.txtB_EvalMetricsPrecision) 
        
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(490, 120, 121, 21))
        self.label_11.setObjectName("label_11")
        self.group_vlayout11.addWidget(self.label_11) 

        self.txtB_EvalMetricsFP = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtB_EvalMetricsFP.setEnabled(True)
        self.txtB_EvalMetricsFP.setGeometry(QtCore.QRect(650, 30, 121, 22))
        self.txtB_EvalMetricsFP.setText("")
        self.txtB_EvalMetricsFP.setReadOnly(True)
        self.txtB_EvalMetricsFP.setObjectName("txtB_EvalMetricsFP")
        # Tooltip stating the functionality of the 'False Positive' box with tooltip duration of 6 seconds.
        self.txtB_EvalMetricsFP.setToolTip("Outcome where model incorrectly predicts the positive result.")
        self.txtB_EvalMetricsFP.setToolTipDuration(6000)
        self.group_vlayout12.addWidget(self.txtB_EvalMetricsFP)

        self.label_16 = QtWidgets.QLabel(self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(650, 60, 121, 21))
        self.label_16.setObjectName("label_16")
        self.group_vlayout12.addWidget(self.label_16)

        self.txtB_EvalMetricsRecall = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtB_EvalMetricsRecall.setEnabled(True)
        self.txtB_EvalMetricsRecall.setGeometry(QtCore.QRect(650, 90, 121, 22))
        self.txtB_EvalMetricsRecall.setText("")
        self.txtB_EvalMetricsRecall.setReadOnly(True)
        self.txtB_EvalMetricsRecall.setObjectName("txtB_EvalMetricsRecall")
        # Tooltip stating the functionality of the 'Recall' box with tooltip duration of 6 seconds.
        self.txtB_EvalMetricsRecall.setToolTip("Measures the model's ability to detect positive samples.")
        self.txtB_EvalMetricsRecall.setToolTipDuration(6000)
        self.group_vlayout12.addWidget(self.txtB_EvalMetricsRecall)

        self.label_12 = QtWidgets.QLabel(self.groupBox_6)
        self.label_12.setGeometry(QtCore.QRect(650, 120, 121, 21))
        self.label_12.setObjectName("label_12")
        self.group_vlayout12.addWidget(self.label_12)

        self.txtB_EvalMetricsFN = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtB_EvalMetricsFN.setEnabled(True)
        self.txtB_EvalMetricsFN.setGeometry(QtCore.QRect(810, 30, 121, 22))
        self.txtB_EvalMetricsFN.setText("")
        self.txtB_EvalMetricsFN.setReadOnly(True)
        self.txtB_EvalMetricsFN.setObjectName("txtB_EvalMetricsFN")
        # Tooltip stating the functionality of the 'False Negative' box with tooltip duration of 6 seconds.
        self.txtB_EvalMetricsFN.setToolTip("Outcome where model incorrectly predicts the negative result.")
        self.txtB_EvalMetricsFN.setToolTipDuration(6000)
        self.group_vlayout13.addWidget(self.txtB_EvalMetricsFN)

        self.label_17 = QtWidgets.QLabel(self.groupBox_6)
        self.label_17.setGeometry(QtCore.QRect(810, 60, 121, 21))
        self.label_17.setObjectName("label_17")
        self.group_vlayout13.addWidget(self.label_17)

        self.txtB_EvalMetricsF1 = QtWidgets.QLineEdit(self.groupBox_6)
        self.txtB_EvalMetricsF1.setEnabled(True)
        self.txtB_EvalMetricsF1.setGeometry(QtCore.QRect(810, 90, 121, 22))
        self.txtB_EvalMetricsF1.setText("")
        self.txtB_EvalMetricsF1.setReadOnly(True)
        self.txtB_EvalMetricsF1.setObjectName("txtB_EvalMetricsF1")
        # Tooltip stating the functionality of the 'F1 Score' box with tooltip duration of 6 seconds.
        self.txtB_EvalMetricsF1.setToolTip("Measure of a model's accuracy on a dataset.")
        self.txtB_EvalMetricsF1.setToolTipDuration(6000)
        self.group_vlayout13.addWidget(self.txtB_EvalMetricsF1)

        self.label_18 = QtWidgets.QLabel(self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(810, 120, 121, 21))
        self.label_18.setObjectName("label_18")
        self.group_vlayout13.addWidget(self.label_18)

        ModelsWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ModelsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        ModelsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ModelsWindow)
        self.statusbar.setObjectName("statusbar")
        ModelsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ModelsWindow)
        QtCore.QMetaObject.connectSlotsByName(ModelsWindow)

    def retranslateUi(self, ModelsWindow):
        _translate = QtCore.QCoreApplication.translate
        ModelsWindow.setWindowTitle(_translate("ModelsWindow", "Models | Vinci ML Tool"))
        self.btn_LoadSchema.setText(_translate("ModelsWindow", "Load Schema"))
        self.label.setText(_translate("ModelsWindow", "Path:"))
        self.groupBox.setTitle(_translate("ModelsWindow", "Models - Training Parameters"))
        self.label_2.setText(_translate("ModelsWindow", "Epochs:"))
        self.label_4.setText(_translate("ModelsWindow", "Learning Rate:"))
        self.txtB_LearningRate.setText(_translate("ModelsWindow", "0.01"))
        self.groupBox_4.setTitle(_translate("ModelsWindow", "Metrics"))
        self.cBox_MetricsAccuracy.setText(_translate("ModelsWindow", "Accuracy"))
        self.cBox_MetricsPrecision.setText(_translate("ModelsWindow", "Precision"))
        self.cBox_MetricsRecall.setText(_translate("ModelsWindow", "Recall"))
        self.groupBox_3.setTitle(_translate("ModelsWindow", "Dataset - Information"))
        self.label_6.setText(_translate("ModelsWindow", "Test Samples"))
        self.label_7.setText(_translate("ModelsWindow", "Features"))
        self.label_8.setText(_translate("ModelsWindow", "Train Samples"))
        self.groupBox_2.setTitle(_translate("ModelsWindow", "Models - Train and Save"))
        self.btn_TrainNow.setText(_translate("ModelsWindow", "Train Now"))
        self.label_3.setText(_translate("ModelsWindow", "Progress:"))
        self.lbl_TrainProgress.setText(_translate("ModelsWindow", "|"))
        self.groupBox_5.setTitle(_translate("ModelsWindow", "Evaluate"))
        self.label_9.setText(_translate("ModelsWindow", "Dataset Sample:"))
        self.groupBox_6.setTitle(_translate("ModelsWindow", "Metrics"))
        self.label_10.setText(_translate("ModelsWindow", "Accuracy"))
        self.label_11.setText(_translate("ModelsWindow", "Precision"))
        self.label_12.setText(_translate("ModelsWindow", "Recall"))
        self.label_14.setText(_translate("ModelsWindow", "True Positive"))
        self.label_15.setText(_translate("ModelsWindow", "True Negative"))
        self.label_16.setText(_translate("ModelsWindow", "False Positive"))
        self.label_17.setText(_translate("ModelsWindow", "False Negative"))
        self.label_18.setText(_translate("ModelsWindow", "F1 Score"))
        self.label_13.setText(_translate("ModelsWindow", "Loss"))
        self.label_19.setText(_translate("ModelsWindow", "Threshold:"))
        self.btn_SaveModel.setText(_translate("ModelsWindow", "Save Model"))
        self.btn_Help.setText(_translate("ModelsWindow", "Help"))
import menu_res_rc
