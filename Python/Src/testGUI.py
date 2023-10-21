import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, QFile, QTextStream

from sidebar_copy import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.home_btn_2.setChecked(True)
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_display_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_display_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_newprofile_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_newprofile_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_uart_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_uart_btn_2_toggled(self, ):
        self.ui.stackedWidget.setCurrentIndex(4)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ## loading style file


    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())
