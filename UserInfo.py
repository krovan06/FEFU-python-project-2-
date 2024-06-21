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
                if i[1] in j[1]:
                    count += 1
            if count == 0:
                cur.execute(f"""INSERT INTO class (loginTeacher, nameTeacher, subject) VALUES ('{i[1]}','{i[2]}','{i[6]}')""")
                con.commit()
            count = 0
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
        print()

    def CheckPassword(self, login, new_password, old_password):
        print("cheking your pass")
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        sp = cur.execute(f"SELECT password FROM users WHERE login = '{login}';").fetchall()
        if sp[0][0] == old_password and new_password != old_password:
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
        print()

    def CheckClass(self, subject, nameTeacher):
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        sp_check = cur.execute(f"SELECT * FROM class WHERE subject = '{subject}' AND nameTeacher = '{nameTeacher}';").fetchall()
        print(sp_check, "CheckClass", nameTeacher, subject)
        if sp_check[0][3] == "" or sp_check[0][3] == None:
            print("True")
            return True
        else:
            return False
        con.close()

    def InsertTeacherLine(self, subject, login):
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        sp = []
        sp_check = cur.execute(f"SELECT * FROM class WHERE subject = '{subject}';").fetchall()
        print(sp_check, "INSERT")
        for i in sp_check:
            if login in i:
                sp.append(i)
                cls = cur.execute(f"SELECT level FROM information_about_users WHERE login = '{i[1]}';").fetchall()
                sp.append(cls[0][0])
                return sp

        return True

        con.close()

    def UpdateClassInfo(self, loginStudent, nameStudent, cls, nameTeacher, subject):
        print("Update your class info...")
        print(loginStudent, nameStudent, cls, nameTeacher, subject)
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        cur.execute("UPDATE class SET loginStudent = ?, nameStudent = ?, class = ? WHERE nameTeacher = ? AND subject = ?", (loginStudent, nameStudent, cls, nameTeacher, subject))
        con.commit()
        con.close()
        print("Updated")
        print()

    def DeleteClassInfo(self, nameTeacher, subject):
        print("Delete")
        con = sqlite3.connect("bebrica.db")
        cur = con.cursor()
        cur.execute("DELETE from class WHERE nameTeacher = ? AND subject = ?", (nameTeacher, subject))
        con.commit()
        con.close()
        self.InsertClassInfo()
        print("Deleted")