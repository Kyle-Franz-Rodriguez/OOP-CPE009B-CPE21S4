# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:43:57 2024

@author: KYLE FRANZ RODRIGUEZ
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QLabel, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QIcon
import csv

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui()

    def ui(self):
        self.setWindowTitle("Account Registration")
        self.setWindowIcon(QIcon('Icon.png'))
        self.resize(300, 450)
        self.center()
        self.button1()
        self.button2()
        self.textboxes()
        self.show()

    def center(self):
        frame = self.frameGeometry()
        center_val = QDesktopWidget().availableGeometry().center()
        frame.moveCenter(center_val)
        self.move(frame.topLeft())

    def button1(self):
        self.button = QPushButton('Register', self)
        self.button.setToolTip('Finish your registration')
        self.button.move(100, 400)
        self.button.clicked.connect(self.button1_clicked)

    def button2(self):
        self.button = QPushButton('Clear entries', self)
        self.button.setToolTip('Clear your entries')
        self.button.move(100, 350)
        self.button.clicked.connect(self.button2_clicked)
        
    def textboxes(self):

        self.textbox1 = QLineEdit(self)
        self.textbox1.move(150, 20)
        self.textbox1.setText('')
        self.label1 = QLabel("First Name", self)
        self.label1.move(80, 20)
        
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(150, 70)
        self.textbox2.setText('')
        self.label2 = QLabel("Last name", self)
        self.label2.move(80, 70)
    
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(150, 120)
        self.textbox3.setText('')
        self.label3 = QLabel("Username", self)
        self.label3.move(80, 120)
    
        self.textbox4 = QLineEdit(self)
        self.textbox4.move(150, 170)
        self.textbox4.setText('')
        self.label4 = QLabel("Password", self)
        self.label4.move(80, 170)
    
        self.textbox5 = QLineEdit(self)
        self.textbox5.move(150, 220)
        self.textbox5.setText('')
        self.label5 = QLabel("Email Address", self)
        self.label5.move(60, 220)
    
        self.textbox6 = QLineEdit(self)
        self.textbox6.move(150, 270)
        self.textbox6.setText('')
        self.label6 = QLabel("Contact Number", self)
        self.label6.move(50, 270)
    
    @pyqtSlot()
    def button1_clicked(self):
        FirstName = self.textbox1.text()
        LastName = self.textbox2.text()
        Username = self.textbox3.text()
        Password = self.textbox4.text()
        EmailAddress = self.textbox5.text()
        ContactNumber = self.textbox6.text()
        
        if (FirstName == '' or LastName == '' or Username == '' or Password == '' or EmailAddress == '' or ContactNumber == ''):
            QMessageBox.information(self, "Account Registration Failed", "Registration failed. Missing entry", 
                                                QMessageBox.Ok, QMessageBox.Ok)
        
        else:
            itemscsv= {
                'FirstName': FirstName,'LastName': LastName, 
                'Username': Username,'Password': Password, 
                'EmailAddress': EmailAddress, 
                'ContactNumber': ContactNumber
                } 
            
            fields= list(itemscsv.keys()) 
            with open('Registered_Accounts',mode='a',encoding='utf-8',newline='') as maincsv: 
                csv_write= csv.DictWriter(maincsv, fieldnames=fields) 
                if maincsv.tell() == 0:
                    csv_write.writeheader() 
                    csv_write.writerow(itemscsv) 
                else:
                    csv_write.writerow(itemscsv) 
            maincsv.close
            
            QMessageBox.information(self, "Account Registered", "Your account has been registered successfully", 
                                                QMessageBox.Ok, QMessageBox.Ok)
   
    def button2_clicked(self):
        self.textbox1.setText('')
        self.textbox2.setText('')
        self.textbox3.setText('')
        self.textbox4.setText('')
        self.textbox5.setText('')
        self.textbox6.setText('')
    
