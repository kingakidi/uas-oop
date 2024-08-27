from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class IntrestWindow(QMainWindow):
    def __init__(self, widget):
        super(IntrestWindow, self).__init__()
        loadUi("ui/interest.ui", self)
        self.widget = widget
        self.btnBestMatch.clicked.connect(self.next_to_list_result_screen)
        self.btnBackToOLevel.clicked.connect(self.back_to_o_level_screen)

    def back_to_o_level_screen(self):
        self.widget.setCurrentIndex(self.widget.currentIndex()-1)

    def next_to_list_result_screen(self):
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
