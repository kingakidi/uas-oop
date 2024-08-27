from PyQt5.QtWidgets import QMainWindow, QComboBox
from PyQt5.uic import loadUi

subject_list =[
    "Accounting", "Agricultural Economics", "Agricultural Engineering", "Agricultural Science",
    "Anatomy", "Architecture", "Biochemistry", "Biology", "Biomedical Engineering", "Botany",
    "Business Administration", "Chemical Engineering", "Chemistry", "Civil Engineering",
    "Computer Engineering", "Computer Science", "Criminology and Security Studies", "Dentistry",
    "Economics", "Education and Chemistry", "Education and Computer Science", "Education and Economics",
    "Education and Mathematics", "Electrical/Electronic Engineering", "English Language",
    "Environmental Management", "Estate Management", "Finance", "Fisheries and Aquaculture",
    "Food Science and Technology", "Forestry and Wildlife Management", "French", "Geography",
    "Geology", "Guidance and Counseling", "History and International Studies", "Industrial Chemistry",
    "Industrial Mathematics", "Industrial Physics", "Information Technology", "International Relations",
    "Law", "Library and Information Science", "Linguistics", "Marketing", "Mass Communication",
    "Mathematics", "Mechanical Engineering", "Medical Laboratory Science", "Medicine and Surgery",
    "Microbiology", "Nursing Science", "Pharmacy", "Philosophy", "Physics", "Physiotherapy",
    "Political Science", "Psychology", "Public Administration", "Quantity Surveying", "Radiography",
    "Sociology", "Software Engineering", "Statistics", "Surveying and Geoinformatics",
    "Theatre Arts", "Urban and Regional Planning", "Veterinary Medicine", "Zoology"
]


grade_list = [
    "A1", "B2", "B3", "C4", "C5", "C6", "D7", "E8", "F9"
]

year_list = [str(year) for year in range(2024, 2003, -1)]

exam_types = [
    "WAEC",
    "NECO",
    "NABTEB",
    "NBAIS"
]
class OLevelWindow(QMainWindow):
    def __init__(self, widget):
        super(OLevelWindow, self).__init__()
        loadUi("ui/o_level.ui", self)
        self.widget = widget
        self.btnNext.clicked.connect(self.go_to_interest_window)
        self.btnBack.clicked.connect(self.back_to_profile_window)

         # Populate the subject combo boxes
        for i in range(1, 10):
            combo = self.findChild(QComboBox, f"cmbSubject_{i}")
          
            if combo:
                combo.addItems(subject_list)
                # combo.adjustSize()
        

        # grade combo 
        for i in range(1, 10):
            combo = self.findChild(QComboBox, f"grade_{i}")
            if combo:
                combo.addItems(grade_list)
                combo.setMinimumContentsLength(max(len(grade) for grade in grade_list))
        for i in range(1, 9):


            combo = self.findChild(QComboBox, f"year_{i}")
            if combo:
                combo.addItems(year_list)
                combo.setMinimumContentsLength(max(len(year) for year in year_list))


        for i in range(1, 9):
            combo = self.findChild(QComboBox, f"cmbExam_{i}")
            if combo:
                combo.addItems(exam_types)
                combo.setMinimumContentsLength(max(len(exam) for exam in exam_types))
    def back_to_profile_window(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def go_to_interest_window(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
