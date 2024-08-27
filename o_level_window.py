from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class OLevelWindow(QMainWindow):
    def __init__(self, widget):
        super(OLevelWindow, self).__init__()
        loadUi("ui/o_level.ui", self)
        self.widget = widget
        self.btnNext.clicked.connect(self.go_to_interest_window)
        self.btnBack.clicked.connect(self.back_to_profile_window)

    def back_to_profile_window(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() - 1)

    def go_to_interest_window(self):
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
