from tkinter import *


class Interface:
    def __init__(self, info_1, info_2, info_3):
        self.info_1 = info_1
        self.info_2 = info_2
        self.info_3 = info_3
        self.frame = Frame()
        self.radio_button_1 = Radiobutton(
            text="Вася",
            variable=var,
            value=0,
            indicatoron=False,
            height=3,
            width=7,
            bg="grey",
            command=lambda i=self.info_1: self.show_info(i),
        )
        self.radio_button_2 = Radiobutton(
            text="Петя",
            variable=var,
            value=1,
            indicatoron=False,
            height=3,
            width=7,
            bg="grey",
            command=lambda i=self.info_2: self.show_info(i),
        )
        self.radio_button_3 = Radiobutton(
            text="Маша",
            variable=var,
            value=2,
            indicatoron=False,
            height=3,
            width=7,
            bg="grey",
            command=lambda i=self.info_3: self.show_info(i),
        )
        self.label = Label(width=30, height=10, bg="darkgreen", text=self.info_1)

        self.label.pack(side=RIGHT, fill=Y)
        self.frame.pack(side=LEFT)
        self.radio_button_1.pack(anchor=W)
        self.radio_button_2.pack(anchor=W)
        self.radio_button_3.pack(anchor=W)

    def show_info(self, info):
        self.label["text"] = info


root = Tk()
var = IntVar()
var.set(0)
i = Interface("+380976512345", "+38098771266", "+6788457711")

root.mainloop()
