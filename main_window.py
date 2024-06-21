from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QLabel, QMainWindow, QVBoxLayout, QWidget, QMessageBox
from setuptools._distutils.spawn import spawn

from MainWindowStudent import Ui_MainWindowStudent
from MainWindowTeacher import Ui_MainWindowTeacher
from UserInfo import FoundInsertInfo

class MainTWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_t_window = Ui_MainWindowTeacher()
        self.text_dict = {}
        self.mainUI()
        self.show_my_account()
        self.bd = FoundInsertInfo()
        self.bd.InsertClassInfo()

    def mainUI(self):
        self.main_t_window.setupUi(self)
        self.connection()
        self.setup_links()

    def connection(self):
        self.main_t_window.my_account_btn.clicked.connect(self.show_my_account)
        self.main_t_window.schedule_btn.clicked.connect(self.show_schedule)
        self.main_t_window.teachers_btn.clicked.connect(self.show_teachers)
        self.main_t_window.lesson_btn.clicked.connect(self.show_lesson)
        self.main_t_window.create_btn_2.clicked.connect(self.apply_selection)
        self.main_t_window.create_btn_3.clicked.connect(self.check_checkboxes)
        self.main_t_window.exit_btn.clicked.connect(self.exit)

    def exit(self):
        self.close()

    def infomation_users(self, name, surname, cls, login):
        self.main_t_window.name_edit.setText(name)
        self.main_t_window.class_edit.setText(cls)
        self.main_t_window.surname_edit.setText(surname)
        self.login = login
        self.name = name


    def show_my_account(self):
        self.main_t_window.stackedWidget.setCurrentIndex(0)
        self.main_t_window.name_edit.setEnabled(False)
        self.main_t_window.class_edit.setEnabled(False)
        self.main_t_window.surname_edit.setEnabled(False)
        self.main_t_window.oldpass_edit.setEnabled(False)
        self.main_t_window.newpass_edit.setEnabled(False)
        self.main_t_window.item_comboBox.setEnabled(False)
        self.main_t_window.create_btn.clicked.connect(self.editing_account)
        self.main_t_window.save_btn.clicked.connect(self.editing_account)

    def editing_account(self):
        if self.sender().text() == "Редактировать":
            self.main_t_window.name_edit.setEnabled(True)
            self.main_t_window.class_edit.setEnabled(True)
            self.main_t_window.surname_edit.setEnabled(True)
            self.main_t_window.oldpass_edit.setEnabled(True)
            self.main_t_window.newpass_edit.setEnabled(True)
            self.main_t_window.item_comboBox.setEnabled(True)
            print("unlocked :)")
        else:
            if self.main_t_window.class_edit.text() in "0123456789":
                self.main_t_window.name_edit.setEnabled(False)
                self.main_t_window.class_edit.setEnabled(False)
                self.main_t_window.surname_edit.setEnabled(False)
                self.main_t_window.item_comboBox.setEnabled(False)
                self.bd.UpdateInfo(self.main_t_window.name_edit.text(), self.main_t_window.surname_edit.text(),
                                   self.main_t_window.class_edit.text(), self.login, self.main_t_window.item_comboBox.currentText())
                print("locked :(")
                print()
                if self.main_t_window.newpass_edit.text() != "":
                    self.bd.CheckPassword(self.login, self.main_t_window.newpass_edit.text(), self.main_t_window.oldpass_edit.text())
            else:
                print("Ошибка в одном из полей, пожалуйста, проверьте информацию.")
    def show_schedule(self):
        self.main_t_window.stackedWidget.setCurrentIndex(2)
        self.main_t_window.save_btn_2.clicked.connect(self.save_shedule)
        self.main_t_window.update_btn.clicked.connect(self.update_shedule)
    def save_shedule(self):
        self.slovar = {}
        self.sp = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
        self.slovar["Monday"] = self.main_t_window.mon_edit.text()
        self.slovar["Tuesday"] = self.main_t_window.tue_edit.text()
        self.slovar["Wednesday"] = self.main_t_window.wed_edit.text()
        self.slovar["Thursday"] = self.main_t_window.thu_edit.text()
        self.slovar["Friday"] = self.main_t_window.fri_edit.text()
        self.slovar["Saturaday"] = self.main_t_window.sat_edit.text()
        self.slovar["Sunday"] = self.main_t_window.sun_edit.text()
        with open(f"{self.name}", "w") as file:
            for day in self.slovar:
                file.write(f"{day}:\n{self.slovar[day]}\n")
        print("Your file is saved :)")
    def update_shedule(self):
        file = open(f"{self.name}.txt")
        sp = []
        slovar = {}
        for i in file:
            if i != "":
                sp.append(i.replace("\n", ""))
        for i in range(len(sp) - 1):
            if sp[i] != "":
                if sp[i][-1] == ":":
                    slovar[sp[i]] = sp[i + 1]
        self.main_t_window.mon_edit.setText(slovar["Monday:"])
        self.main_t_window.tue_edit.setText(slovar["Tuesday:"])
        self.main_t_window.wed_edit.setText(slovar["Wednesday:"])
        self.main_t_window.thu_edit.setText(slovar["Thursday:"])
        self.main_t_window.fri_edit.setText(slovar["Friday:"])
        self.main_t_window.sat_edit.setText(slovar["Saturaday:"])
        self.main_t_window.sun_edit.setText(slovar["Sunday:"])

    def show_teachers(self):
        self.main_t_window.stackedWidget.setCurrentIndex(3)

    def show_lesson(self):
        self.main_t_window.stackedWidget.setCurrentIndex(4)

    def setup_links(self):
        # Словарь ссылок на учебники
        self.links = {
            ('1', 'Математика'): 'https://example.com/math1',
            ('2', 'Математика'): 'https://example.com/math2',
            ('3', 'Математика'): 'https://example.com/math3',
            ('4', 'Математика'): 'https://example.com/math4',
            ('5', 'Математика'): 'https://example.com/math5',
            ('6', 'Математика'): 'https://example.com/math6',
            ('7', 'Математика'): 'https://example.com/math7',
            ('8', 'Математика'): 'https://example.com/math8',
            ('9', 'Математика'): 'https://example.com/math9',
            ('10', 'Математика'): 'https://example.com/math10',
            ('11', 'Математика'): 'https://example.com/math11',
            ('1', 'Русский язык'): 'https://example.com/russ1',
            ('2', 'Русский язык'): 'https://example.com/russ2',
            ('3', 'Русский язык'): 'https://example.com/russ3',
            ('4', 'Русский язык'): 'https://example.com/russ4',
            ('5', 'Русский язык'): 'https://example.com/russ5',
            ('6', 'Русский язык'): 'https://example.com/russ6',
            ('7', 'Русский язык'): 'https://example.com/russ7',
            ('8', 'Русский язык'): 'https://example.com/russ8',
            ('9', 'Русский язык'): 'https://example.com/russ9',
            ('10', 'Русский язык'): 'https://example.com/russ10',
            ('11', 'Русский язык'): 'https://example.com/russ11',
            ('1', 'Английский язык'): 'https://example.com/endl1',
            ('2', 'Английский язык'): 'https://example.com/endl2',
            ('3', 'Английский язык'): 'https://example.com/endl3',
            ('4', 'Английский язык'): 'https://example.com/endl4',
            ('5', 'Английский язык'): 'https://example.com/endl5',
            ('6', 'Английский язык'): 'https://example.com/endl6',
            ('7', 'Английский язык'): 'https://example.com/endl7',
            ('8', 'Английский язык'): 'https://example.com/endl8',
            ('9', 'Английский язык'): 'https://example.com/endl9',
            ('10', 'Английский язык'): 'https://example.com/endl10',
            ('11', 'Английский язык'): 'https://example.com/endl11',
            ('7', 'Химия'): 'https://example.com/chem7',
            ('8', 'Химия'): 'https://example.com/chem8',
            ('9', 'Химия'): 'https://example.com/chem9',
            ('10', 'Химия'): 'https://example.com/chem10',
            ('11', 'Химия'): 'https://example.com/chem11',
            ('7', 'Физика'): 'https://example.com/phys7',
            ('8', 'Физика'): 'https://example.com/phys8',
            ('9', 'Физика'): 'https://example.com/phys9',
            ('10', 'Физика'): 'https://example.com/phys10',
            ('11', 'Физика'): 'https://example.com/phys11',
            ('5', 'Биология'): 'https://example.com/biol5',
            ('6', 'Биология'): 'https://example.com/biol6',
            ('7', 'Биология'): 'https://example.com/biol7',
            ('8', 'Биология'): 'https://example.com/biol8',
            ('9', 'Биология'): 'https://example.com/biol9',
            ('10', 'Биология'): 'https://example.com/biol10',
            ('11', 'Биология'): 'https://example.com/biol11',
        }

    def apply_selection(self):
        selected_class = self.main_t_window.class_comboBox.currentText()
        selected_subject = self.main_t_window.objects_comboBox.currentText()
        key = (selected_class, selected_subject)
        link = self.links.get(key, 'Для данного класса и/или предмета нет учебника')
        self.main_t_window.lineEdit.setText(link)

    def check_checkboxes(self):
        if self.main_t_window.checkBox_2.isChecked() and self.main_t_window.checkBox_4.isChecked() and self.main_t_window.checkBox_6.isChecked():
            QMessageBox.information(self, 'Сообщение', 'Идет урок')
            self.show_lesson()
        else:
            QMessageBox.warning(self, 'Сообщение', 'Отметьте все пункты')

class MainSWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.text_dict = {}
        self.main_s_window = Ui_MainWindowStudent()
        self.mainUI()
        self.bd = FoundInsertInfo()
        self.show_my_account()
        #self.update_schedule()

    def mainUI(self):
        self.main_s_window.setupUi(self)
        self.connection()

    def connection(self):
        self.main_s_window.my_account_btn.clicked.connect(self.show_my_account)
        self.main_s_window.schedule_btn.clicked.connect(self.show_schedule)
        self.main_s_window.teachers_btn.clicked.connect(self.show_teachers)
        self.main_s_window.lesson_btn.clicked.connect(self.show_lesson)
        self.main_s_window.exit_btn.clicked.connect(self.exit)
        self.main_s_window.create_btn_3.clicked.connect(self.check_checkboxes)
        self.main_s_window.item_comboBox.currentIndexChanged.connect(self.update_item_edit)
        self.main_s_window.update_btn.clicked.connect(self.update_schedule)

    def infomation_users(self, name, cls, login, surname):
        self.main_s_window.name_edit.setText(name)
        self.main_s_window.class_edit.setText(cls)
        self.main_s_window.surname_edit.setText(surname)
        self.login = login
        self.name = name
        self.cls = cls


    def exit(self):
        self.close()

    def show_my_account(self):
        self.main_s_window.stackedWidget.setCurrentIndex(0)
        self.main_s_window.surname_edit.setEnabled(False)
        self.main_s_window.item_comboBox.setEnabled(False)
        self.main_s_window.name_edit.setEnabled(False)
        self.main_s_window.class_edit.setEnabled(False)
        self.main_s_window.newpass_edit.setEnabled(False)
        self.main_s_window.oldpass_edit.setEnabled(False)
        self.main_s_window.save_btn.clicked.connect(self.editing_account)
        self.main_s_window.create_btn.clicked.connect(self.editing_account)
        print(0)

    def editing_account(self):
        if self.sender().text() == "Редактировать":
            self.main_s_window.name_edit.setEnabled(True)
            self.main_s_window.class_edit.setEnabled(True)
            self.main_s_window.surname_edit.setEnabled(True)
            self.main_s_window.oldpass_edit.setEnabled(True)
            self.main_s_window.newpass_edit.setEnabled(True)
            self.main_s_window.item_comboBox.setEnabled(True)
            print("unlocked :)")
        else:
            if self.main_s_window.class_edit.text() in "0123456789":
                self.main_s_window.name_edit.setEnabled(False)
                self.main_s_window.class_edit.setEnabled(False)
                self.main_s_window.surname_edit.setEnabled(False)
                self.main_s_window.item_comboBox.setEnabled(False)
                self.bd.UpdateInfo(self.main_s_window.name_edit.text(), self.main_s_window.surname_edit.text(),
                                   self.main_s_window.class_edit.text(), self.login,
                                   self.main_s_window.item_comboBox.currentText())
                print("locked :(")
                print()

                if self.bd.InsertTeacherLine(self.main_s_window.item_edit.text(), self.login) == True:
                    pass
                else:
                    sp = self.bd.InsertTeacherLine(self.main_s_window.item_edit.text(), self.login)

                    self.main_s_window.name_teacher_edit.setText(sp[0][2])
                    self.main_s_window.level_edit.setText(sp[-1])

                if self.main_s_window.newpass_edit.text() != "":
                    self.bd.CheckPassword(self.login, self.main_s_window.newpass_edit.text(),
                                          self.main_s_window.oldpass_edit.text())
            else:
                print("Ошибка в одном из полей, пожалуйста, проверьте информацию.")

    def show_schedule(self):
        self.main_s_window.stackedWidget.setCurrentIndex(2)

    def update_schedule(self):
        file = open(f"{self.main_s_window.name_teacher_edit.text()}")
        sp = []
        slovar = {}
        for i in file:
            if i != "":
                sp.append(i.replace("\n", ""))
        for i in range(len(sp) - 1):
            if sp[i] != "":
                if sp[i][-1] == ":":
                    slovar[sp[i]] = sp[i + 1]
        self.main_s_window.mon_edit.setText(slovar["Monday:"])
        self.main_s_window.tue_edit.setText(slovar["Tuesday:"])
        self.main_s_window.wed_edit.setText(slovar["Wednesday:"])
        self.main_s_window.thu_edit.setText(slovar["Thursday:"])
        self.main_s_window.fri_edit.setText(slovar["Friday:"])
        self.main_s_window.sat_edit.setText(slovar["Saturaday:"])
        self.main_s_window.sun_edit.setText(slovar["Sunday:"])

    def check_checkboxes(self):
        if self.main_s_window.checkBox_2.isChecked() and self.main_s_window.checkBox_4.isChecked() and self.main_s_window.checkBox_6.isChecked():
            QMessageBox.information(self, 'Сообщение', 'Идет урок')
            self.show_lesson()
        else:
            QMessageBox.warning(self, 'Сообщение', 'Отметьте все пункты')

    def show_teachers(self):
        self.main_s_window.stackedWidget.setCurrentIndex(3)
        self.main_s_window.change_btn.clicked.connect(self.change_teacher)
        self.main_s_window.save_btn_2.clicked.connect(self.change_teacher)
        self.main_s_window.name_teacher_edit.text()
        self.main_s_window.item_edit.text()
        self.main_s_window.level_edit.text()
    def change_teacher(self):
        if self.bd.CheckClass(self.main_s_window.item_edit.text(), self.main_s_window.teachers_comboBox.currentText().split()[0]) == True:
            self.bd.DeleteClassInfo(self.main_s_window.name_teacher_edit.text(), self.main_s_window.item_edit.text())
            self.bd.UpdateClassInfo(self.login, self.name, self.cls, self.main_s_window.teachers_comboBox.currentText().split()[0], self.main_s_window.item_edit.text())

            sp = self.bd.InsertTeacherLine(self.main_s_window.item_edit.text(), self.login)
            self.main_s_window.name_teacher_edit.setText(sp[0][2])
            self.main_s_window.level_edit.setText(sp[-1])
        else:
            print("Занято епты")


    def show_lesson(self):
        self.main_s_window.stackedWidget.setCurrentIndex(4)

    def update_item_edit(self):
        selected_item = self.main_s_window.item_comboBox.currentText()
        self.main_s_window.item_edit.setText(selected_item)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = MainSWindow()
    main_window.show()
    sys.exit(app.exec())