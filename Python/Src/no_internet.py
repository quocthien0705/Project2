# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import img_src_rc

class Ui_no_internet(object):
    def setupUi(self, no_internet):
        screen_resolution = QtWidgets.QApplication.desktop().screenGeometry()
        screen_width, screen_height = screen_resolution.width(), screen_resolution.height()
        screen_center_x = screen_width//2
        screen_center_y = screen_height//2
        no_internet.setObjectName("no_internet")
        no_internet.resize(1920, 1055)
        no_internet.setWindowTitle("Health Monitoring System")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/healthcare.png"), QtGui.QIcon.Selected, QtGui.QIcon.On)
        no_internet.setWindowIcon(icon)
        no_internet.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label = QtWidgets.QLabel(no_internet)
        self.label.setGeometry(QtCore.QRect(928, 465, 64, 64))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"image: url(:/icon/Icon_Logo/no-internet.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(no_internet)
        self.label_2.setGeometry(QtCore.QRect(810, 540, 300, 20))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setKerning(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(no_internet)
        self.label_3.setGeometry(QtCore.QRect(635, 565, 650, 40))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(16)
        font.setKerning(False)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(no_internet)
        QtCore.QMetaObject.connectSlotsByName(no_internet)

    def retranslateUi(self, no_internet):
        _translate = QtCore.QCoreApplication.translate
        self.label_2.setText(_translate("no_internet", "No Internet connection."))
        self.label_3.setText(_translate("no_internet", "Please check your Internet connection and try again."))

