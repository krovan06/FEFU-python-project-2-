import sqlite3

class FoundInsertInfo():
    def __init__(self):
        pass

    def InsertClassInfo(self):
        count = 0
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        sp_info = cur.execute("SELECT * FROM information_about_users WHERE prof = 'teacher'").fetchall()
        sp_teacher = cur.execute("SELECT * FROM class").fetchall()
        for i in sp_info:
            for j in sp_teacher:
                if i[1] in j:
                    count += 1
            if count == 0:
                cur.execute(f"""INSERT INTO class (loginTeacher, nameTeacher, subject) VALUES ('{i[1]}','{i[2]}','{i[6]}')""")
                con.commit()
        con.close()

    def UpdateInfo(self, name, surname, cls, login, subject):
        print("save...")
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        cur.execute("UPDATE information_about_users SET name = ?, surname = ?, level = ?, subject = ? WHERE login = ?", (name, surname, cls, subject, login))
        cur.execute("UPDATE class SET nameTeacher = ?, subject = ? WHERE loginTeacher = ?", (name, subject, login))
        con.commit()
        con.close()
        print("saved")

    def CheckPassword(self, login, new_password, old_password):
        print("cheking your pass")
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        sp = cur.execute(f"SELECT password FROM users WHERE login = '{login}';").fetchall()
        if sp[0][0] == old_password:
            self.UpdatePassword(login, new_password)
        else:
            print("your password is not correct")

    def UpdatePassword(self, login, password):
        print("update password...")
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        cur.execute("UPDATE users SET password = ? WHERE login = ?", (password, login))
        con.commit()
        con.close()
        print("password updated")

    def CheckClass(self, name, subject):
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        sp = cur.execute(f"SELECT * FROM class WHERE nameTeacher = '{name}' AND subject = '{subject}';").fetchall()
        if sp[0][3] == None:
            self.UpdateClassInfo()
        con.close()

    def UpdateClassInfo(self):
        print("мяу")