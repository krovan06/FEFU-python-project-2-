from PyQt6.QtCore import QUrl, Qt
from PyQt6.QtGui import QDesktopServices, QIntValidator
from PyQt6.QtWidgets import QMessageBox, QWidget
from registration import Ui_Form
from Check_BD import CheckThread

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.text = QMessageBox(self)
        self.check_db = CheckThread()
        self.regwindow = Ui_Form()
        self.regwindow.setupUi(self)
        self.regwindow.create_btn.clicked.connect(self.registar)
        self.regwindow.label_data.mousePressEvent = self.open_document

        # Установка валидатора для class_edit
        self.regwindow.class_edit.setValidator(QIntValidator(1, 11))

    def open_document(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            document_path = "9e9da1e9bc62dcc0.docx"
            if not QDesktopServices.openUrl(QUrl.fromLocalFile(document_path)):
                QMessageBox.critical(self, "Error", f"Failed to open document: {document_path}")

    def registar(self):

        Name = self.regwindow.name_edit.text()
        Class = self.regwindow.class_edit.text()

        # Проверка на допустимый диапазон значений для class_edit
        if not Class.isdigit() or not (1 <= int(Class) <= 11):
            self.text.setText("Такого класса не существует")
            self.text.show()
            return

        log = self.regwindow.login_edit.text()
        password1 = self.regwindow.pass_edit.text()
        password2 = self.regwindow.reliab_pass_edit.text()
        if password1 == password2 and password2 != "" and password1 != "" and log != "" and self.regwindow.checkBox.isChecked():
            if self.check_db.thr_register(log, password1, Name, Class):
                self.close()
        elif not(password2 != "" and password1 != "" and log != ""):
            self.text.setText("Заполните все пустые поля")
            self.text.show()
        else:
            self.text.setText("Введен не верный логин/пароль или аккаунт с таким логином уже существует")
            self.text.show()