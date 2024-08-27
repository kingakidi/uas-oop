from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

class ListResultWindow(QMainWindow):
    def __init__(self, widget):
        super(ListResultWindow, self).__init__()
        loadUi("ui/list_result.ui", self)
        self.widget = widget
        self.btnBackHome.clicked.connect(self.back_home)

        
    def back_home(self):
        self.widget.setCurrentIndex(0)
