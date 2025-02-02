from tkinter import *


class Interface:
    def __init__(self):
        self.var = BooleanVar()

        self.frame = Frame()
        self.label = Label(width=20, height=10, bg="darkred")
        self.check_button = Checkbutton(
            self.frame,
            text="Input",
            variable=self.var,
            command=self.toggle_label_visibillity,
        )
        

        self.frame.pack(side=TOP)
        self.check_button.pack()

    def toggle_label_visibillity(self):

        if self.var.get():
            self.label.pack(side=BOTTOM)
        else:
            self.label.pack_forget()


root = Tk()

i = Interface()

root.mainloop()
