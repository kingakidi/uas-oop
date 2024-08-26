from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HomeWindow(object):
    def setupUi(self, HomeWindow):
        HomeWindow.setObjectName("HomeWindow")
        HomeWindow.resize(504, 474)
        self.centralwidget = QtWidgets.QWidget(HomeWindow)
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
        self.label_2.setGeometry(QtCore.QRect(180, 70, 151, 16))
        self.label_2.setStyleSheet("font-size: 10px;")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 110, 401, 231))
        self.widget.setStyleSheet("background-color: white;")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 161, 21))
        self.label_3.setStyleSheet("color: #00A272;\n"
"font-size: 20px;\n"
"font-weight: 500;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 191, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 361, 61))
        self.label_5.setStyleSheet("color: rgb(116, 116, 116);\n"
"line-height: 15px;")
        self.label_5.setObjectName("label_5")
        self.btnGetStarted = QtWidgets.QPushButton(self.widget)
        self.btnGetStarted.setGeometry(QtCore.QRect(20, 170, 361, 41))
        font = QtGui.QFont()
        font.setFamily("Inter")
        font.setPointSize(-1)
        font.setKerning(True)
        self.btnGetStarted.setFont(font)
        self.btnGetStarted.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btnGetStarted.setAutoFillBackground(False)
        self.btnGetStarted.setStyleSheet("background-color: #00A272; \n"
"padding: 4px; \n"
"border-radius: 3px; \n"
"color: white; \n"
"font-size: 13px; \n"
"cursor:pointer;\n"
"font-weight: medium;\n"
"font-family: Inter")
        self.btnGetStarted.setObjectName("btnGetStarted")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 419, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(7)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("text-align: center;")
        self.lineEdit.setFrame(False)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")
        HomeWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(HomeWindow)
        self.statusbar.setObjectName("statusbar")
        HomeWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomeWindow)
        QtCore.QMetaObject.connectSlotsByName(HomeWindow)

    def retranslateUi(self, HomeWindow):
        _translate = QtCore.QCoreApplication.translate
        HomeWindow.setWindowTitle(_translate("HomeWindow", "MainWindow"))
        self.label.setText(_translate("HomeWindow", "UAS"))
        self.label_2.setText(_translate("HomeWindow", "University  Adminssion  Software"))
        self.label_3.setText(_translate("HomeWindow", "Welcome to UAS"))
        self.label_4.setText(_translate("HomeWindow", "Your Gateway to the Perfect University!"))
        self.label_5.setText(_translate("HomeWindow", "Easily discover universities that match your O\'Level results \n"
"and personal preferences. Let UAS guide you through finding the perfect \n"
"institution to achieve your academic dreams."))
        self.btnGetStarted.setText(_translate("HomeWindow", "Get Started"))
        self.lineEdit.setText(_translate("HomeWindow", "© Copyright 2024 uas.abu.edu.ng. All rights reserved."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HomeWindow = QtWidgets.QMainWindow()
    ui = Ui_HomeWindow()
    ui.setupUi(HomeWindow)
    HomeWindow.show()
    sys.exit(app.exec_())
