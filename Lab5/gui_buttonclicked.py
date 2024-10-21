# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:15:48 2024

@author: KYLE FRANZ RODRIGUEZ
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt Button"
        self.x = 200
        self.y = 200
        self.width = 300
        self.height = 300
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.x,self.y,self.width,self.height)
        self.setWindowIcon(QIcon('pythonico.ico'))
        
        #Modifications
        """self.button2 = QPushButton('Register',self)
        self.button2.setToolTip("This button does nothing.. yet")
        self.button2.move(100,50)"""
        
        #In GUI Python, these are called widgets
        self.button = QPushButton('Click me!', self)
        self.button.setToolTip("You've hover over me!")
        self.button.move(100,70) #button.move(x,y)
        self.button.clicked.connect(self.on_click)
        
        self.show()
    
    @pyqtSlot()
    def on_click(self):
        print("You clicked me!")
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

