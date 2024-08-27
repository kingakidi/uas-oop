from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class StudentProfile(QMainWindow):
    def __init__(self, widget):
        super(StudentProfile, self).__init__()
        loadUi("ui/student_profile.ui", self)
        self.widget = widget
        self.btnProfileNext.clicked.connect(self.go_next)

    def go_next(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
