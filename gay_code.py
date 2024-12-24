from tkinter import *


class Interface:
    def __init__(self, main):
        self.labe_1 = Label(main, width=20, bg="grey", fg="black")
        self.labe_2 = Label(main, width=20, bg="white", fg="black")
        self.button_red = Button(main, width=20, bg="#ff0000")
        self.button_orange = Button(width=20, bg="#ff7d00")
        self.button_yellow = Button(width=20, bg="#ffff00")
        self.button_green = Button(width=20, bg="#00ff00")
        self.button_blue = Button(width=20, bg="#007dff")
        self.button_another_blue = Button(width=20, bg="#0000ff")
        self.button_purple = Button(width=20, bg="#7d00ff")

        self.button_red["command"] = self.show_red
        self.button_orange["command"] = self.show_orange
        self.button_yellow["command"] = self.show_yellow
        self.button_green["command"] = self.show_green
        self.button_blue["command"] = self.show_blue
        self.button_another_blue["command"] = self.show_another_blue
        self.button_purple["command"] = self.show_purple

        self.labe_1.pack()
        self.labe_2.pack()
        self.button_red.pack()
        self.button_orange.pack()
        self.button_yellow.pack()
        self.button_green.pack()
        self.button_blue.pack()
        self.button_another_blue.pack()
        self.button_purple.pack()

    def show_red(self):
        self.labe_1["text"] = "red"
        self.labe_2["text"] = "#ff0000"

    def show_orange(self):
        self.labe_1["text"] = "orange"
        self.labe_2["text"] = "#ff7d00"

    def show_yellow(self):
        self.labe_1["text"] = "yellow"
        self.labe_2["text"] = "#ffff00"

    def show_green(self):
        self.labe_1["text"] = "green"
        self.labe_2["text"] = "#00ff00"

    def show_blue(self):
        self.labe_1["text"] = "blue"
        self.labe_2["text"] = "#007dff"

    def show_another_blue(self):
        self.labe_1["text"] = "another blue"
        self.labe_2["text"] = "#0000ff"

    def show_purple(self):
        self.labe_1["text"] = "purple"
        self.labe_2["text"] = "#7d00ff"


root = Tk()

i = Interface(root)

root.mainloop()
