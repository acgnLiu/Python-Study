import sys

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QLineEdit, QHBoxLayout, QVBoxLayout, QGridLayout


class Login(QWidget):

    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 400, 700)
        self.setWindowTitle("PyQt6 Login Window")
        self.setFixedWidth(700)
        self.setFixedHeight(400)

        self.setStyleSheet("background-color:black")
        # self.setWindowOpacity(0.5)

        self.create_lineedit()
        self.create_btn()
        self.create_label()
        self.create_Layout()

    def create_label(self):
        self.label_1 = QLabel("第一个标签")

    def create_btn(self):
        self.btn_1 = QPushButton("第一个按键")

    def create_lineedit(self):

        self.line_edit = QLineEdit()
        self.line_edit.setFont(QFont("Sanserif", 15))
        # line_edit.setText("Default Text")
        self.line_edit.setPlaceholderText("Please enter your username.")
        # line_edit.setEnabled(False)
        # line_edit.setEchoMode(QLineEdit.EchoMode.Password)

    def create_Layout(self):

        hbox = QHBoxLayout()
        hbox.addWidget(self.line_edit)
        hbox.addWidget(self.btn_1)
        hbox.addWidget(self.label_1)
        self.setLayout(hbox)

        # vbox = QVBoxLayout()
        # vbox.addWidget(self.btn_1)
        # vbox.addWidget(self.label_1)
        # vbox.addWidget(self.line_edit)
        # self.setLayout(vbox)

    def create_grid(self):

        grid = QGridLayout()






app = QApplication(sys.argv)

window = Login()

window.show()

sys.exit(app.exec())