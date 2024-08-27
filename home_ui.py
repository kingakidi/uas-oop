from PyQt5.QtWidgets import QApplication, QStackedWidget
import sys

from home_window import HomeWindow
from student_profile_window import StudentProfile
from o_level_window import OLevelWindow
from interest_window import IntrestWindow
from list_result_window import ListResultWindow

app = QApplication(sys.argv)

widget = QStackedWidget()

# Initialize all screens
homeWindow = HomeWindow(widget)
profileScreen = StudentProfile(widget)
oLevelWindow = OLevelWindow(widget)
interestWindow = IntrestWindow(widget)
listResultWindow = ListResultWindow(widget)

# Add screens to the QStackedWidget
widget.setFixedHeight(700)
widget.setFixedWidth(800)
widget.addWidget(homeWindow)
widget.addWidget(profileScreen)
widget.addWidget(oLevelWindow)
widget.addWidget(interestWindow)
widget.addWidget(listResultWindow)

widget.show()

sys.exit(app.exec_())
