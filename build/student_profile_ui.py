from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StudentProfileWindow(object):
    def setupUi(self, StudentProfileWindow):
        StudentProfileWindow.setObjectName("StudentProfileWindow")
        StudentProfileWindow.resize(503, 624)
        self.centralwidget = QtWidgets.QWidget(StudentProfileWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 151, 61))
        self.label.setStyleSheet("color:  #00A272;\n"
"font-size: 70px;\n"
"font-weight: bold; \n"
"letter-spacing: 2px; \n"
"\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 70, 161, 16))
        self.label_2.setStyleSheet("font-size: 10px;")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 120, 421, 421))
        self.widget.setStyleSheet("background-color: white;")
        self.widget.setObjectName("widget")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(30, 80, 361, 331))
        self.groupBox.setTitle("")
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 81, 20))
        self.label_3.setStyleSheet("color:rgb(58, 58, 76);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 81, 20))
        self.label_4.setStyleSheet("color:rgb(58, 58, 76);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 81, 20))
        self.label_5.setStyleSheet("color: rgb(58, 59, 76)")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 200, 101, 16))
        self.label_6.setStyleSheet("color:rgb(58, 58, 76);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(190, 200, 101, 16))
        self.label_7.setStyleSheet("color:rgb(58, 58, 76);")
        self.label_7.setObjectName("label_7")
        self.btnProfileNext = QtWidgets.QPushButton(self.groupBox)
        self.btnProfileNext.setGeometry(QtCore.QRect(10, 280, 331, 41))
        self.btnProfileNext.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnProfileNext.setAutoFillBackground(False)
        self.btnProfileNext.setStyleSheet("background-color: #f4f5f6; \n"
"padding: 6px; \n"
"border-radius: 4px; \n"
"color: #8b9787; \n"
"font-size: 10px; \n"
"cursor:pointer;\n"
"")
        self.btnProfileNext.setObjectName("btnProfileNext")
        self.dateOfBirth = QtWidgets.QDateEdit(self.groupBox)
        self.dateOfBirth.setGeometry(QtCore.QRect(10, 150, 331, 31))
        self.dateOfBirth.setStyleSheet("padding: 3px;\n"
"border-radius: 3px; \n"
"border: 1px solid #18C474; ")
        self.dateOfBirth.setDisplayFormat("M/d/yyyy")
        self.dateOfBirth.setObjectName("dateOfBirth")
        self.cmbState = QtWidgets.QComboBox(self.groupBox)
        self.cmbState.setGeometry(QtCore.QRect(10, 220, 151, 31))
        self.cmbState.setAcceptDrops(False)
        self.cmbState.setStyleSheet("#cmbState {\n"
"\n"
"padding: 3px;\n"
"border-radius: 3px; \n"
"border: 1px solid #18C474; \n"
"\n"
"}\n"
"\n"
"#cmbState::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#cmbState::down-arrow {\n"
"    image: url(:/icon/arrow-204-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right:15px;\n"
"}\n"
"\n"
"#cmbState:on {\n"
"     border: 2px solid #18C474;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"    font-size: 12px;\n"
"    border:1px solid rgba(0,0,0,10%);\n"
"    padding:5px;\n"
"    background-color: #fff;\n"
"    outline: 0px;  \n"
"}\n"
"\n"
"QComboBox QListView::item{\n"
"    padding-left:10px;\n"
"    background-color:#FFFFFF;\n"
"}\n"
"QComboBox QListView::item:hover{\n"
"   background-color:#1e90ff;\n"
"}\n"
"QComboBox QListView::item:selected{\n"
"   background-color:#1e90ff;\n"
"}")
        self.cmbState.setFrame(False)
        self.cmbState.setObjectName("cmbState")
        self.cmbState.addItem("")
        self.cmbState.addItem("")
        self.cmbLga = QtWidgets.QComboBox(self.groupBox)
        self.cmbLga.setGeometry(QtCore.QRect(190, 220, 151, 31))
        self.cmbLga.setStyleSheet("#cmbLga {\n"
"\n"
"    padding: 3px;\n"
"    border-radius: 3px; \n"
"    border: 1px solid #18C474; \n"
"    \n"
"    }\n"
"    \n"
"    #cmbLga::drop-down {\n"
"        border: 0px;\n"
"    }\n"
"    \n"
"    #cmbLga::down-arrow {\n"
"        image: url(:/icon/arrow-204-32.ico);\n"
"        width: 12px;\n"
"        height: 12px;\n"
"        margin-right:15px;\n"
"    }\n"
"    \n"
"    #cmbLga:on {\n"
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
        self.cmbLga.setFrame(False)
        self.cmbLga.setObjectName("cmbLga")
        self.firstName = QtWidgets.QLineEdit(self.groupBox)
        self.firstName.setGeometry(QtCore.QRect(10, 30, 331, 31))
        self.firstName.setStyleSheet("padding: 3px;\n"
"border-radius: 3px; \n"
"border: 1px solid #18C474; ")
        self.firstName.setFrame(True)
        self.firstName.setObjectName("firstName")
        self.lastName = QtWidgets.QLineEdit(self.groupBox)
        self.lastName.setGeometry(QtCore.QRect(10, 90, 331, 31))
        self.lastName.setStyleSheet("padding: 3px;\n"
"border-radius: 3px; \n"
"border: 1px solid #18C474; ")
        self.lastName.setObjectName("lastName")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(30, 10, 241, 31))
        self.label_8.setStyleSheet("font-weight: 600; \n"
"color: #2C2F44;\n"
"font-size: 20px;")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(30, 40, 361, 16))
        self.label_9.setStyleSheet("color: #687285;\n"
"")
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 560, 501, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("text-align: center;")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        StudentProfileWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(StudentProfileWindow)
        self.statusbar.setObjectName("statusbar")
        StudentProfileWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StudentProfileWindow)
        QtCore.QMetaObject.connectSlotsByName(StudentProfileWindow)

    def retranslateUi(self, StudentProfileWindow):
        _translate = QtCore.QCoreApplication.translate
        StudentProfileWindow.setWindowTitle(_translate("StudentProfileWindow", "MainWindow"))
        self.label.setText(_translate("StudentProfileWindow", "UAS"))
        self.label_2.setText(_translate("StudentProfileWindow", "University  Adminssion  Software"))
        self.label_3.setText(_translate("StudentProfileWindow", "First name:"))
        self.label_4.setText(_translate("StudentProfileWindow", "Last Name:"))
        self.label_5.setText(_translate("StudentProfileWindow", "Date of Birth:"))
        self.label_6.setText(_translate("StudentProfileWindow", "State of Origin"))
        self.label_7.setText(_translate("StudentProfileWindow", "Local Govt. "))
        self.btnProfileNext.setText(_translate("StudentProfileWindow", "Next"))
        self.cmbState.setItemText(0, _translate("StudentProfileWindow", "Kogi"))
        self.cmbState.setItemText(1, _translate("StudentProfileWindow", "Abuja"))
        self.firstName.setPlaceholderText(_translate("StudentProfileWindow", "e.g John"))
        self.lastName.setPlaceholderText(_translate("StudentProfileWindow", "e.g Doe"))
        self.label_8.setText(_translate("StudentProfileWindow", "Tell us about yourself"))
        self.label_9.setText(_translate("StudentProfileWindow", "We need a few details to help match you with the best universities."))
        self.lineEdit.setText(_translate("StudentProfileWindow", "© Copyright 2024 uas.abu.edu.ng. All rights reserved."))
import resource_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentProfileWindow = QtWidgets.QMainWindow()
    ui = Ui_StudentProfileWindow()
    ui.setupUi(StudentProfileWindow)
    StudentProfileWindow.show()
    sys.exit(app.exec_())
