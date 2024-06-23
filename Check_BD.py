import sqlite3
from PyQt6.QtWidgets import QMessageBox
from PyQt6 import QtCore
from main_window import *

class CheckThread(QWidget, QtCore.QThread):
    def __init__(self):
        super().__init__()
        self.start_main_t_window = MainTWindow()
        self.start_main_s_window = MainSWindow()
        self.text_box = QMessageBox(self)

    def thr_login(self, name, password):
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM Users WHERE login = ?", (name,))
        sp_users = cur.fetchall()
        print(sp_users)

        if sp_users:
            user_info = {row[1]: row[2] for row in sp_users}
            print(user_info)
            if name in user_info and user_info[name] == password:
                if sp_users[0][3] == "teacher":
                    self.StartMainTWindow(name)
                else:
                    print(name)
                    self.StartMainSWindow(name)
                return True
            else:
                self.text_box.setText("Введен неверный логин/пароль")
                self.text_box.show()
                return False
        else:
            self.text_box.setText("Введен неверный логин/пароль")
            self.text_box.show()
            return False
        con.close()

    def thr_register(self, log, password, name, cls):
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()

        sp_user = cur.execute(f"""SELECT * FROM users WHERE login = '{log}';""").fetchall()
        if sp_user != []:
            self.text_box.setText("Аккаунт с таким логином уже существует")
            self.text_box.show()
            return False

        elif sp_user == []:
            print(2)
            print(log, name, cls)
            cur.execute(f"""INSERT INTO users (login, password) VALUES ('{log}','{password}')""")
            print(3)
            cur.execute(f"""INSERT INTO information_about_users (login, name, level) VALUES ('{log}', '{name}', '{cls}')""")
            print(4)
            self.text_box.setText("Поздравляю с успешной регестрации аккаунта на платформе Бебрика!")
            self.text_box.show()
            con.commit()
            self.StartMainSWindow(log)
            con.close()
            return True

    def StartMainTWindow(self, login):
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        info_users = cur.execute(f"""SELECT * FROM information_about_users WHERE login = '{login}';""").fetchall()
        self.start_main_t_window.infomation_users(info_users[0][2], info_users[0][3], info_users[0][5], info_users[0][1], info_users[0][6])
        self.start_main_t_window.show()
        con.close()

    def StartMainSWindow(self, login):
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        info_users = cur.execute(f"""SELECT * FROM information_about_users WHERE login = '{login}';""").fetchall()
        self.start_main_s_window.show()
        self.start_main_s_window.infomation_users(info_users[0][2], info_users[0][5], info_users[0][1], info_users[0][3])
        con.close()