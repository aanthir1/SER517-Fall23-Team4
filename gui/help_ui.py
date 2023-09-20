from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(1280, 360)
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
        HelpWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        HelpWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../res/ML4CYBER_Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        HelpWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QTextEdit(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 89, 1000, 125))
        self.label.setObjectName("label")
        self.label.setReadOnly(True)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 1000, 31))
        self.label_2.setObjectName("label_2")
        HelpWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        if(HelpWindow.type == "Main"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the tool!"))
            self.label.setText(_translate("HelpWindow", "The three Buttons are used to Load the Datasets, Train and then Predict the trained model about the vulnerablities. Datasets Button redirects to the Dataset window which is mostly used to load the Dataset which is the output of the static code analyser. In the same window you can also label the dataset. After labelling the dataset you will be training the dataset by loading the schema and selecting approapriate things to save the dataset. The trained dataset is again used in the predictions to predict the accuracy of the model."))

        if(HelpWindow.type == "Labeler"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the Labeler Window"))
            self.label.setText(_translate("HelpWindow", "You can separate here the training set. Load the dataset you saved as a .csv file before, select the Stratified type and save the training set.\nLoad the training dataset you just created at the Dataset Labeling section. Each finding will be displayed separately and you will be able to assign the True or False label using the check boxes on the right. Save the dataset and close the window."))    
            
        if(HelpWindow.type == "Risk"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the Risk window."))
            self.label.setText(_translate("HelpWindow", "The risk window can be used to assess the risk of the software vulnerabilities. The CWSS(Common Weakness Scoring System) Score is the ultimate score which evaluates the threat of the software vulnerabilities. The Base Finding Score, Attack Surface Score, and Environment Score add up to form the score of the threat. Several tabs in the window display the detailed description of each of the scores shown. "))

        if(HelpWindow.type == "Prediction"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow","Here is all the information about the Prediction window."))
            self.label.setText(_translate("HelpWindow","Load the original dataset, the schema you created and the training model. Press Predict and Save Results when finished to save a .csv file with the predictions."))

        if(HelpWindow.type == "Models"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the 'Models' window."))
            self.label.setText(_translate("HelpWindow", "The model window can be used to train the dataset. Load the schema which you want to use for training. Set the epochs and learning rate. Also select the metrics you want to use. Click on Train Now to train the model and use Save Model to save the trained model to your system. The threshold can also be set and metrics information can be viewed on the bottom section of the window. "))

        if(HelpWindow.type == "Dataset"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the DataSet Window."))
            self.label.setText(_translate("HelpWindow", "Click the Datasets button, press the Load Dataset on the top left corner and select the csv or xml file that contains the dataset.(It seems to work mostly with the XMLs with the CVS you have to manually pick the “preset” on the right).The tool will recognize the type of report and preload the recommended features for best prediction accuracy.\nYou can add or remove columns and the start labelling the dataset which also can be saved to used later."))

        if(HelpWindow.type == "Risk Model"):
            HelpWindow.setWindowTitle(_translate("HelpWindow", "Help | Vinci ML Tool"))
            self.label_2.setText(_translate("HelpWindow", "Here is all the information about the 'Risk Model' window."))
            self.label.setText(_translate("HelpWindow", "The risk model window can be used to train the dataset. Load the schema which you want to use for training. Set the epochs and learning rate. Also select the metrics you want to use. Click on Train Now to train the model and use Save Model to save the trained model to your system. The threshold can also be set and metrics information can be viewed on the bottom section of the window."))

import menu_res_rc
