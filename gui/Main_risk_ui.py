from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QLabel, QLineEdit, QFormLayout, QTabWidget, QGroupBox, QTableWidgetItem

class RiskWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Risk Window')
        self.setMinimumSize(1280, 720)

        # Set up Load Dataset layout
        self.setupLoadDatasetLayout()

        # Set up Sample Info and Attack Surface layouts
        self.setupTabsLayout()
     

    def setupLoadDatasetLayout(self):
        # Create a button named "Load Dataset"
        self.load_dataset_button = QtWidgets.QPushButton(self)
        self.load_dataset_button.setGeometry(QtCore.QRect(50, 50, 200, 100))
        self.load_dataset_button.setText("Load Dataset")
        self.load_dataset_button.clicked.connect(self.btn_Load_Dataset_clicked)

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

    def setupTabsLayout(self):
        # Creating the tab widget
        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setGeometry(20, 200, 981, 500)

        # Call the functions to set up the Sample Info and Attack Surface tabs
        self.setupSampleInfoTab()
        self.setupAttackSurfaceTab()
        self.setupBaseFindingTab()
        self.setupEnvironmentalTab()

    def setupSampleInfoTab(self):
        # Sample Info tab
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabWidget.addTab(self.tab, "Sample Info")

        # Layout for Sample Info tab
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout.setObjectName("verticalLayout")

        # Group box for sample information
        self.group_box = QtWidgets.QGroupBox("Group Labelling", self.tab)
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)

        # Adding labels and input fields for Sample Info inside the group box
        self.label_2 = QtWidgets.QLabel("Label 1:", self.tab)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)

        self.group_box_layout.addWidget(self.label_2)
        self.group_box_layout.addWidget(self.lineEdit_2)

        # Add the group box to the vertical layout
        self.verticalLayout.addWidget(self.group_box)

    def setupAttackSurfaceTab(self):
        # Attack Surface tab without the inside block for brevity
        self.attack_surface_tab = QWidget()
        self.attack_surface_tab.setObjectName("attack_surface_tab")
        self.tabWidget.addTab(self.attack_surface_tab, "Attack Surface")

        self.verticalLayout_attack_surface = QVBoxLayout(self.attack_surface_tab)
        self.verticalLayout_attack_surface.setObjectName("verticalLayout_attack_surface")

    def setupBaseFindingTab(self):
        # Attack Surface tab without the inside block for brevity
        self.base_finding_tab = QWidget()
        self.base_finding_tab.setObjectName("base_finding_tab")
        self.tabWidget.addTab(self.base_finding_tab, "Base Finding")

        self.verticalLayout_base_finding = QVBoxLayout(self.base_finding_tab)
        self.verticalLayout_base_finding.setObjectName("verticalLayout_base_finding")

        # Create the table widget without row and column headers
        self.table_base_finding = QTableWidget(5, 5)  # 5 rows, 5 columns
        self.table_base_finding.setHorizontalHeaderLabels(["", "", "", "", ""])  # Empty headers

        # Disable editing for all cells in the table
        for i in range(self.table_base_finding.rowCount()):
            for j in range(self.table_base_finding.columnCount()):
                item = QTableWidgetItem()
                item.setFlags(item.flags() & ~QtCore.Qt.ItemIsEditable)
                self.table_base_finding.setItem(i, j, item)

        self.verticalLayout_base_finding.addWidget(self.table_base_finding)


    def setupEnvironmentalTab(self):
        self.environmental_tab = QWidget()
        self.environmental_tab.setObjectName("environmental_tab")
        self.tabWidget.addTab(self.environmental_tab, "Environmental")

        self.verticalLayout_environmental = QVBoxLayout(self.environmental_tab)
        self.verticalLayout_environmental.setObjectName("verticalLayout_environmental")



    def btn_Load_Dataset_clicked(self):
        """Clicked event on the Load Dataset button.
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


