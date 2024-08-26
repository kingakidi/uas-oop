from PyQt5 import QtCore, QtGui, QtWidgets

import resource_rc

class Ui_InstrestWindow(object):
    def setupUi(self, InstrestWindow):
        InstrestWindow.setObjectName("InstrestWindow")
        InstrestWindow.resize(574, 671)
        self.centralwidget = QtWidgets.QWidget(InstrestWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 10, 151, 61))
        self.label.setStyleSheet("color:  #00A272;\n"
"font-size: 70px;\n"
"font-weight: bold; \n"
"letter-spacing: 2px; \n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 70, 161, 16))
        self.label_2.setStyleSheet("font-size: 10px;")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 110, 521, 371))
        self.widget.setStyleSheet("background-color: white;")
        self.widget.setObjectName("widget")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 281, 31))
        self.label_8.setStyleSheet("font-weight: 600; \n"
"color: #2C2F44;\n"
"font-size: 20px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(30, 40, 331, 31))
        self.label_9.setStyleSheet("color: #687285;\n"
"")
        self.label_9.setObjectName("label_9")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 461, 231))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(40, 30, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(40, 100, 151, 16))
        self.label_4.setObjectName("label_4")
        self.cmbCourseOfStudy = QtWidgets.QComboBox(self.groupBox)
        self.cmbCourseOfStudy.setGeometry(QtCore.QRect(40, 50, 391, 31))
        self.cmbCourseOfStudy.setStyleSheet("#cmbCourseOfStudy {\n"
"\n"
"    padding: 3px;\n"
"    border-radius: 3px; \n"
"    border: 1px solid #18C474; \n"
"    \n"
"    }\n"
"\n"
"    #cmbCourseOfStudy{\n"
"        padding-left: 10px;\n"
"    }\n"
"    \n"
"    #cmbCourseOfStudy::drop-down {\n"
"        border: 0px;\n"
"    }\n"
"    \n"
"    #cmbCourseOfStudy::down-arrow {\n"
"        image: url(:/icon/arrow-204-32.ico);\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        margin-right:15px;\n"
"    }\n"
"    \n"
"    #cmbCourseOfStudy:on {\n"
"         border: 2px solid #18C474;\n"
"     }\n"
"    \n"
"    QComboBox QListView {\n"
"        font-size: 12px;\n"
"        border:1px solid rgba(0,0,0,10%);\n"
"        padding:5px;\n"
"        background-color: #fff;\n"
"        outline: 0px;  \n"
"    }\n"
"    \n"
"    QComboBox QListView::item{\n"
"        padding-left:10px;\n"
"        background-color:#FFFFFF;\n"
"    }\n"
"    QComboBox QListView::item:hover{\n"
"       background-color:#1e90ff;\n"
"    }\n"
"    QComboBox QListView::item:selected{\n"
"       background-color:#1e90ff;\n"
"    }")
        self.cmbCourseOfStudy.setObjectName("cmbCourseOfStudy")
        self.cmbCourseOfStudy.addItem("")
        self.cmbCourseOfStudy.addItem("")
        self.cmbCourseOfStudy.addItem("")
        self.cmbCourseOfStudy.addItem("")
        self.cmbCourseOfStudy.addItem("")
        self.cmbUniversityType = QtWidgets.QComboBox(self.groupBox)
        self.cmbUniversityType.setGeometry(QtCore.QRect(40, 120, 391, 31))
        self.cmbUniversityType.setStyleSheet("#cmbUniversityType {\n"
"\n"
"    padding: 3px;\n"
"    border-radius: 3px; \n"
"    border: 1px solid #18C474; \n"
"    \n"
"    }\n"
"    \n"
"\n"
"    #cmbUniversityType{\n"
"        padding-left: 10px;\n"
"    }\n"
"\n"
"    #cmbUniversityType::drop-down {\n"
"        border: 0px;\n"
"    }\n"
"    \n"
"    #cmbUniversityType::down-arrow {\n"
"        image: url(:/icon/arrow-204-32.ico);\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        margin-right:15px;\n"
"    }\n"
"    \n"
"    #cmbUniversityType:on {\n"
"         border: 2px solid #18C474;\n"
"     }\n"
"    \n"
"    QComboBox QListView {\n"
"        font-size: 12px;\n"
"        border:1px solid rgba(0,0,0,10%);\n"
"        padding:5px;\n"
"        background-color: #fff;\n"
"        outline: 0px;  \n"
"    }\n"
"    \n"
"    QComboBox QListView::item{\n"
"        padding-left:10px;\n"
"        background-color:#FFFFFF;\n"
"    }\n"
"    QComboBox QListView::item:hover{\n"
"       background-color:#1e90ff;\n"
"    }\n"
"    QComboBox QListView::item:selected{\n"
"       background-color:#1e90ff;\n"
"    }")
        self.cmbUniversityType.setObjectName("cmbUniversityType")
        self.cmbUniversityType.addItem("")
        self.cmbUniversityType.addItem("")
        self.cmbUniversityType.addItem("")
        self.cmbUniversityType.addItem("")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(40, 170, 75, 41))
        self.pushButton.setStyleSheet("background: #F4F5F6;\n"
"padding: 5px; \n"
"border-radius: 3px;\n"
"color: #2C2F44;\n"
"font-weight: 400;\n"
"font-size: 10px;\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 170, 121, 41))
        self.pushButton_2.setStyleSheet("background: #00A272;\n"
"padding: 5px; \n"
"border-radius: 3px;\n"
"color: #fff;\n"
"font-weight: 400;\n"
"font-size: 10px;\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 620, 571, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("text-align: center;")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        InstrestWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(InstrestWindow)
        self.statusbar.setObjectName("statusbar")
        InstrestWindow.setStatusBar(self.statusbar)

        self.retranslateUi(InstrestWindow)
        QtCore.QMetaObject.connectSlotsByName(InstrestWindow)

    def retranslateUi(self, InstrestWindow):
        _translate = QtCore.QCoreApplication.translate
        InstrestWindow.setWindowTitle(_translate("InstrestWindow", "MainWindow"))
        self.label.setText(_translate("InstrestWindow", "UAS"))
        self.label_2.setText(_translate("InstrestWindow", "University  Admission  Software"))
        self.label_8.setText(_translate("InstrestWindow", "Tell us about your Interests and Preferences"))
        self.label_9.setText(_translate("InstrestWindow", "Help us understand your academic interests and  \n"
"university preferences to provide personalized recommendations."))
        self.label_3.setText(_translate("InstrestWindow", "Preferred Faculty of Study"))
        self.label_4.setText(_translate("InstrestWindow", "Preferred University Type"))
        self.cmbCourseOfStudy.setItemText(0, _translate("InstrestWindow", "- Select - "))
        self.cmbCourseOfStudy.setItemText(1, _translate("InstrestWindow", "Art"))
        self.cmbCourseOfStudy.setItemText(2, _translate("InstrestWindow", "Scient"))
        self.cmbCourseOfStudy.setItemText(3, _translate("InstrestWindow", "Socials Science"))
        self.cmbCourseOfStudy.setItemText(4, _translate("InstrestWindow", "Business"))
        self.cmbUniversityType.setItemText(0, _translate("InstrestWindow", "- Select -"))
        self.cmbUniversityType.setItemText(1, _translate("InstrestWindow", "Federal University"))
        self.cmbUniversityType.setItemText(2, _translate("InstrestWindow", "State University"))
        self.cmbUniversityType.setItemText(3, _translate("InstrestWindow", "Private University"))
        self.pushButton.setText(_translate("InstrestWindow", " Back "))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.pushButton_2.setText(_translate("InstrestWindow", "Find Your Best Match"))
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.lineEdit.setText(_translate("InstrestWindow", "© Copyright 2024 uas.abu.edu.ng. All rights reserved."))

        
        self.pushButton.clicked.connect(self.get_o_level)
        self.pushButton_2.clicked.connect(self.get_result_list)

    def get_o_level(self):
        print('you clicked')
        import o_level_ui
        from PyQt5.QtWidgets import QMainWindow
        self.o_level_window = QMainWindow()
        ui = o_level_ui.Ui_OLevelResultWindow()
        ui.setupUi(self.o_level_window)
        self.o_level_window.show()
        InstrestWindow.close()
        
    def get_result_list(self):
        print('you clicked')
        import list_result_ui
        from PyQt5.QtWidgets import QMainWindow
        self.result_list_window = QMainWindow()
        ui = list_result_ui.Ui_ListResultWindow()
        ui.setupUi(self.result_list_window)
        self.result_list_window.show()
        InstrestWindow.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    InstrestWindow = QtWidgets.QMainWindow()
    ui = Ui_InstrestWindow()
    ui.setupUi(InstrestWindow)
    InstrestWindow.show()
    sys.exit(app.exec_())
