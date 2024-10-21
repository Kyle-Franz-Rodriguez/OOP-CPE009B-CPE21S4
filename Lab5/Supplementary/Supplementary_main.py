# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:40:53 2024

@author: KYLE FRANZ RODRIGUEZ
"""

import sys
from Supplementary_func import MyApp
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

