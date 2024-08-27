from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import json
import os

def load_json_files(directory):
    data = {}
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r') as file:
                data[filename] = json.load(file)
    return data

def save_json_file(data, filepath):
    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)

class ListResultWindow(QMainWindow):
    def __init__(self, widget):
        super(ListResultWindow, self).__init__()
        loadUi("ui/list_result.ui", self)
        self.widget = widget
        self.btnBackHome.clicked.connect(self.back_home)

        
    def back_home(self):
        self.widget.setCurrentIndex(0)
