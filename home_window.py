from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class HomeWindow(QMainWindow):
    def __init__(self, widget):
        super(HomeWindow, self).__init__()
        loadUi("ui/home.ui", self)
        self.widget = widget
        self.btnGetStarted.clicked.connect(self.get_started)

    def get_started(self):
        self.widget.setCurrentIndex(self.widget.currentIndex()+1)
