from tkinter import *
from Exercise3 import MyCalculator


window = Tk()
MyWin = MyCalculator(window)
window.geometry("400x300+10+10")
window.title("Mio Amato Calculator")
window.mainloop()
