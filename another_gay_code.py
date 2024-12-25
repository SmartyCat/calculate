from tkinter import *


class Interface:
    def __init__(self, main):
        self.d = {"red": "#ff0000"}
        self.label_top = Label(main, width=20, bg="grey")
        self.label_bottom = Label(main, width=20, bg="white")
        self.button_red = Button(main, width=4, height=2, bg="red")
        self.button_orange = Button(main, width=4, height=2, bg="orange")
        self.button_yellow = Button(main, width=4, height=2, bg="yellow")
        self.button_green = Button(main, width=4, height=2, bg="green")
        self.button_light_blue = Button(main, width=4, height=2, bg="lightblue")
        self.button_blue = Button(main, width=4, height=2, bg="blue")
        self.button_purple = Button(main, width=4, height=2, bg="purple")

        self.button_red["command"] = self.show_red
        self.button_orange["command"] = self.show_orange
        self.button_yellow["command"] = self.show_yellow
        self.button_green["command"] = self.show_green
        self.button_light_blue["command"] = self.show_lightblue
        self.button_blue["command"] = self.show_blue
        self.button_purple["command"] = self.show_purple

        self.label_top.pack()
        self.label_bottom.pack(padx=10, pady=10)
        self.button_red.pack(side=LEFT, padx=0, pady=3)
        self.button_orange.pack(side=LEFT, padx=3, pady=3)
        self.button_yellow.pack(side=LEFT, padx=3, pady=3)
        self.button_green.pack(side=LEFT, padx=3, pady=3)
        self.button_light_blue.pack(side=LEFT, padx=3, pady=3)
        self.button_blue.pack(side=LEFT, padx=3, pady=3)
        self.button_purple.pack(side=LEFT, padx=0, pady=3)

    def show_red(self):
        self.label_top["text"] = "red"
        self.label_bottom["text"] = "#007dff"

    def show_orange(self):
        self.label_top["text"] = "orange"
        self.label_bottom["text"] = "#ff7d00"

    def show_yellow(self):
        self.label_top["text"] = "yellow"
        self.label_bottom["text"] = "#ffff00"

    def show_green(self):
        self.label_top["text"] = "green"
        self.label_bottom["text"] = "#00ff00"

    def show_lightblue(self):
        self.label_top["text"] = "lightblue"
        self.label_bottom["text"] = "#007dff"

    def show_blue(self):
        self.label_top["text"] = "blue"
        self.label_bottom["text"] = "#0000ff"

    def show_purple(self):
        self.label_top["text"] = "purple"
        self.label_bottom["text"] = "#7d00ff"


root = Tk()
# root.geometry("200x250+200+200")
i = Interface(root)
root["bg"] = "grey"
root.mainloop()
