# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 08:18:26 2024

@author: KYLE FRANZ RODRIGUEZ
"""
from FileReaderWriter import FileReaderWriter
from CSVFileReaderWriter import CSVFileReaderWriter
from JSONFileReaderWriter import JSONFileReaderWriter
#This is for SUPPLEMENTARY ACTIVITY
from TextFileReaderWriter import TextFileReaderWriter

df = FileReaderWriter()
df.read()
df.write()

c = CSVFileReaderWriter()
c.read("sample.csv")
c.write(filepath="sample2.csv", data=["Hello","World"])

j = JSONFileReaderWriter()
j.read("sample.json")
j.write(data=['foo', {'bar': ('baz', None, 1.0, 2)}],filepath="sample2.json")

#This is for SUPPLEMENTARY ACTIVITY
t = TextFileReaderWriter()
print("This is what it says in the file:",t.read("sample.txt"))
userin=input("Type something to change it- ")
t.write("sample.txt", userin)
print(f"Text file changed to[{userin}]")
