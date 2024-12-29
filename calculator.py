from tkinter import *
import re


class Calculator:
    def __init__(self, main):
        self.frame = Frame()
        self.frame_b = Frame()
        self.entry = Text(self.frame, width=40, height=3, bg="brown")
        self.button_ac = Button(
            self.frame, width=3, height=1, text="AC", bg="purple", command=self.del_all
        )
        self.button_del = Button(
            self.frame,
            width=3,
            height=1,
            text="del",
            bg="purple",
            command=self.del_last,
        )
        self.button_per = Button(
            self.frame,
            width=3,
            height=1,
            text="%",
            bg="purple",
            command=self.give_perce,
        )
        self.button_div = Button(
            self.frame,
            width=3,
            height=1,
            text="/",
            bg="purple",
            command=lambda i="/": self.add_to_text(i),
        )
        self.button_mul = Button(
            self.frame,
            width=3,
            height=1,
            text="x",
            bg="purple",
            command=lambda i="x": self.add_to_text(i),
        )
        self.button_sub = Button(
            self.frame,
            width=3,
            height=1,
            text="-",
            bg="purple",
            command=lambda i="-": self.add_to_text(i),
        )
        self.button_add = Button(
            self.frame,
            width=3,
            height=1,
            text="+",
            bg="purple",
            command=lambda i="+": self.add_to_text(i),
        )
        self.button_d = Button(
            self.frame,
            width=3,
            height=1,
            text=".",
            bg="purple",
            command=lambda i=".": self.add_to_text(i),
        )
        self.button_sqrt = Button(self.frame, width=3, height=1, text="√", bg="purple")
        self.button_eq = Button(
            self.frame,
            width=3,
            height=1,
            text="=",
            bg="black",
            fg="green",
            command=self.equel,
        )
        self.button_1 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="1",
            bg="darkgreen",
            command=lambda i="1": self.add_to_text(i),
        )
        self.button_2 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="2",
            bg="darkgreen",
            command=lambda i="2": self.add_to_text(i),
        )
        self.button_3 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="3",
            bg="darkgreen",
            command=lambda i="3": self.add_to_text(i),
        )
        self.button_4 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="4",
            bg="darkgreen",
            command=lambda i="4": self.add_to_text(i),
        )
        self.button_5 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="5",
            bg="darkgreen",
            command=lambda i="5": self.add_to_text(i),
        )
        self.button_6 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="6",
            bg="darkgreen",
            command=lambda i="6": self.add_to_text(i),
        )
        self.button_7 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="7",
            bg="darkgreen",
            command=lambda i="7": self.add_to_text(i),
        )
        self.button_8 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="8",
            bg="darkgreen",
            command=lambda i="8": self.add_to_text(i),
        )
        self.button_9 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="9",
            bg="darkgreen",
            command=lambda i="9": self.add_to_text(i),
        )
        self.button_0 = Button(
            self.frame_b,
            width=3,
            height=1,
            text="0",
            bg="darkgreen",
            command=lambda i="0": self.add_to_text(i),
        )

        self.frame.pack(side=TOP)
        self.frame_b.pack(side=LEFT)
        self.entry.pack(side=TOP)
        self.button_ac.pack(side=LEFT)
        self.button_del.pack(side=LEFT)
        self.button_per.pack(side=LEFT)
        self.button_div.pack(side=LEFT)
        self.button_mul.pack(side=LEFT)
        self.button_sub.pack(side=LEFT)
        self.button_add.pack(side=LEFT)
        self.button_d.pack(side=LEFT)
        self.button_sqrt.pack(side=LEFT)
        self.button_eq.pack(side=LEFT)
        self.button_1.pack(side=LEFT)
        self.button_2.pack(side=LEFT)
        self.button_3.pack(side=LEFT)
        self.button_4.pack(side=LEFT)
        self.button_5.pack(side=LEFT)
        self.button_6.pack(side=LEFT)
        self.button_7.pack(side=LEFT)
        self.button_8.pack(side=LEFT)
        self.button_9.pack(side=LEFT)
        self.button_0.pack(side=LEFT)

        self.entry.bind("<Key>",lambda e: "break")

    def add_to_text(self, x):
        self.entry.insert(END, x)

    def del_all(self):
        self.entry.delete(1.0, END)

    def del_last(self):
        self.entry.delete("end-2c")

    def give_perce(self):
        x = self.entry.get(1.0, END)
        try:
            if "." in x:
                x = float(eval(x))
                self.entry.insert(END, "=" + str(x / 100))
            else:
                x = int(eval(x))
                self.entry.insert(END, "=" + str(x / 100))
        except ValueError as e:
            self.entry.delete(1.0,END)
            self.entry.insert(1.0, "Error")

    def equel(self):
        exp = self.entry.get(1.0, END).strip()
        try:
            result = eval(exp)
            self.entry.insert(END, "=" + str(result))
        except Exception:
            self.entry.delete(1.0,END)
            self.entry.insert(1.0,"Error")
        

root = Tk()

root.title("Calculator")
root["bg"] = "darkgrey"
root.geometry("310x100")

c = Calculator(root)

root.mainloop()
