from PyQt5.QtWidgets import QMainWindow, QComboBox, QMessageBox
from PyQt5.uic import loadUi
import json

class IntrestWindow(QMainWindow):
    def __init__(self, widget):
        super(IntrestWindow, self).__init__()
        loadUi("ui/interest.ui", self)
        self.widget = widget

        self.faculty = self.findChild(QComboBox, "cmbFaculty")
        self.universityType = self.findChild(QComboBox, "cmbUniversityType")

        self.btnBestMatch.clicked.connect(self.next_to_list_result_screen)
        self.btnBackToOLevel.clicked.connect(self.back_to_o_level_screen)

    def back_to_o_level_screen(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def next_to_list_result_screen(self):
        faculty_value = self.faculty.currentText()
        university_type = self.universityType.currentText()

        # Check if any of the fields are empty
        if faculty_value == "" or university_type == "":
            QMessageBox.warning(self, "All Fields Required", "Please select both Faculty and University Type.")
            return  # Stop execution if any field is empty

        data_value = {
            "faculty": faculty_value,
            "university type": university_type
        }

        # Save data to interest_data.json
        with open("fields data/interest_data.json", "w") as file:
            json.dump(data_value, file, indent=4)

        # Proceed to the next page
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
