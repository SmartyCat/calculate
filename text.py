from tkinter import *


class Inteface:
    def __init__(self, main):
        self.file = None
        self.f = Frame(main)
        self.f_b = Frame(main)
        self.entry = Entry(self.f, width=50, bg="grey", fg="yellow")
        self.button_open = Button(
            self.f, width=20, bg="black", fg="yellow", text="Open"
        )
        self.button_save = Button(
            self.f, width=20, bg="black", fg="yellow", text="Save"
        )
        self.text = Text(self.f_b, width=75, height=35, bg="darkgreen", fg="white")
        self.scroll_y = Scrollbar(command=self.text.yview)
        self.scroll_x = Scrollbar(command=self.text.xview, orient=HORIZONTAL)

        self.text.config(yscrollcommand=self.scroll_y.set)
        self.text.config(xscrollcommand=self.scroll_x.set)

        self.button_open["command"] = self.open_info
        self.button_save["command"] = self.save_info

        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.pack(side=BOTTOM, fil=X)
        self.f.pack()
        self.f_b.pack()
        self.entry.pack(side=LEFT, fill=Y)
        self.button_open.pack(side=LEFT)
        self.button_save.pack(side=LEFT)
        self.text.pack(side=BOTTOM)

    def open_info(self):
        self.text.delete(1.0, END)
        s = open(self.entry.get(), "r+")

        self.text.insert(1.0, s.read())
        self.file = s

    def save_info(self):
        x = self.text.get(1.0, END)
        self.file.seek(0)

        self.file.truncate()
        self.file.write("")
        self.file.write(x)
        self.file.close()


root = Tk()

i = Inteface(root)
root["bg"] = "purple"

root.mainloop()
