import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton, QWidget, QHBoxLayout

class ScheduleApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weekly Schedule")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)

        self.title = QLabel("Weekly Schedule", self)
        self.title.setStyleSheet("font-size: 24px; font-weight: bold;")
        self.main_layout.addWidget(self.title)

        self.days_text_edit = {}

        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

        for day in days_of_week:
            self.add_day_section(day)

        self.save_button = QPushButton("Save Schedule", self)
        self.save_button.clicked.connect(self.save_schedule)

        self.load_button = QPushButton("Load suka", self)
        self.load_button.clicked.connect(self.load_schedule)

        self.main_layout.addWidget(self.save_button)
        self.main_layout.addWidget(self.load_button)

        self.load_schedule()

    def add_day_section(self, day):
        layout = QVBoxLayout()

        # Заголовок дня
        label = QLabel(day, self)
        label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(label)

        # Текстовое поле для ввода задач
        text_edit = QTextEdit(self)
        layout.addWidget(text_edit)

        self.days_text_edit[day] = text_edit
        self.main_layout.addLayout(layout)

    def save_schedule(self):
        # Получение задач из текстовых полей и сохранение их в файл
        with open("weekly_schedule.txt", "w") as file:
            for day, text_edit in self.days_text_edit.items():
                tasks = text_edit.toPlainText()
                file.write(f"{day}:\n{tasks}\n")

        print("Schedule saved to weekly_schedule.txt")

    def load_schedule(self):
        file = open("weekly_schedule.txt")
        sp = []
        for i in file:
            if i != "":
                sp.append(i.replace("\n", ""))
        for i in range(len(sp) - 1):
            if sp[i] != "":
                if sp[i][-1] == ":":
                    self.days_text_edit[sp[i][0:-1]].setText(sp[i + 1])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScheduleApp()
    window.show()
    sys.exit(app.exec())