from tkinter import *


class Calculator:
    def __init__(self, main):
        self.frame = Frame()
        self.frame_b = Frame()
        self.entry = Text(self.frame, width=40, height=3, bg="brown")
        self.button_ac = Button(self.frame, width=3, height=1, text="AC", bg="purple")
        self.button_x = Button(self.frame, width=3, height=1, text="del", bg="purple")
        self.button_per = Button(self.frame, width=3, height=1, text="%", bg="purple")
        self.button_div = Button(self.frame, width=3, height=1, text="/", bg="purple")
        self.button_mul = Button(self.frame, width=3, height=1, text="x", bg="purple")
        self.button_sub = Button(self.frame, width=3, height=1, text="-", bg="purple")
        self.button_add = Button(self.frame, width=3, height=1, text="+", bg="purple")
        self.button_d = Button(self.frame, width=3, height=1, text=",", bg="purple")
        self.button_sqrt = Button(self.frame, width=3, height=1, text="√", bg="purple")
        self.button_eq = Button(
            self.frame, width=3, height=1, text="=", bg="black", fg="green"
        )
        self.button_1 = Button(
            self.frame_b, width=3, height=1, text="1", bg="darkgreen"
        )
        self.button_2 = Button(
            self.frame_b, width=3, height=1, text="2", bg="darkgreen"
        )
        self.button_3 = Button(
            self.frame_b, width=3, height=1, text="3", bg="darkgreen"
        )
        self.button_4 = Button(
            self.frame_b, width=3, height=1, text="4", bg="darkgreen"
        )
        self.button_5 = Button(
            self.frame_b, width=3, height=1, text="5", bg="darkgreen"
        )
        self.button_6 = Button(
            self.frame_b, width=3, height=1, text="6", bg="darkgreen"
        )
        self.button_7 = Button(
            self.frame_b, width=3, height=1, text="7", bg="darkgreen"
        )
        self.button_8 = Button(
            self.frame_b, width=3, height=1, text="8", bg="darkgreen"
        )
        self.button_9 = Button(
            self.frame_b, width=3, height=1, text="9", bg="darkgreen"
        )
        self.button_0 = Button(
            self.frame_b, width=3, height=1, text="0", bg="darkgreen"
        )

        self.frame.pack(side=TOP)
        self.frame_b.pack(side=LEFT)
        self.entry.pack(side=TOP)
        self.button_ac.pack(side=LEFT)
        self.button_x.pack(side=LEFT)
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


root = Tk()

root.title("Calculator")
root["bg"] = "darkgrey"
root.geometry("310x100")

c = Calculator(root)

root.mainloop()
