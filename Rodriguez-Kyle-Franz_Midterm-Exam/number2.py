# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:20:25 2024

@author: KYLE FRANZ RODRIGUEZ
"""

from PyQt5.QtWidgets import QMainWindow, QPushButton
from PyQt5.QtWidgets import QApplication
import sys

class leWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.body()

    
    def body(self):
        self.setWindowTitle("Special Midterm Exam in OOP")
        self.resize(300, 200)
        self.coloredbutton()
        self.show()
    
    def color_change(self):
        self.lebutton.setStyleSheet("background-color : yellow")
    
    def coloredbutton(self):
        self.lebutton = QPushButton("Click to Change Color", self)
        self.lebutton.clicked.connect(self.color_change)
        self.lebutton.setGeometry(50, 70, 200, 50)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = leWindow()
    sys.exit(app.exec_())
        