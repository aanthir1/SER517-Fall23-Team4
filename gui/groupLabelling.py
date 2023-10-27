import pandas as pd
from groupLabelling_ui import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QInputDialog

class Impl_GroupLabelling_Window(Ui_Dialog, QtWidgets.QMainWindow):
    """Creates Group Labeler window"""

    def __init__(self, dataset_path):
        """Initializes Group Labeler window object"""
        super(Impl_GroupLabelling_Window, self).__init__()
        self.setupUi(self)
        self.path = dataset_path
        self.pushButton.clicked.connect(self.displayMatchingRecordsfromfile)
        self.save_dataset_button.clicked.connect(self.saveDataset)

        # Add items to the comboBox
        try:
            df = pd.read_csv(dataset_path)  # Use read_excel for Excel files
            column_names = df.columns
            self.comboBox.addItems(column_names)  # Add column names directly to the comboBox
            max_width = self.comboBox.view().sizeHintForColumn(0)
            self.comboBox.view().setMinimumWidth(max_width)
            self.comboBox.currentIndexChanged.connect(self.updateDropdownItems)  # Connect the event handler
        except Exception as e:
            print("Error:", e)
    
    def updateDropdownItems(self, index):
        """Update the dropdown with unique values from the selected column"""
        selected_column = self.comboBox.currentText()  # Get the selected column name
        if selected_column:
            try:
                df = pd.read_csv(self.path)
                unique_values = df[selected_column].unique()
                self.comboBox_2.clear()  # Clear the existing items
                self.comboBox_2.addItems([str(val) for val in unique_values])
                max_width = self.comboBox_2.view().sizeHintForColumn(0)
                self.comboBox_2.view().setMinimumWidth(max_width)

            except Exception as e:
                print("Error:", e)

    def displayMatchingRecordsfromfile(self):
        key = self.comboBox.currentText()
        value = self.comboBox_2.currentText()

        if key and value:
            try:
                df = pd.read_csv(self.path)
                matching_records = df[(df[key] == value)]
                num_columns = len(df.columns)

                # Clear previous content in the QTableWidget
                self.tbl_MatchingRecords.setRowCount(0)
                self.tbl_MatchingRecords.setColumnCount(num_columns + 1)
                header_labels = df.columns.tolist() + ["Output"]
                self.tbl_MatchingRecords.setHorizontalHeaderLabels(header_labels)

                # Get the selected radio button
                if self.true_radio_button.isChecked():
                    output_value = "True"
                elif self.false_radio_button.isChecked():
                    output_value = "False"
                else:
                    output_value = ""  # Handle this case based on your requirements

                # Populate the QTableWidget with matching records and set the output value
                for i, (_, row) in enumerate(matching_records.iterrows()):
                    self.tbl_MatchingRecords.insertRow(i)
                    for j, val in enumerate(row):
                        item = QtWidgets.QTableWidgetItem(str(val))
                        self.tbl_MatchingRecords.setItem(i, j, item)
                    output_item = QtWidgets.QTableWidgetItem(output_value)
                    self.tbl_MatchingRecords.setItem(i, num_columns, output_item)

            except Exception as e:
                print("Error:", e)
                
    def saveDataset(self):
        key = self.comboBox.currentText()
        value = self.comboBox_2.currentText()

        if key and value:
            try:
                df = pd.read_csv(self.path)
                matching_records = df[df[key] == value]

                # Get the selected radio button
                if self.true_radio_button.isChecked():
                    output_value = True
                elif self.false_radio_button.isChecked():
                    output_value = False
                else:
                    output_value = None  # Handle this case based on your requirements

                # Update the 'Output' column with the selected output value using .loc
                matching_records.loc[:, 'Output'] = output_value

                # Create a file dialog to allow the user to choose the save location
                file_dialog = QFileDialog(self, "Save Labeled Dataset File", "", "CSV Files (*.csv)")
                file_dialog.setAcceptMode(QFileDialog.AcceptSave)

                if file_dialog.exec_():
                    selected_file = file_dialog.selectedFiles()[0]

                    # Prompt the user for a custom file name
                    custom_file_name, _ = QInputDialog.getText(self, "Custom File Name", "Enter a custom file name:")

                    if custom_file_name:
                        selected_file = selected_file.rsplit("/", 1)[0] + "/" + custom_file_name + ".csv"

                        # Save the updated DataFrame to the selected file
                        matching_records.to_csv(selected_file, index=False)

                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Labeled dataset file at: {} saved successfully!".format(selected_file))
                        msg.setWindowTitle("File saved")
                        msg.exec_()

            except Exception as e:
                print("Error:", e)
