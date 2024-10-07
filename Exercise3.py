from tkinter import *
class MyCalculator:
    def __init__(self, win):
        # LABEL TITLE
        self.Label1 = Label(win, text="CALCULATOR", fg="blue")
        self.Label1.place(x=160,y=0)

        # First Entry
        self.Label2 = Label(win, text="Number 1:")
        self.Label2.place(x=80,y=80)
        self.Entry1 = Entry(win,bd=2)
        self.Entry1.place(x=150, y=80)

        # Second Entry
        self.Label3 = Label(win, text="Number 2:")
        self.Label3.place(x=80, y=120)
        self.Entry2 = Entry(win, bd=2)
        self.Entry2.place(x=150, y=120)

        # Result Entry
        self.Label3 = Label(win, text="Result:", fg="red")
        self.Label3.place(x=80, y=160)
        self.Entry3 = Entry(win, bd=2, fg="blue")
        self.Entry3.place(x=150, y=160)

        # Buttons
        # Add
        self.Button1 = Button(win, text=" + ", fg="red", command = self.add)
        self.Button1.place(x=152, y=200)

        # Subtract
        self.Button1 = Button(win, text=" - ", fg="red", command = self.subtract)
        self.Button1.place(x=184, y=200)

        # Multiply
        self.Button1 = Button(win, text=" * ", fg="red", command = self.multiply)
        self.Button1.place(x=216, y=200)

        # Divide
        self.Button1 = Button(win, text=" / ", fg="red", command = self.divide)
        self.Button1.place(x=248, y=200)

        # Button functions
    def add(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        sum = num1 + num2
        self.Entry3.delete(0,END)
        self.Entry3.insert(END,str(sum))

    def subtract(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        difference = num1 - num2
        self.Entry3.delete(0,END)
        self.Entry3.insert(END,str(difference))

    def multiply(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        product = num1 * num2
        self.Entry3.delete(0,END)
        self.Entry3.insert(END,str(product))

    def divide(self):
        num1 = int(self.Entry1.get())
        num2 = int(self.Entry2.get())
        quotient = num1 / num2
        self.Entry3.delete(0,END)
        self.Entry3.insert(END,str(quotient))
