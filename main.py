import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget
from reg_window import *
from authorization import Ui_Form
from Check_BD import CheckThread

class Interface(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.regist_btn.clicked.connect(self.reg)
        self.sign_btn.clicked.connect(self.login)

        self.check_db = CheckThread()
        self.NewWindow = RegisterWindow()

        self.flag = False
    def UpdateRegisterWindow(self):
        self.close()
        self.NewWindow.show()

    def login(self):
        name = self.login_edit.text()
        password = self.pass_edit.text()
        if self.check_db.thr_login(name, password):
            self.close()



    def reg(self):
        self.UpdateRegisterWindow()


if True:
    app = QtWidgets.QApplication(sys.argv)
    mywin = Interface()
    mywin.show()
    sys.exit(app.exec())