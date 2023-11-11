import pandas as pd
from groupLabelling_ui import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QWidget, QInputDialog, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal

class Impl_GroupLabelling_Window(Ui_Dialog, QtWidgets.QMainWindow):
    """Creates Group Labeler window"""
    window_closed = pyqtSignal(str)

    def __init__(self, dataset_path):
        """Initializes Group Labeler window object"""
        super(Impl_GroupLabelling_Window, self).__init__()
        self.setupUi(self)
        self.path = dataset_path
        self.displayed_records_df = pd.DataFrame()
        self.labeled_records = {}
        self.go_back_button.clicked.connect(self.goback_button_clicked)
        self.home_button.triggered.connect(self.home_button_clicked)
                                                                                     

        # Add items to the comboBox
        try:
            df = pd.read_csv(dataset_path)  # Use read_excel for Excel files
            column_names = df.columns
            self.comboBox.addItems(column_names)  # Add column names directly to the comboBox
            max_width = self.comboBox.view().sizeHintForColumn(0)
            self.comboBox.view().setMinimumWidth(max_width)
            self.comboBox.currentIndexChanged.connect(self.displayMatchingRecords)
            self.comboBox_2.currentIndexChanged.connect(self.displayMatchingRecords)
        
            self.comboBox.currentIndexChanged.connect(self.updateDropdownItems)
              # Connect the event handler
        except Exception as e:
            print("Error:", e)
        
        self.pushButton.clicked.connect(self.labelRecords)
        self.save_dataset_button.clicked.connect(self.saveDataset)
        

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

    

    def displayMatchingRecords(self):
        key = self.comboBox.currentText()
        value = self.comboBox_2.currentText()

        if key and value:
            try:
                df = pd.read_csv(self.path)
                matching_records = df[df[key] == value]

                # Clear previous content in the QTableWidget by setting row count to 0
                self.tbl_MatchingRecords.setRowCount(0)

                num_columns = len(df.columns)

                # Check if the "Output" column already exists in the original CSV file
                if "Output" not in df.columns:
                    # Add the "Output" column to the DataFrame and initialize it with None
                    df["Output"] = None
                    num_columns += 1  # Increment the column count

                # Set up the QTableWidget with the correct number of columns
                self.tbl_MatchingRecords.setColumnCount(num_columns + 1)
                header_labels = ['Number'] + df.columns.tolist()
                self.tbl_MatchingRecords.setHorizontalHeaderLabels(header_labels)
                self.tbl_MatchingRecords.verticalHeader().setVisible(False)


                # Populate the QTableWidget with matching records, including original row numbers
                for i, (original_row_number, row) in enumerate(matching_records.iterrows(), start=1):
                    self.tbl_MatchingRecords.insertRow(i - 1)
                    # Display the original row number in the first column
                    item = QtWidgets.QTableWidgetItem(str(original_row_number + 1))
                    self.tbl_MatchingRecords.setItem(i - 1, 0, item)
                    for j, val in enumerate(row):
                        item = QtWidgets.QTableWidgetItem(str(val))
                        self.tbl_MatchingRecords.setItem(i - 1, j + 1, item)
                    # Set the "Output" column to its actual value if it exists, or None otherwise
                    output_value = row.get("Output", None)
                    if output_value is not None:
                        output_item = QtWidgets.QTableWidgetItem(str(output_value))
                    else:
                        output_item = QtWidgets.QTableWidgetItem("None")
                    self.tbl_MatchingRecords.setItem(i - 1, num_columns, output_item)

            except Exception as e:
                print("Error:", e)



    def labelRecords(self):
        # This method is called when the "Label" button is clicked.

        # Check if a label has been selected
        if not self.true_radio_button.isChecked() and \
        not self.false_radio_button.isChecked() and \
        not self.clear_button.isChecked():
            # None of the radio buttons are selected, show an error message
            QMessageBox.critical(self, "Error", "Please select a label (True/False/None).")
            return

        # Get the selected label
        if self.true_radio_button.isChecked():
            label_value = "True"
        elif self.false_radio_button.isChecked():
            label_value = "False"
        elif self.clear_button.isChecked():
            label_value = "None"

        # Get the selected key and value
        key = self.comboBox.currentText()
        value = self.comboBox_2.currentText()

        if key and value:
            # Update both the QTableWidget and the labeled_records dictionary
            for row_index in range(self.tbl_MatchingRecords.rowCount()):
                number_item = self.tbl_MatchingRecords.item(row_index, 0)
                if number_item is not None:
                    original_row_number = int(number_item.text())
                    # Update the QTableWidget
                    output_item = self.tbl_MatchingRecords.item(row_index, self.tbl_MatchingRecords.columnCount() - 1)
                    if output_item is not None:
                        output_item.setText(label_value)
                    else:
                        output_item = QTableWidgetItem(label_value)
                        self.tbl_MatchingRecords.setItem(row_index, self.tbl_MatchingRecords.columnCount() - 1, output_item)

                    # Update the labeled_records dictionary
                    self.labeled_records[original_row_number] = label_value

            # Inform the user that the labels have been applied
            QMessageBox.information(self, "Info", "Labels applied to displayed records.")

    def saveDataset(self):
        # Create a QMessageBox for confirmation
        confirm_msg = QMessageBox()
        confirm_msg.setIcon(QMessageBox.Warning)
        confirm_msg.setText("Are you sure you want to save the file?")
        confirm_msg.setWindowTitle("Confirmation")
        confirm_msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        # Show the confirmation dialog and get the user's choice
        choice = confirm_msg.exec_()
        
        if choice == QMessageBox.Ok:  # User clicked "OK"
            key = self.comboBox.currentText()
            value = self.comboBox_2.currentText()

            if key and value:
                try:
                    df = pd.read_csv(self.path)
                    matching_records = df[df[key] == value]

                    if self.true_radio_button.isChecked():
                        output_value = True
                    elif self.false_radio_button.isChecked():
                        output_value = False
                    else:
                        output_value = None

                    file_dialog = QFileDialog(self, "Save Labeled Dataset File", "", "CSV Files (*.csv)")
                    file_dialog.setAcceptMode(QFileDialog.AcceptSave)

                    if file_dialog.exec_():
                        selected_file = file_dialog.selectedFiles()[0]
                        self.path = selected_file

                        matching_records.loc[:, 'Output'] = output_value
                        matching_records.to_csv(selected_file, index=False)

                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Labeled dataset file at: {} saved successfully!".format(selected_file))
                        msg.setWindowTitle("File saved")
                        msg.exec_()

                except Exception as e:
                    print("Error:", e)
        else:
            # User clicked "Cancel" or closed the dialog, do nothing
            pass
            
    def goToLabeller(self):
        self.close()

    def goback_button_clicked(self):
        self.close()

    def closeEvent(self, event):
        self.window_closed.emit(self.path)

    def home_button_clicked(self):
        self.close()


