from tkinter import *


class Calc:
    def __init__(self, main):
        self.ent_top = Entry(main, width=20, bg="purple", fg="yellow")
        self.ent_down = Entry(main, width=20, bg="blue", fg="yellow")
        self.but_plus = Button(main, text="+")
        self.but_minus = Button(main, text="-")
        self.but_mul = Button(main, text="*")
        self.but_dev = Button(main, text="/")
        self.label = Label(main, bg="black", fg="yellow")
        self.but_plus["command"] = self.add
        self.but_minus["command"] = self.sub
        self.but_mul["command"] = self.mul
        self.but_dev["command"] = self.dev
        self.ent_top.pack()
        self.ent_down.pack()
        self.but_plus.pack()
        self.but_minus.pack()
        self.but_mul.pack()
        self.but_dev.pack()
        self.label.pack()

    def add(self):

        self.label["text"] = self.take_number()[0] + self.take_number()[1]

    def sub(self):

        self.label["text"] = round(self.take_number()[0] - self.take_number()[1], 2)

    def mul(self):

        self.label["text"] = round(self.take_number()[0] * self.take_number()[1], 2)

    def dev(self):
        self.label["text"] = round(self.take_number()[0] / self.take_number()[1], 2)

    def take_number(self):
        num1 = self.check_number(self.ent_top.get())
        num2 = self.check_number(self.ent_down.get())
        return (num1, num2)

    def check_number(self, x):
        if (
            "." in x
            and x.index(".") != 0
            and x.count(".") == 1
            and x.index(".") != len(x) - 1
        ):
            return float(x)
        elif x.isdigit():
            return int(x)
        else:
            self.label["text"] = "Error"


root = Tk()
c = Calc(root)

root.mainloop()
