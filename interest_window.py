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

        # Determine the file to load based on university type
        if university_type.lower() == "federal":
            json_file = "final_federal_university.json"
        elif university_type.lower() == "state":
            json_file = "final_state_university.json"
        else:
            QMessageBox.warning(self, "Invalid University Type", "The selected university type is invalid.")
            return

        # Load the appropriate university data file
        try:
            with open(json_file, "r") as file:
                university_data = json.load(file)
        except FileNotFoundError:
            QMessageBox.warning(self, "File Not Found", f"Cannot find the file {json_file}.")
            return
        except json.JSONDecodeError:
            QMessageBox.warning(self, "File Error", f"Error decoding the JSON file {json_file}.")
            return

        # Load O-level results
        try:
            with open("fields data/o_level_data.json", "r") as file:
                o_level_data = json.load(file)
        except FileNotFoundError:
            QMessageBox.warning(self, "File Not Found", "Cannot find the O-level data file.")
            return
        except json.JSONDecodeError:
            QMessageBox.warning(self, "File Error", "Error decoding the O-level data file.")
            return

        # Find applicable universities and courses
        applicable_universities = self.find_applicable_universities(university_data, o_level_data)

        # Save the selected university and course data

        try:
            with open("fields data/result.json", "w") as file:
                json.dump(applicable_universities, file, indent=4)
        except IOError as e:
            QMessageBox.warning(self, "Save Error", f"An error occurred while saving the file: {e}.")
            return

        # Proceed to the next page
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)

    def find_applicable_universities(self, university_data, o_level_data):
        """Finds universities and courses that match the O-level results."""
        applicable_universities = {}
        
        #     this is how the structure of a single requirement looks like 
        #   "requirements": [
        #   {
        #     "subject": "Chemistry",
        #     "max_grade": "B",
        #     "percentage": 25
        #   },
        #   {
        #     "subject": "Biology",
        #     "max_grade": "C",
        #     "percentage": 20
        #   },
        #   {
        #     "subject": "Mathematics",
        #     "max_grade": "B",
        #     "percentage": 25
        #   },
        #   {
        #     "subject": "Physics",
        #     "max_grade": "C",
        #     "percentage": 20
        #   }
        # ]

        # A - 25, B-20, C-15 D-10 

        # if the o_level_data is like below for example

#         {
#     "Chemistry": "B",
#     "Biology": "C",
#     "Physics": "C",
#     "Mathematics": "B"
# }

        # that means the person have 

#         {
#     "Chemistry": 20,
#     "Biology": 15,
#     "Physics": 15,
#     "Mathematics": 20
# }

# part ii. what the requirements data show is the minimum score the person must have to enable the search for example if the score from teh olevel for Chemistry is B and the User have A, the person is qualify but if he has C is disqualify for that course 

        for university, faculties in university_data.items():
            applicable_faculties = {}
            for faculty, departments in faculties.items():
                applicable_departments = {}
                for department, department_data in departments.items():
                    requirements = department_data.get('requirements', [])
                    if self.check_requirements(o_level_data, requirements):
                        applicable_departments[department] = requirements
                if applicable_departments:
                    applicable_faculties[faculty] = applicable_departments
            if applicable_faculties:
                applicable_universities[university] = applicable_faculties
        
        return applicable_universities

    def check_requirements(self, o_level_data, requirements):
        """Checks if O-level results meet the requirements."""
        for req in requirements:
            subject = req['subject']
            max_grade = req['max_grade']
            if subject not in o_level_data or o_level_data[subject] > max_grade:
                return False
        return True
