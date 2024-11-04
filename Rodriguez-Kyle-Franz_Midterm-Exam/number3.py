# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:43:44 2024

@author: KYLE FRANZ RODRIGUEZ
"""

from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel
from PyQt5.QtWidgets import QApplication
import sys

class leWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.body()

    
    def body(self):
        self.setWindowTitle("Special Midterm Exam in OOP")
        self.resize(400, 200)
        self.coloredbutton()
        self.textbox()
        self.show()
    
    def coloredbutton(self):
        self.lebutton = QPushButton("Click to Display your fullname", self)
        self.lebutton.setStyleSheet("color : red")
        self.lebutton.clicked.connect(self.clicked)
        self.lebutton.setGeometry(40, 100, 150, 25)
    
    def textbox(self):

        self.textbox1 = QLineEdit(self)
        self.textbox1.setGeometry(200, 60, 150, 25)
        self.textbox2 = QLineEdit(self)
        self.textbox2.setGeometry(200, 100, 150, 25)
        self.label1 = QLabel("Enter your fullname", self)
        self.label1.setStyleSheet("color : red")
        self.label1.setGeometry(45, 60, 150, 25)
    
    def clicked(self):
        fullname = self.textbox1.text()
        self.textbox2.setText(fullname)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = leWindow()
    sys.exit(app.exec_())