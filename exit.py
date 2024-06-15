from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(409, 194)
        self.widget = QtWidgets.QWidget(parent=Form)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 411, 201))
        self.widget.setStyleSheet("QWidget { \n"
"    background: rgb(255, 212, 194); \n"
"}\n"
"")
        self.widget.setObjectName("widget")
        self.class_label_8 = QtWidgets.QLabel(parent=self.widget)
        self.class_label_8.setGeometry(QtCore.QRect(0, 40, 411, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(16)
        self.class_label_8.setFont(font)
        self.class_label_8.setStyleSheet("color:rgb(156, 36, 0)")
        self.class_label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.class_label_8.setObjectName("class_label_8")
        self.yes_btn = QtWidgets.QPushButton(parent=self.widget)
        self.yes_btn.setGeometry(QtCore.QRect(100, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.yes_btn.setFont(font)
        self.yes_btn.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.yes_btn.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color:  rgb(255, 92, 71);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(255, 162, 125);\n"
"}")
        self.yes_btn.setObjectName("yes_btn")
        self.update_btn_5 = QtWidgets.QPushButton(parent=self.widget)
        self.update_btn_5.setGeometry(QtCore.QRect(220, 100, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.update_btn_5.setFont(font)
        self.update_btn_5.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.update_btn_5.setStyleSheet("QPushButton {\n"
"    border-radius: 8px;\n"
"    background-color:  rgb(255, 92, 71);\n"
"    color:  rgb(255, 255, 255);\n"
"    font-size:  25px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color:  rgb(255, 162, 125);\n"
"}")
        self.update_btn_5.setObjectName("update_btn_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.class_label_8.setText(_translate("Form", "Вы точно хотите выйти?"))
        self.yes_btn.setText(_translate("Form", "Да"))
        self.update_btn_5.setText(_translate("Form", "Нет"))
