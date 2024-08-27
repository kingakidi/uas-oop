from PyQt5.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QGroupBox, QHBoxLayout
from PyQt5.uic import loadUi
import json
import os

class ListResultWindow(QMainWindow):
    def __init__(self, widget):
        super(ListResultWindow, self).__init__()
        loadUi("ui/list_result.ui", self)
        self.widget = widget
        self.btnBackHome.clicked.connect(self.back_home)

        # Create a QVBoxLayout for the group box
        self.layout = QVBoxLayout(self.grpShowResult)
        
        # Create the QTableWidget
        self.tableWidget = QTableWidget()
        self.layout.addWidget(self.tableWidget)

        # Load results and populate the table
        self.load_results()

    def load_results(self):
        json_file = "fields data/result.json"

        if not os.path.exists(json_file):
            print("File not found.")
            return None

        try:
            with open(json_file, "r") as file:
                results = json.load(file)
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")
            return None
        except IOError as e:
            print(f"Error reading the file: {e}.")
            return None

        if results is not None:
            print("Results loaded successfully:")
            print(results)
            self.populate_table(results, 'Biochemistry')  # Adjust the department as needed
        else:
            print("Failed to load results.")

    def populate_table(self, data, department_filter):
        if not data:
            return

        # Flatten the nested dictionary into a list of rows
        rows = []
        for university, fields in data.items():
            for field, departments in fields.items():
                if department_filter in departments:
                    subjects = departments[department_filter]
                    total_percentage = sum(subject.get('percentage', 0) for subject in subjects)

                    for subject in subjects:
                        row = [
                            university,
                            field,
                            department_filter,
                            subject.get('subject', ''),
                            subject.get('max_grade', ''),
                            subject.get('percentage', ''),
                            total_percentage
                        ]
                        rows.append(row)

        if rows:
            # Set table headers
            headers = ['University', 'Field', 'Department', 'Subject', 'Max Grade', 'Percentage', 'Total Percentage']
            self.tableWidget.setColumnCount(len(headers))
            self.tableWidget.setHorizontalHeaderLabels(headers)

            # Set the row count
            self.tableWidget.setRowCount(len(rows))

            # Populate the table with data
            for row_idx, row_data in enumerate(rows):
                for col_idx, item in enumerate(row_data):
                    table_item = QTableWidgetItem(str(item))
                    self.tableWidget.setItem(row_idx, col_idx, table_item)

    def back_home(self):
        self.widget.setCurrentIndex(0)
