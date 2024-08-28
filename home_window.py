from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import json
import os

class HomeWindow(QMainWindow):
    def __init__(self, widget):
        super(HomeWindow, self).__init__()
        loadUi("ui/home.ui", self)
        self.widget = widget
        self.btnGetStarted.clicked.connect(self.get_started)

    def get_started(self):
        # Path to the JSON file
        json_file_path = "fields data/user_data.json"
        
        # Clear the contents of the JSON file
        if os.path.exists(json_file_path):
            with open(json_file_path, "w") as file:
                # Writing an empty dictionary to the file to clear it
                json.dump({}, file)
        
        # Move to the next widget
        self.widget.setCurrentIndex(self.widget.currentIndex() + 1)
