# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stacked_login_signup.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/healthcare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout = QtWidgets.QGridLayout(self.page)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(263, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)
        self.widget_login = QtWidgets.QWidget(self.page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_login.sizePolicy().hasHeightForWidth())
        self.widget_login.setSizePolicy(sizePolicy)
        self.widget_login.setMinimumSize(QtCore.QSize(380, 480))
        self.widget_login.setMaximumSize(QtCore.QSize(380, 480))
        self.widget_login.setStyleSheet("QPushButton#sign_inButton_2{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(105, 16, 168, 219), stop:1 rgba(171, 81, 227, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#sign_inButton_2:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(163, 116, 186, 219), stop:1 rgba(215, 160, 255, 226));\n"
"}\n"
"QPushButton#sign_inButton_2:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(163, 116, 186, 200);\n"
"}")
        self.widget_login.setObjectName("widget_login")
        self.label_3 = QtWidgets.QLabel(self.widget_login)
        self.label_3.setGeometry(QtCore.QRect(15, 10, 350, 460))
        self.label_3.setStyleSheet("border-image: url(:/icon/Icon_Logo/bg.jpg);\n"
"border-radius:20px")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_signup_2 = QtWidgets.QLabel(self.widget_login)
        self.label_signup_2.setEnabled(True)
        self.label_signup_2.setGeometry(QtCore.QRect(30, 50, 320, 45))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_signup_2.setFont(font)
        self.label_signup_2.setTabletTracking(False)
        self.label_signup_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_signup_2.setAutoFillBackground(False)
        self.label_signup_2.setStyleSheet("background-color: rgba(0,0,0,0)\n"
"")
        self.label_signup_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signup_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_signup_2.setObjectName("label_signup_2")
        self.line_username_2 = QtWidgets.QLineEdit(self.widget_login)
        self.line_username_2.setGeometry(QtCore.QRect(80, 150, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_username_2.setFont(font)
        self.line_username_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0, 0, 0,255);\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_username_2.setText("")
        self.line_username_2.setClearButtonEnabled(True)
        self.line_username_2.setObjectName("line_username_2")
        self.linepassword_2 = QtWidgets.QLineEdit(self.widget_login)
        self.linepassword_2.setGeometry(QtCore.QRect(80, 220, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.linepassword_2.setFont(font)
        self.linepassword_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0, 0, 0,255);\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.linepassword_2.setText("")
        self.linepassword_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.linepassword_2.setClearButtonEnabled(True)
        self.linepassword_2.setObjectName("linepassword_2")
        self.sign_inButton_2 = QtWidgets.QPushButton(self.widget_login)
        self.sign_inButton_2.setGeometry(QtCore.QRect(90, 300, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.sign_inButton_2.setFont(font)
        self.sign_inButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sign_inButton_2.setObjectName("sign_inButton_2")
        self.label_createnew_2 = QtWidgets.QLabel(self.widget_login)
        self.label_createnew_2.setGeometry(QtCore.QRect(75, 370, 145, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setKerning(False)
        self.label_createnew_2.setFont(font)
        self.label_createnew_2.setAutoFillBackground(False)
        self.label_createnew_2.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.label_createnew_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_createnew_2.setObjectName("label_createnew_2")
        self.createButton_2 = QtWidgets.QPushButton(self.widget_login)
        self.createButton_2.setGeometry(QtCore.QRect(220, 365, 85, 30))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(False)
        self.createButton_2.setFont(font)
        self.createButton_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none")
        self.createButton_2.setObjectName("createButton_2")
        self.gridLayout.addWidget(self.widget_login, 1, 2, 2, 1)
        spacerItem2 = QtWidgets.QSpacerItem(263, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 3, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(393, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem5, 1, 0, 1, 1)
        self.widget_signup = QtWidgets.QWidget(self.page_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_signup.sizePolicy().hasHeightForWidth())
        self.widget_signup.setSizePolicy(sizePolicy)
        self.widget_signup.setMinimumSize(QtCore.QSize(380, 480))
        self.widget_signup.setMaximumSize(QtCore.QSize(380, 480))
        self.widget_signup.setStyleSheet("QPushButton#sign_upButton_2{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(105, 16, 168, 219), stop:1 rgba(171, 81, 227, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton#sign_upButton_2:hover{    \n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(163, 116, 186, 219), stop:1 rgba(215, 160, 255, 226));\n"
"}\n"
"QPushButton#sign_upButton_2:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(163, 116, 186, 200);\n"
"}")
        self.widget_signup.setObjectName("widget_signup")
        self.label_7 = QtWidgets.QLabel(self.widget_signup)
        self.label_7.setGeometry(QtCore.QRect(15, 10, 350, 460))
        self.label_7.setStyleSheet("border-image: url(:/icon/Icon_Logo/bg.jpg);\n"
"border-radius:20px")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_signup_4 = QtWidgets.QLabel(self.widget_signup)
        self.label_signup_4.setEnabled(True)
        self.label_signup_4.setGeometry(QtCore.QRect(30, 50, 320, 45))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.label_signup_4.setFont(font)
        self.label_signup_4.setTabletTracking(False)
        self.label_signup_4.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_signup_4.setAutoFillBackground(False)
        self.label_signup_4.setStyleSheet("background-color: rgba(0,0,0,0)\n"
"")
        self.label_signup_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_signup_4.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_signup_4.setObjectName("label_signup_4")
        self.line_username_signup_2 = QtWidgets.QLineEdit(self.widget_signup)
        self.line_username_signup_2.setGeometry(QtCore.QRect(80, 120, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_username_signup_2.setFont(font)
        self.line_username_signup_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0, 0, 0,255);\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_username_signup_2.setText("")
        self.line_username_signup_2.setClearButtonEnabled(True)
        self.line_username_signup_2.setObjectName("line_username_signup_2")
        self.line_password_signup_2 = QtWidgets.QLineEdit(self.widget_signup)
        self.line_password_signup_2.setGeometry(QtCore.QRect(80, 240, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_password_signup_2.setFont(font)
        self.line_password_signup_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0, 0, 0,255);\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_password_signup_2.setText("")
        self.line_password_signup_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_password_signup_2.setClearButtonEnabled(True)
        self.line_password_signup_2.setObjectName("line_password_signup_2")
        self.sign_upButton_2 = QtWidgets.QPushButton(self.widget_signup)
        self.sign_upButton_2.setGeometry(QtCore.QRect(90, 380, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.sign_upButton_2.setFont(font)
        self.sign_upButton_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sign_upButton_2.setObjectName("sign_upButton_2")
        self.line_email_2 = QtWidgets.QLineEdit(self.widget_signup)
        self.line_email_2.setGeometry(QtCore.QRect(80, 180, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_email_2.setFont(font)
        self.line_email_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0, 0, 0,255);\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_email_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_email_2.setText("")
        self.line_email_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.line_email_2.setClearButtonEnabled(True)
        self.line_email_2.setObjectName("line_email_2")
        self.line_confirm_2 = QtWidgets.QLineEdit(self.widget_signup)
        self.line_confirm_2.setGeometry(QtCore.QRect(80, 300, 220, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_confirm_2.setFont(font)
        self.line_confirm_2.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0, 0, 0,255);\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_confirm_2.setText("")
        self.line_confirm_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_confirm_2.setClearButtonEnabled(True)
        self.line_confirm_2.setObjectName("line_confirm_2")
        self.back_Button = QtWidgets.QPushButton(self.widget_signup)
        self.back_Button.setGeometry(QtCore.QRect(30, 60, 51, 28))
        self.back_Button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.back_Button.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.back_Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/arrow-119-48.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.back_Button.setIcon(icon1)
        self.back_Button.setIconSize(QtCore.QSize(25, 25))
        self.back_Button.setAutoDefault(False)
        self.back_Button.setDefault(False)
        self.back_Button.setFlat(False)
        self.back_Button.setObjectName("back_Button")
        self.gridLayout_4.addWidget(self.widget_signup, 1, 1, 2, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 78, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem6, 3, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(392, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem7, 2, 3, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Health Monitoring System"))
        self.label_signup_2.setText(_translate("MainWindow", "Sign in"))
        self.line_username_2.setPlaceholderText(_translate("MainWindow", "Username"))
        self.linepassword_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.sign_inButton_2.setText(_translate("MainWindow", "Sign in"))
        self.label_createnew_2.setText(_translate("MainWindow", "Don\'t have account?"))
        self.createButton_2.setText(_translate("MainWindow", "Create one"))
        self.label_signup_4.setText(_translate("MainWindow", "Sign up"))
        self.line_username_signup_2.setPlaceholderText(_translate("MainWindow", "Username"))
        self.line_password_signup_2.setPlaceholderText(_translate("MainWindow", "Password"))
        self.sign_upButton_2.setText(_translate("MainWindow", "Sign up"))
        self.line_email_2.setPlaceholderText(_translate("MainWindow", "Email"))
        self.line_confirm_2.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
import img_src_rc
