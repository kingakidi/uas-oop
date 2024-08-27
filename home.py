from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QStackedWidget
from PyQt5.uic import loadUi
import sys

# home screen
class HomeWindow(QMainWindow):  
    def __init__(self):
        super(HomeWindow, self).__init__()
        loadUi("ui/home.ui", self)

        self.btnGetStarted.clicked.connect(self.get_started)

    def get_started(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


# student screen 
class StudentProfile(QMainWindow):  
    def __init__(self):
        super(StudentProfile, self).__init__()
        loadUi("ui/student_profile.ui", self)  

        self.btnProfileNext.clicked.connect(self.go_to_screen_1)

    def go_to_screen_1(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

# o level screen 
class OLevelWindow(QMainWindow):  
    def __init__(self):
        super(OLevelWindow, self).__init__()
        loadUi("ui/student_profile.ui", self)  

        self.btnProfileNext.clicked.connect(self.go_to_screen_1)

    def go_to_screen_1(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


# interest screen screen 
class IntrestWindow(QMainWindow):  
    def __init__(self):
        super(IntrestWindow, self).__init__()
        loadUi("ui/interest.ui", self)  

        self.btnBestMatch.clicked.connect(self.next_to_list_result_screen)
        self.btnBackToOLevel.clicked.connect(self.back_to_o_level_screen)

    def back_to_o_level_screen(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def next_to_list_result_screen(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


# list result screen 
class ListResultWindow(QMainWindow):  
    def __init__(self):
        super(ListResultWindow, self).__init__()
        loadUi("ui/list_result.ui", self)  

        self.btnBackHome.clicked.connect(self.back_home)

    def back_home(self):
       widget.setCurrentIndex(0)

app = QApplication(sys.argv)

widget = QStackedWidget()


homeWindow = HomeWindow()
profileScreen = StudentProfile()
oLevelWindow = OLevelWindow()
interestWindow = IntrestWindow() 
listResultWindow = ListResultWindow()




widget.setFixedHeight(700)
widget.setFixedWidth(700)
widget.addWidget(homeWindow)
widget.addWidget(profileScreen)
widget.addWidget(oLevelWindow)
widget.addWidget(interestWindow)
widget.addWidget(listResultWindow)
widget.show()

sys.exit(app.exec_())
