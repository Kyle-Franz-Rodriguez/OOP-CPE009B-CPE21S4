# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:42:17 2024

@author: KYLE FRANZ RODRIGUEZ
"""
from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read(self, filepath):
        with open(filepath, 'r') as readfile:
            data = readfile.readlines()
            for line in data:
                print(line.strip())
            return data

    def write(self, filepath, data):
        with open(filepath, 'w') as writefile:
            writefile.write(data)
            