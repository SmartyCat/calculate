from tkinter import *


class Interface:
    def __init__(self, main):
        self.file = None
        self.frame_top = Frame(main)
        self.f_bottom = Frame(main)
        self.entry = Entry(self.frame_top, width=50, bg="grey", fg="yellow")
        self.button_open = Button(
            self.frame_top, width=20, bg="black", fg="yellow", text="Open"
        )
        self.button_save = Button(
            self.frame_top, width=20, bg="black", fg="yellow", text="Save"
        )
        self.text = Text(self.f_bottom, width=75, height=35, bg="darkgreen", fg="white")
        self.scroll_y = Scrollbar(command=self.text.yview)
        self.scroll_x = Scrollbar(command=self.text.xview, orient=HORIZONTAL)

        self.text.config(yscrollcommand=self.scroll_y.set)
        self.text.config(xscrollcommand=self.scroll_x.set)

        self.button_open["command"] = self.open_info
        self.button_save["command"] = self.save_info

        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.frame_top.pack()
        self.f_bottom.pack()
        self.entry.pack(side=LEFT, fill=Y)
        self.button_open.pack(side=LEFT)
        self.button_save.pack(side=LEFT)
        self.text.pack(side=BOTTOM)

    def open_info(self):
        try:
            self.text.delete(1.0, END)
            s = open(self.entry.get(), "r+")

            self.text.insert(1.0, s.read())
            self.file = s
            self.save_info()
        except FileNotFoundError as e:
            self.text.insert(1.0, f"\nError, file not find")

    def save_info(self):
        x = self.text.get(1.0, END)
        self.file.seek(0)

        self.file.truncate()
        self.file.write("")
        self.file.write(x)
        self.file.close()


root = Tk()

i = Interface(root)
root["bg"] = "purple"

root.mainloop()
