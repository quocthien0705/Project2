# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sidebar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from testUART import SerialMonitor
import test_visualize

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 900)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/healthcare.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #fff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setStyleSheet("    #icon_only_widget {\n"
"        background-color: #313a46;\n"
"        width:50px;\n"
"    }\n"
"\n"
"    #icon_only_widget QPushButton, QLabel {\n"
"        height:50px;\n"
"        border:none;\n"
"        background-color: #313a46;\n"
"        /* border-bottom: 1px solid #b0b0b0; */\n"
"    }\n"
"\n"
"    #icon_only_widget QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }")
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.logo_label_1 = QtWidgets.QLabel(self.icon_only_widget)
        self.logo_label_1.setMinimumSize(QtCore.QSize(64, 64))
        self.logo_label_1.setMaximumSize(QtCore.QSize(64, 64))
        self.logo_label_1.setStyleSheet("    #logo_label_1 {\n"
"    background-color: rgba(0, 0, 0,0);\n"
"        padding: 5px\n"
"    }")
        self.logo_label_1.setText("")
        self.logo_label_1.setPixmap(QtGui.QPixmap(":/icon/Icon_Logo/healthcare.png"))
        self.logo_label_1.setScaledContents(True)
        self.logo_label_1.setObjectName("logo_label_1")
        self.horizontalLayout_3.addWidget(self.logo_label_1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.home_btn_1.setStyleSheet("")
        self.home_btn_1.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/home_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon1.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/home_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.home_btn_1.setIcon(icon1)
        self.home_btn_1.setIconSize(QtCore.QSize(40, 40))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.newprofile_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.newprofile_btn_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.newprofile_btn_1.setStyleSheet("")
        self.newprofile_btn_1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/add-user_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/add-user_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.newprofile_btn_1.setIcon(icon2)
        self.newprofile_btn_1.setIconSize(QtCore.QSize(40, 40))
        self.newprofile_btn_1.setCheckable(True)
        self.newprofile_btn_1.setAutoExclusive(True)
        self.newprofile_btn_1.setObjectName("newprofile_btn_1")
        self.verticalLayout.addWidget(self.newprofile_btn_1)
        self.display_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.display_btn_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.display_btn_1.setStyleSheet("")
        self.display_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/heartbeat_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/heartbeat_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.display_btn_1.setIcon(icon3)
        self.display_btn_1.setIconSize(QtCore.QSize(40, 40))
        self.display_btn_1.setCheckable(True)
        self.display_btn_1.setAutoExclusive(True)
        self.display_btn_1.setObjectName("display_btn_1")
        self.verticalLayout.addWidget(self.display_btn_1)
        self.uart_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.uart_btn_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.uart_btn_1.setStyleSheet("")
        self.uart_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/two-arrows_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/two-arrows_white.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.uart_btn_1.setIcon(icon4)
        self.uart_btn_1.setIconSize(QtCore.QSize(40, 40))
        self.uart_btn_1.setCheckable(True)
        self.uart_btn_1.setAutoExclusive(True)
        self.uart_btn_1.setObjectName("uart_btn_1")
        self.verticalLayout.addWidget(self.uart_btn_1)
        spacerItem = QtWidgets.QSpacerItem(20, 375, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_btn_1.setStyleSheet("")
        self.exit_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/logout_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_btn_1.setIcon(icon5)
        self.exit_btn_1.setIconSize(QtCore.QSize(32, 32))
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setStyleSheet("    #full_menu_widget {\n"
"        background-color: #313a46;\n"
"    }\n"
"\n"
"    /* style for QPushButton */\n"
"    #full_menu_widget QPushButton {\n"
"        border:none;\n"
"        border-radius: 3px;\n"
"        text-align: left;\n"
"        padding: 4px 10px 8px 15px;\n"
"        color: #f2f3f4;\n"
"        background-color: #313a46;\n"
"    }\n"
"\n"
"    #full_menu_widget QPushButton:hover {\n"
"        background-color: rgba( 86, 101, 115, 0.5);\n"
"    }\n"
"\n"
"    #full_menu_widget QPushButton:checked {\n"
"        color: #fff;\n"
"    }")
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(7)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.logo_label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.logo_label_2.setMinimumSize(QtCore.QSize(64, 64))
        self.logo_label_2.setMaximumSize(QtCore.QSize(64, 64))
        self.logo_label_2.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.logo_label_2.setText("")
        self.logo_label_2.setPixmap(QtGui.QPixmap(":/icon/Icon_Logo/healthcare.png"))
        self.logo_label_2.setScaledContents(True)
        self.logo_label_2.setObjectName("logo_label_2")
        self.horizontalLayout_2.addWidget(self.logo_label_2)
        self.logo_label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logo_label_3.setFont(font)
        self.logo_label_3.setStyleSheet("    #logo_label_3 {\n"
"        padding: 5px;\n"
"        color: #fff;\n"
"        \n"
"    background-color: rgba(0, 0, 0,0);\n"
"    }")
        self.logo_label_3.setObjectName("logo_label_3")
        self.horizontalLayout_2.addWidget(self.logo_label_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.home_btn_2.setFont(font)
        self.home_btn_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.home_btn_2.setAutoFillBackground(False)
        self.home_btn_2.setStyleSheet("")
        self.home_btn_2.setIcon(icon1)
        self.home_btn_2.setIconSize(QtCore.QSize(30, 30))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.newprofile_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.newprofile_btn_2.setFont(font)
        self.newprofile_btn_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.newprofile_btn_2.setStyleSheet("")
        self.newprofile_btn_2.setIcon(icon2)
        self.newprofile_btn_2.setIconSize(QtCore.QSize(30, 30))
        self.newprofile_btn_2.setCheckable(True)
        self.newprofile_btn_2.setAutoExclusive(True)
        self.newprofile_btn_2.setObjectName("newprofile_btn_2")
        self.verticalLayout_2.addWidget(self.newprofile_btn_2)
        self.display_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.display_btn_2.setFont(font)
        self.display_btn_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.display_btn_2.setStyleSheet("")
        self.display_btn_2.setIcon(icon3)
        self.display_btn_2.setIconSize(QtCore.QSize(30, 30))
        self.display_btn_2.setCheckable(True)
        self.display_btn_2.setAutoExclusive(True)
        self.display_btn_2.setObjectName("display_btn_2")
        self.verticalLayout_2.addWidget(self.display_btn_2)
        self.uart_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(60)
        sizePolicy.setHeightForWidth(self.uart_btn_2.sizePolicy().hasHeightForWidth())
        self.uart_btn_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.uart_btn_2.setFont(font)
        self.uart_btn_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.uart_btn_2.setStyleSheet("")
        self.uart_btn_2.setIcon(icon4)
        self.uart_btn_2.setIconSize(QtCore.QSize(24, 24))
        self.uart_btn_2.setCheckable(True)
        self.uart_btn_2.setAutoExclusive(True)
        self.uart_btn_2.setObjectName("uart_btn_2")
        self.verticalLayout_2.addWidget(self.uart_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 373, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem1)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.exit_btn_2.setFont(font)
        self.exit_btn_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.exit_btn_2.setStyleSheet("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icon/icon/close-window-64.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/logout_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.exit_btn_2.setIcon(icon6)
        self.exit_btn_2.setIconSize(QtCore.QSize(25, 25))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setMinimumSize(QtCore.QSize(0, 40))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.change_btn.setStyleSheet("    #change_btn {\n"
"        padding: 5px;\n"
"        border: none;\n"
"        width: 30px;\n"
"        height: 30px;\n"
"    }")
        self.change_btn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icon/Icon_Logo/sidebar_black.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon7)
        self.change_btn.setIconSize(QtCore.QSize(24, 24))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_4.addWidget(self.change_btn)
        spacerItem2 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_4.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(236, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_5 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.widget_2 = QtWidgets.QWidget(self.page_3)
        self.widget_2.setObjectName("widget_2")
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setGeometry(QtCore.QRect(318, 0, 1000, 831))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.frame.setFont(font)
        self.frame.setStyleSheet("")
        self.frame.setInputMethodHints(QtCore.Qt.ImhNone)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(340, 20, 320, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(50)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 85, 127);")
        self.label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(150, 120, 112, 32))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(150, 200, 130, 32))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.line_fullname = QtWidgets.QLineEdit(self.frame)
        self.line_fullname.setGeometry(QtCore.QRect(272, 120, 508, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(11)
        self.line_fullname.setFont(font)
        self.line_fullname.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0, 0, 0,255);\n"
"border-radius: 5px;\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_fullname.setText("")
        self.line_fullname.setPlaceholderText("")
        self.line_fullname.setObjectName("line_fullname")
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setGeometry(QtCore.QRect(290, 200, 130, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.dateEdit.setStyleSheet("/* Style for header area  ####################################################*/ \n"
"\n"
"QCalendarWidget QWidget {\n"
"     alternate-background-color: #B8E2FF;\n"
"}\n"
"\n"
"/* style for top navigation area ###############################################*/ \n"
"\n"
"QDateEdit QWidget#qt_calendar_navigationbar {\n"
"    background-color: #fff;\n"
"    border: 2px solid  #B8E2FF;\n"
"    border-bottom: 0px;\n"
"    border-top-left-radius: 5px;\n"
"    border-top-right-radius: 5px;\n"
"}\n"
"\n"
"/* style for month change buttons ############################################ */\n"
"\n"
"QDateEdit QWidget#qt_calendar_prevmonth, \n"
"QDateEdit QWidget#qt_calendar_nextmonth {\n"
"    /* border delete */\n"
"    border: none;  \n"
"    /* delete default icons */\n"
"    qproperty-icon: none; \n"
"    \n"
"    min-width: 13px;\n"
"    max-width: 13px;\n"
"    min-height: 13px;\n"
"    max-height: 13px;\n"
"\n"
"    border-radius: 5px; \n"
"    /* set background transparent */\n"
"    background-color: transparent; \n"
"    padding: 5px;\n"
"}\n"
"\n"
"/* style for pre month button ############################################ */\n"
"\n"
"QDateEdit QWidget#qt_calendar_prevmonth {\n"
"    /* set text for button */\n"
"    /*qproperty-text: \">\";*/\n"
"    margin-left:5px;\n"
"    image: url(:/icon/Icon_Logo/arrow-119-48.ico);\n"
"}\n"
"\n"
"/* style for next month button ########################################### */\n"
"QDateEdit QWidget#qt_calendar_nextmonth {\n"
"    margin-right:5px;\n"
"    image: url(:/icon/Icon_Logo/arrow-19-48.ico);\n"
"    /* qproperty-text: \">\"; */\n"
"}\n"
"QDateEdit QWidget#qt_calendar_prevmonth:hover, \n"
"QDateEdit QWidget#qt_calendar_nextmonth:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"QDateEdit QWidget#qt_calendar_prevmonth:pressed, \n"
"QDateEdit QWidget#qt_calendar_nextmonth:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"\n"
"/* Style for month and yeat buttons #################################### */\n"
"\n"
"QDateEdit QWidget#qt_calendar_yearbutton {\n"
"    color: #000;\n"
"    margin:5px;\n"
"    border-radius: 5px;\n"
"    font-size: 13px;\n"
"    padding:0px 10px;\n"
"}\n"
"\n"
"QDateEdit QWidget#qt_calendar_monthbutton {\n"
"    width: 110px;\n"
"    color: #000;\n"
"    font-size: 13px;\n"
"    margin:5px 0px;\n"
"    border-radius: 5px;\n"
"    padding:0px 2px;\n"
"}\n"
"\n"
"QDateEdit QWidget#qt_calendar_yearbutton:hover, \n"
"QDateEdit QWidget#qt_calendar_monthbutton:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"QDateEdit QWidget#qt_calendar_yearbutton:pressed, \n"
"QDateEdit QWidget#qt_calendar_monthbutton:pressed {\n"
"    background-color: rgba(235, 235, 235, 100);\n"
"}\n"
"\n"
"/* Style for year input lineEdit ######################################*/\n"
"\n"
"QDateEdit QWidget#qt_calendar_yearedit {\n"
"    min-width: 53px;\n"
"    color: #000;\n"
"    background: transparent;\n"
"    font-size: 13px;\n"
"}\n"
"\n"
"/* Style for year change buttons ######################################*/\n"
"\n"
"QDateEdit QWidget#qt_calendar_yearedit::up-button { \n"
"    image: url(:/icon/Icon_Logo/arrow-151-48.ico);\n"
"    subcontrol-position: right;\n"
"}\n"
"\n"
"QDateEdit QWidget#qt_calendar_yearedit::down-button { \n"
"    image: url(:/icon/Icon_Logo/arrow-213-48.ico);\n"
"    subcontrol-position: left; \n"
"}\n"
"\n"
"QDateEdit QWidget#qt_calendar_yearedit::down-button, \n"
"QDateEdit QWidget#qt_calendar_yearedit::up-button {\n"
"    width:10px;\n"
"    padding: 0px 5px;\n"
"    border-radius:3px;\n"
"}\n"
"\n"
"QDateEdit QWidget#qt_calendar_yearedit::down-button:hover, \n"
"QDateEdit QWidget#qt_calendar_yearedit::up-button:hover {\n"
"    background-color: #55aaff;\n"
"}\n"
"\n"
"/* Style for month select menu ##################################### */\n"
"\n"
"QDateEdit QCalendarWidget QToolButton QMenu {\n"
"     background-color: white;\n"
"}\n"
"\n"
"QDateEdit QCalendarWidget QToolButton QMenu::item {\n"
"    /*padding: 10px;*/\n"
"}\n"
"\n"
"QDateEdit QCalendarWidget QToolButton QMenu::item:selected:enabled {\n"
"    background-color: #55aa7f;\n"
"}\n"
"\n"
"QDateEdit QCalendarWidget QToolButton::menu-indicator {\n"
"    /* Remove toolButton arrow */\n"
"      /*image: none; */\n"
"    nosubcontrol-origin: margin;\n"
"    subcontrol-position: right center;\n"
"    margin-top: 10px;\n"
"    width:20px;\n"
"}\n"
"\n"
"/* Style for calendar table ########################################## */\n"
"\n"
"QDateEdit QCalendarWidget QTableView {\n"
"    /* Remove the selected dashed box */\n"
"    outline: 0px;\n"
"\n"
"    border: 2px solid  #B8E2FF;\n"
"    border-top: 0px;\n"
"    border-bottom-left-radius: 5px;\n"
"    border-bottom-right-radius: 5px;\n"
"}\n"
"\n"
"QDateEdit QCalendarWidget QTableView::item:hover {\n"
"   border-radius:5px;\n"
"    background-color:#aaffff;\n"
"}\n"
"\n"
"QDateEdit QCalendarWidget QTableView::item:selected {\n"
"    background-color: #55aa7f; \n"
"    border-radius:5px;\n"
"}")
        self.dateEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.dateEdit.setReadOnly(False)
        self.dateEdit.setAccelerated(False)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setCurrentSectionIndex(0)
        self.dateEdit.setTimeSpec(QtCore.Qt.LocalTime)
        self.dateEdit.setObjectName("dateEdit")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(540, 200, 50, 32))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(600, 200, 180, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(9)
        self.comboBox.setFont(font)
        self.comboBox.setFocusPolicy(QtCore.Qt.NoFocus)
        self.comboBox.setStyleSheet("#comboBox {\n"
"    border: 1px solid #000;\n"
"    border-radius: 4px;\n"
"    padding-left: 10px;\n"
"}\n"
"\n"
"#comboBox::drop-down {\n"
"    border: 0px;\n"
"}\n"
"\n"
"#comboBox::down-arrow {\n"
"    image: url(:/icon/Icon_Logo/arrow-204-32.ico);\n"
"    width: 12px;\n"
"    height: 12px;\n"
"    margin-right:15px;\n"
"}\n"
"\n"
"#comboBox:on {\n"
"     border: 2px solid #c2dbfe;\n"
" }\n"
"\n"
"QComboBox QListView {\n"
"    font-size: 12px;\n"
"    border:1px solid rgba(0,0,0,10%);\n"
"    padding:5px;\n"
"    background-color: #fff;\n"
"    outline: 0px;  /*去虚线*/\n"
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
"}\n"
"\n"
"")
        self.comboBox.setPlaceholderText("")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.line_height = QtWidgets.QLineEdit(self.frame)
        self.line_height.setGeometry(QtCore.QRect(290, 360, 80, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_height.setFont(font)
        self.line_height.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0, 0, 0,255);\n"
"border-radius: 5px;\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_height.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_height.setText("")
        self.line_height.setPlaceholderText("")
        self.line_height.setObjectName("line_height")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(150, 360, 130, 32))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line_weight = QtWidgets.QLineEdit(self.frame)
        self.line_weight.setGeometry(QtCore.QRect(560, 360, 220, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_weight.setFont(font)
        self.line_weight.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0, 0, 0,255);\n"
"border-radius: 5px;\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_weight.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_weight.setText("")
        self.line_weight.setPlaceholderText("")
        self.line_weight.setObjectName("line_weight")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(410, 360, 140, 32))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.line_insur_number = QtWidgets.QLineEdit(self.frame)
        self.line_insur_number.setGeometry(QtCore.QRect(450, 520, 330, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_insur_number.setFont(font)
        self.line_insur_number.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0, 0, 0,255);\n"
"border-radius: 5px;\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_insur_number.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_insur_number.setText("")
        self.line_insur_number.setPlaceholderText("")
        self.line_insur_number.setObjectName("line_insur_number")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(150, 520, 290, 32))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.line_address = QtWidgets.QLineEdit(self.frame)
        self.line_address.setGeometry(QtCore.QRect(260, 280, 520, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_address.setFont(font)
        self.line_address.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0, 0, 0,255);\n"
"border-radius: 5px;\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_address.setText("")
        self.line_address.setPlaceholderText("")
        self.line_address.setObjectName("line_address")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(150, 280, 100, 32))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.line_note = QtWidgets.QLineEdit(self.frame)
        self.line_note.setGeometry(QtCore.QRect(220, 600, 560, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_note.setFont(font)
        self.line_note.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0, 0, 0,255);\n"
"border-radius: 5px;\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_note.setText("")
        self.line_note.setObjectName("line_note")
        self.line_phone_number = QtWidgets.QLineEdit(self.frame)
        self.line_phone_number.setGeometry(QtCore.QRect(330, 440, 450, 35))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(10)
        self.line_phone_number.setFont(font)
        self.line_phone_number.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border:1px solid rgba(0, 0, 0,255);\n"
"border-radius: 5px;\n"
"color: rgba(0,0,0,255);\n"
"padding-bottom:5px")
        self.line_phone_number.setInputMethodHints(QtCore.Qt.ImhNone)
        self.line_phone_number.setText("")
        self.line_phone_number.setPlaceholderText("")
        self.line_phone_number.setObjectName("line_phone_number")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(150, 440, 170, 32))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(150, 600, 60, 32))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.save_button = QtWidgets.QPushButton(self.frame)
        self.save_button.setGeometry(QtCore.QRect(370, 700, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.save_button.setFont(font)
        self.save_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.save_button.setStyleSheet("QPushButton#save_button{    \n"
"    background-color: rgba(239, 35, 60,255);\n"
"    color:white;\n"
"    border-radius:7px;\n"
"}\n"
"QPushButton#save_button:hover{    \n"
"    background-color: rgba(239, 35, 60,200);\n"
"}\n"
"QPushButton#save_button:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: rgba(229, 56, 59,200);\n"
"}")
        self.save_button.setObjectName("save_button")
        self.clear_button = QtWidgets.QPushButton(self.frame)
        self.clear_button.setGeometry(QtCore.QRect(530, 700, 100, 50))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.clear_button.setFont(font)
        self.clear_button.setFocusPolicy(QtCore.Qt.NoFocus)
        self.clear_button.setStyleSheet("QPushButton#clear_button{    \n"
"    background-color: rgba(21, 122, 110,255);\n"
"    color:white;\n"
"    border-radius:7px;\n"
"}\n"
"QPushButton#clear_button:hover{    \n"
"    background-color: rgba(21, 122, 110,200);\n"
"}\n"
"QPushButton#clear_button:pressed{    \n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color: rgba(17, 98, 87,200);\n"
"}")
        self.clear_button.setObjectName("clear_button")
        self.gridLayout_4.addWidget(self.widget_2, 1, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.serialMonitor_V = test_visualize.MainWindow()
        self.gridLayout_5.addWidget(self.serialMonitor_V, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        # self.label_7 = QtWidgets.QLabel(self.page_4)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.label_7.setFont(font)
        # self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_7.setObjectName("label_7")
        # self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        # self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setObjectName("page_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.page_5)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.serialMonitor = SerialMonitor()
        self.gridLayout_6.addWidget(self.serialMonitor, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_5)
        # self.label_8 = QtWidgets.QLabel(self.page_5)
        # font = QtGui.QFont()
        # font.setPointSize(20)
        # self.label_8.setFont(font)
        # self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        # self.label_8.setObjectName("label_8")
        # self.gridLayout_6.addWidget(self.label_8, 0, 0, 1, 1)
        # self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setObjectName("page_6")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.page_6)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QtWidgets.QWidget()
        self.page_7.setObjectName("page_7")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.page_7)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.stackedWidget.addWidget(self.page_7)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.comboBox.setCurrentIndex(0)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.newprofile_btn_1.toggled['bool'].connect(self.newprofile_btn_2.setChecked) # type: ignore
        self.display_btn_1.toggled['bool'].connect(self.display_btn_2.setChecked) # type: ignore
        self.uart_btn_1.toggled['bool'].connect(self.uart_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        self.newprofile_btn_2.toggled['bool'].connect(self.newprofile_btn_1.setChecked) # type: ignore
        self.display_btn_2.toggled['bool'].connect(self.display_btn_1.setChecked) # type: ignore
        self.uart_btn_2.toggled['bool'].connect(self.uart_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Health Monitoring System"))
        self.logo_label_3.setText(_translate("MainWindow", "Project_2"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.newprofile_btn_2.setText(_translate("MainWindow", "Create New Profile"))
        self.display_btn_2.setText(_translate("MainWindow", "Display"))
        self.uart_btn_2.setText(_translate("MainWindow", "UART"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))
        self.label_5.setText(_translate("MainWindow", "HomePage"))
        self.label.setText(_translate("MainWindow", "Create New Profile"))
        self.label_2.setText(_translate("MainWindow", "Full Name:"))
        self.label_3.setText(_translate("MainWindow", "Day of Birth:"))
        self.dateEdit.setDisplayFormat(_translate("MainWindow", "MM/dd/yyyy"))
        self.label_4.setText(_translate("MainWindow", "Sex:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Male"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Female"))
        self.label_6.setText(_translate("MainWindow", "Height (cm):"))
        self.label_9.setText(_translate("MainWindow", "Weight (kg):"))
        self.label_10.setText(_translate("MainWindow", "Health Insurance Number:"))
        self.label_11.setText(_translate("MainWindow", "Address:"))
        self.line_note.setPlaceholderText(_translate("MainWindow", "Note here if the patient has underlying disease."))
        self.label_13.setText(_translate("MainWindow", "Phone Number:"))
        self.label_12.setText(_translate("MainWindow", "Note:"))
        self.save_button.setText(_translate("MainWindow", "Save"))
        self.clear_button.setText(_translate("MainWindow", "Clear"))
        # self.label_7.setText(_translate("MainWindow", "Display"))
        # self.label_8.setText(_translate("MainWindow", "UART"))
import img_src_rc
